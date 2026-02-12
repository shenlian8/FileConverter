file_path = 'test_files/big5.txt'
try:
    with open(file_path, 'rb') as f:
        content = f.read()
        print(f"Bytes: {content}")
        try:
            content.decode('utf-8')
            print("Decoded as UTF-8: Success")
        except UnicodeDecodeError:
            print("Decoded as UTF-8: Fail")
except Exception as e:
    print(f"Error: {e}")
