#open_file_r_and_rb.py

file = open(input("Input the filename:").strip(),"rb")
for line in file.readlines():
    print(line)
file.close()
