# Release notes

## v1.0.1

Preserves the original CSV line endings by marking dataset files as binary
for Git's text-conversion rules. The public downloads match the SHA-256
values in `DATASET_MANIFEST.json` byte for byte. No numerical data values
were changed.

## v1.0.0

Initial upload. Git's automatic line-ending normalization affected the CSV
bytes. Use v1.0.1 for a download matching the original-file checksums.
