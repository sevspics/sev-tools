#!/usr/bin/env bash
# Bootstrap a new client folder from the template.
# Usage: ./scripts/new-client.sh [client-slug]
#
# Claude Code should call this, then populate the files with real content.

set -e

if [ -z "$1" ]; then
  echo "Usage: $0 [client-slug]"
  echo "Example: $0 living-oceans"
  exit 1
fi

SLUG="$1"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TEMPLATE="$ROOT/_template"
TARGET="$ROOT/clients/$SLUG"

if [ -d "$TARGET" ]; then
  echo "Error: clients/$SLUG already exists."
  echo "Use 'update client $SLUG' instead, or delete the folder first."
  exit 1
fi

echo "Creating clients/$SLUG from template..."
mkdir -p "$TARGET/iterations"

cp "$TEMPLATE/matrix.html" "$TARGET/matrix.html"
cp "$TEMPLATE/research.md" "$TARGET/research.md"
cp "$TEMPLATE/notes.md" "$TARGET/notes.md"
cp "$TEMPLATE/README.md" "$TARGET/README.md"

# Replace simple placeholders
DATE=$(date "+%d %b %Y")
for f in "$TARGET/matrix.html" "$TARGET/research.md" "$TARGET/notes.md" "$TARGET/README.md"; do
  sed -i.bak "s|{{CLIENT_SLUG}}|$SLUG|g; s|{{DATE}}|$DATE|g; s|{{VERSION}}|1|g" "$f"
  rm "$f.bak"
done

echo "Done. Folder ready at: clients/$SLUG/"
echo ""
echo "Next: Claude Code should now populate the placeholders with real research."
echo "Placeholders still to fill:"
echo "  {{CLIENT_NAME}}, {{CLIENT_TAGLINE}}, {{CLIENT_URL}}, {{INDUSTRY}},"
echo "  {{ICP}}, {{POSITIONING}}, {{AVG_CLIENT_VALUE}}, {{VIDEOS_PER_MONTH}},"
echo "  {{LONG_FORM_PER_MONTH}}"
echo ""
echo "Plus all the content blocks marked with HTML comments in matrix.html."
