# Author: Caleb A. Moura

# alma-mater.txt file opened.
file_path = "alma-mater.txt"

# Content of file read using reading files all at once method.
with open(file_path, "r") as my_file:
    contents = my_file.readlines()

# Lines to the console printed in reverse order, with a blank line between each.
for line in reversed(contents):
    print(line.strip())
    print()  