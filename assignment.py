# You can remove 'pass' if you written code in the function
# Exercise 1
def write_shopping_list(items, filename):
file = open(filename, "w")
c=1
    for i in items:
        file.write(f"{c}. {i}\n")
        c=c+1
    file.close
items = ["Bread", "Milk", "Eggs"]
filename = "shopping.txt"

# Exercise 2
def read_names(filename):
    file -= open(filename, "r")
    lst = []
    lines = file.readline()
    for line in lines:
        if  line.strip()!="":
            lst.append(line.strip())
    file.close()
    return lst
print(read_names("text.txt"))

# Exercise 3
def append_entry(filename, text):
    # Write your code here
    pass

# Exercise 4
def search_file(filename, word):
    # Write your code here
    pass

# Exercise 5
def number_the_lines(source, destination):
    # Write your code here
    pass
