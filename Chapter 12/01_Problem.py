# Write a program to open 3 files 1.txt, 2.txt, 3.txt.
# if any of these files are not present a message without exiting the program
# should be printed on the console



def OpenFile(fileName: str):
    try:
        with open(fileName) as f:
            data = f.readlines()
            print(data)
    except Exception as e:
        print(f"File {fileName} does not exists")


OpenFile("file1.txt")
OpenFile("file2.txt")
OpenFile("file3.txt")