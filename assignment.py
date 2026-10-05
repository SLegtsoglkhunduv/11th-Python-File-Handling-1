# You can remove 'pass' if you written code in the function
# Exercise 1
def write_shopping_list(items, filename):
    file = open(filename, "w")
    c = 1
    for i in items:
        file.write(f"{c}. {i}\n")
        c = c + 1
    file.close()

# Exercise 2
def read_names(filename):
    file = open(filename, "r")
    lst = []
    lines = file.readlines()
    for line in lines:
        cleaned_line = line.strip()
        if cleaned_line != "":
            lst.append(cleaned_line)
    file.close()
    return lst

# Exercise 3
def append_entry(filename, text):
    file = open(filename, "a")
    file.write(text + "\n")
    file.close()
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    return len(lines)
# Exercise 4
def search_file(filename, word):
    # Write your code here
    pass

# Exercise 5
def number_the_lines(source, destination):
    # Write your code here
    pass
