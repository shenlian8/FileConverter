# Text File Encoding Converter

A simplified Python script to batch convert text files from Chinese encodings (GBK, GB18030, Big5) to UTF-8.

## Features

- **Recursive Search**: Scans a specified directory and all its subdirectories for `.txt` files.
- **Auto-Detection**: Attempts to detect if a file is encoded in `utf-8`, `gb18030` (covers GBK/GB2312), or `big5`.
- **Safe Conversion**: Reads the file and saves a converted copy with a `_utf8.txt` suffix (e.g., `document.txt` -> `document_utf8.txt`). Original files are untouched.
- **Skipping**: Skips files that are already UTF-8.

## Usage

1.  Ensure you have Python 3 installed.
2.  Run the script from the command line, providing the target directory:

```bash
python convert_encoding.py "C:\Path\To\Your\Files"
```

## Example Output

```text
Scanning directory: M:\Archive
Converted: M:\Archive\old_doc.txt (gb18030) -> M:\Archive\old_doc_utf8.txt
Skipped: M:\Archive\new_doc.txt (Already UTF-8)
Failed: M:\Archive\image.txt (Convertion Failed)
```

## Notes

- This script is designed specifically for text files that might be in Simplified Chinese (GBK/GB18030) or Traditional Chinese (Big5).
- If detection between Big5 and GBK is ambiguous, it defaults to GB18030 (Simplified).
