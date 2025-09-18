# read the file and exception handling
'''
file1=open("sample.txt",'r')
data=file1.read()
print(data)
file1.close()'''
print("\nThis is using readline\n")
try:
    file1 = open("sample.txt", 'r')
    data = file1.readline()
    while data:
        print(data.strip()) #remove \n from line
        data = file1.readline()

    file1.close()
except FileNotFoundError:
    print("Error : file does not exist")

print("\nThis is using readlines\n")
try:
    file1 = open("sample.txt", 'r')
    data = file1.readlines()
   # print(data)   # use to print as a list
    for i in data:
        print(i.strip()) #remove \n from line


    file1.close()
except FileNotFoundError:
    print("Error : file does not exist")