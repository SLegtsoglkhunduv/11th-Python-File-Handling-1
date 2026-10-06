# You can remove 'pass' if you written code in the function
# Exercise 1
def write_shopping_list(items, filename):
    with open(filename, "w") as file:
        for i, item in enumerate(items, start=1):
            file.write(f"{i}. {item}\n")


# Exercise 2
def read_names(filename):
    names = []
    with open(filename, "r") as file:
        for line in file:
            cleaned = line.strip()
            if cleaned:  # Skip blank lines
                names.append(cleaned)
    return names


# Exercise 3
def append_entry(filename, text):
    # Step 1: Open in append mode to add the new line
    with open(filename, "a") as file:
        file.write(f"{text}\n")

    # Step 2: Open in read mode to count total lines
    with open(filename, "r") as file:
        return len(file.readlines())


# Exercise 4
def search_file(filename, word):
    matches = []
    target = word.lower()
    with open(filename, "r") as file:
        for line_num, line in enumerate(file, start=1):
            if target in line.lower():
                matches.append(line_num)
    return matches


# Exercise 5
def number_the_lines(source, destination):
    # Read everything from source first
    with open(source, "r") as src_file:
        lines = src_file.readlines()

    # Write numbered lines to destination
    with open(destination, "w") as dest_file:
        for i, line in enumerate(lines, start=1):
            dest_file.write(f"{i}: {line.rstrip('\r\n')}\n")

    return len(lines)
