import os

os.makedirs('test_files', exist_ok=True)

# Create UTF-8 file
with open('test_files/utf8.txt', 'w', encoding='utf-8') as f:
    f.write('This is a UTF-8 file.\n中文测试')

# Create GBK file
with open('test_files/gbk.txt', 'w', encoding='gbk') as f:
    f.write('This is a GBK file.\n中文测试')

# Create Big5 file
with open('test_files/big5.txt', 'w', encoding='big5') as f:
    f.write('This is a Big5 file.\n中文測試')

print("Test files created in 'test_files' directory.")
