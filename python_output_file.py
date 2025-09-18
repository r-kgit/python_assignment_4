try:
    file1 = open("output.txt", 'a')
    yes = input("do you want to enter data in file type y for yes ")
    while yes == "y":
        user_input = input("enter some data into file ")
        file1.write("\n"+ user_input)
        yes = input("do you want to enter data in file type y for yes ")
    file1.close()
except FileNotFoundError:
    print("Error : file does not exist")

try:
    file1 = open("output.txt", 'r')
    data = file1.readline()
    while data:
        print(data.strip()) #remove \n from line
        data = file1.readline()

    file1.close()
except FileNotFoundError:
    print("Error : file does not exist")