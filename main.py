print("Hello World") # Prints "Hello World"

# I want to read a txt file
def readtxt():
    with open("test.txt", "r") as f:
        print(f.read())

# call the function readtxt
readtxt()
# After reading the txt file, I want to write to it
def writetxt():
    with open("test.txt", "w") as f:
        f.write("Hello World")
# call the function writetxt
writetxt()

sdasd