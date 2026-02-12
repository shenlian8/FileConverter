import os
import subprocess

# Run the conversion script
subprocess.run(['python', 'convert_encoding.py', 'test_files'], check=True)

# Verify results
expected_output = {
    'test_files/utf8.txt': 'This is a UTF-8 file.\n中文测试',
    'test_files/gbk_utf8.txt': 'This is a GBK file.\n中文测试',
    'test_files/big5_utf8.txt': 'This is a Big5 file.\n中文測試'
}

for file_path, expected_content in expected_output.items():
    if not os.path.exists(file_path):
        print(f"FAIL: {file_path} not created.")
        continue
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if content.strip() == expected_content.strip():
                print(f"PASS: {file_path} content verified.")
            else:
                print(f"FAIL: {file_path} content mismatch.\nExpected: {expected_content}\nGot: {content}")
    except Exception as e:
        print(f"FAIL: Error reading {file_path}: {e}")

# Check that original non-utf8 files still exist
if os.path.exists('test_files/gbk.txt') and os.path.exists('test_files/big5.txt'):
    print("PASS: Original files preserved.")
else:
    print("FAIL: Original files deleted.")
