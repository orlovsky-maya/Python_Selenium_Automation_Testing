file_write = open('txt_files/file1', 'w')
file_write.write('Privet python\n')
file_write.close()

file_read = open('txt_files/file1', 'r')
text = file_read.read()
print(text)
file_read.close()

file_add = open('txt_files/file1', 'a')
file_add.write('Python is better language')
file_add.close()