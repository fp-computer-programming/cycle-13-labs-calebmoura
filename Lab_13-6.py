# Author: Caleb A. Moura

# alma-mater.txt file opened.
file_path = "alma-mater.txt"

# File opened in read mode.
my_file = open(file_path, "r")

# File read line by line & print each line with a blank line between each.
while True:
    line = my_file.readline()
    if len(line) == 0:
        break
    print(line.strip())
    print()

# File closed.
my_file.close()