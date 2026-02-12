import os
import argparse

def convert_encoding(file_path):
    """
    Attempts to read a file with different encodings and save it as UTF-8
    if it's not already UTF-8.
    """
    encodings_to_try = ['utf-8', 'gb18030', 'big5']
    
    content = ""
    detected_encoding = None

    for encoding in encodings_to_try:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
            detected_encoding = encoding
            break
        except UnicodeDecodeError:
            continue
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return
    
    if detected_encoding is None:
        print(f"Failed: {file_path} (Convertion Failed)")
        return

    if detected_encoding == 'utf-8':
        print(f"Skipped: {file_path} (Already UTF-8)")
        return

    # Construct new file path
    base, ext = os.path.splitext(file_path)
    new_file_path = f"{base}_utf8{ext}"

    try:
        with open(new_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Converted: {file_path} ({detected_encoding}) -> {new_file_path}")
    except Exception as e:
        print(f"Error writing {new_file_path}: {e}")

def process_directory(directory):
    """
    recursively searches for .txt files in the directory and processes them.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.txt'):
                file_path = os.path.join(root, file)
                convert_encoding(file_path)

if __name__ == "__main__":
    print("Starting process...", flush=True)
    parser = argparse.ArgumentParser(description="Convert .txt files to UTF-8.")
    parser.add_argument("directory", help="Directory to search for .txt files")
    args = parser.parse_args()

    print(f"Checking directory: {args.directory}", flush=True)
    if not os.path.exists(args.directory):
        print(f"Error: Directory '{args.directory}' does not exist.", flush=True)
    elif not os.path.isdir(args.directory):
        print(f"Error: '{args.directory}' is not a directory.", flush=True)
    else:
        print(f"Scanning directory: {args.directory}", flush=True)
        process_directory(args.directory)
