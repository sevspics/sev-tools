#!/usr/bin/env python3
"""
Regenerate clients/index.html — the landing page showing all active client
matrices. Run after any client add/update.

Usage:
    python3 scripts/build-index.py

Scans clients/*/matrix.html, reads the client name and date from each,
and produces a visual directory grid.
"""

import os
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CLIENTS_DIR = ROOT / "clients"
OUTPUT = CLIENTS_DIR / "index.html"


def extract_client_info(matrix_path: Path) -> dict:
    """Pull client name, date, version from a matrix.html file."""
    content = matrix_path.read_text(encoding="utf-8")

    # Name from <h1 class="client-name">
    name_match = re.search(r'<h1 class="client-name">(.+?)</h1>', content)
    name = name_match.group(1).strip() if name_match else matrix_path.parent.name

    # Tagline
    tag_match = re.search(r'<div class="client-tagline">(.+?)</div>', content)
    tagline = tag_match.group(1).strip() if tag_match else ""

    # Version + date from masthead-top second span
    meta_match = re.search(r'Generated (.+?) ·.+?V(\d+)', content)
    date = meta_match.group(1).strip() if meta_match else ""
    version = meta_match.group(2).strip() if meta_match else "1"

    return {
        "slug": matrix_path.parent.name,
        "name": name,
        "tagline": tagline,
        "date": date,
        "version": version,
    }


def scan_clients() -> list[dict]:
    """Find all clients/*/matrix.html files."""
    clients = []
    if not CLIENTS_DIR.exists():
        return clients
    for entry in sorted(CLIENTS_DIR.iterdir()):
        if not entry.is_dir() or entry.name.startswith("_"):
            continue
        matrix_path = entry / "matrix.html"
        if matrix_path.exists():
            clients.append(extract_client_info(matrix_path))
    return clients


def render_index(clients: list[dict]) -> str:
    """Render the index.html."""
    today = datetime.now().strftime("%d %b %Y")
    count = len(clients)

    cards = []
    for c in clients:
        cards.append(f"""
        <a class="client-card" href="{c['slug']}/matrix.html">
          <div class="client-card-meta">
            <span>V{c['version']}</span>
            <span>{c['date']}</span>
          </div>
          <h3>{c['name']}</h3>
          <p>{c['tagline']}</p>
          <div class="client-card-footer">View matrix →</div>
        </a>
        """)

    cards_html = "\n".join(cards) if cards else """
      <div class="empty-state">
        <p>No client matrices yet.</p>
        <p class="muted">Run "new client [slug]" in Claude Code to start.</p>
      </div>
    """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Content Matrix · Client Directory</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../_assets/styles.css">
<style>
.directory-grid {{
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 16px;
  margin-top: 32px;
}}
.client-card {{
  background: var(--surface);
  border: 1px solid var(--border);
  padding: 28px 24px;
  text-decoration: none;
  color: var(--text);
  transition: all 0.15s;
  display: block;
}}
.client-card:hover {{
  background: var(--surface-2);
  border-color: var(--accent-dim);
}}
.client-card-meta {{
  display: flex;
  justify-content: space-between;
  font-family: var(--font-mono);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--text-faint);
  margin-bottom: 20px;
}}
.client-card h3 {{
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 8px;
  letter-spacing: -0.01em;
}}
.client-card p {{
  font-family: var(--font-mono);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent);
  margin-bottom: 24px;
}}
.client-card-footer {{
  font-family: var(--font-mono);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  color: var(--text-dim);
  padding-top: 16px;
  border-top: 1px solid var(--border);
}}
.empty-state {{
  grid-column: 1 / -1;
  text-align: center;
  padding: 64px 24px;
  color: var(--text-dim);
  border: 1px dashed var(--border);
}}
.empty-state .muted {{
  color: var(--text-faint);
  font-family: var(--font-mono);
  font-size: 12px;
  margin-top: 8px;
}}
</style>
</head>
<body class="view-client">
<div class="shell">

<header class="masthead">
  <div class="masthead-top">
    <span class="label">Content Matrix · Directory</span>
    <span>{count} {'client' if count == 1 else 'clients'} · Updated {today}</span>
  </div>
  <div class="masthead-main">
    <div>
      <h1 class="client-name">Client Matrices</h1>
      <div class="client-tagline">6×6 Content Systems · Sev's Advisory</div>
    </div>
  </div>
</header>

<div class="directory-grid">
{cards_html}
</div>

<footer class="meta-footer" style="margin-top: 80px;">
  <span>sev-tools / matrix · auto-generated index</span>
  <span>Built on the 6×6 methodology</span>
</footer>

</div>
</body>
</html>
"""


def main():
    clients = scan_clients()
    html = render_index(clients)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Generated {OUTPUT.relative_to(ROOT)} with {len(clients)} clients.")


if __name__ == "__main__":
    main()
