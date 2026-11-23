"""Verify original data bytes; no third-party dependencies or file writes."""
from pathlib import Path
import hashlib
import json


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'DATASET_MANIFEST.json').read_text(encoding='utf-8'))
    for item in manifest['files']:
        path = root / item['path']
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != item['sha256'] or path.stat().st_size != item['bytes']:
            raise SystemExit('FAILED: ' + item['path'])
        print('OK:', item['path'], item['sha256'])
    print('All data-file checksums match the release manifest.')


if __name__ == '__main__':
    main()
