def read_file(file_name):
    # Reads in a file.
    f = open(file_name, "r")
    return f.read()

def read_file_into_list(file_name):
    # Reads in a file and stores each line as an element in a list
    with open(file_name, mode="r") as file:
        return file.readlines()
    
def write_first_line_to_file(file_contents, output_filename):
    # Writes the first line of a string to a file.
    str_list = file_contents.split("\n")
    file2 = open(output_filename, "w")
    file2.write(str_list[0])
    return

def read_even_numbered_lines(file_name):
    # Reads in the even numbered lines of a file
    with open(file_name, 'r') as f:
        return list(f)[1::2]

def read_file_in_reverse(file_name):
    # Reads a file and returns a list of the lines in reverse order
    line_list = []
    with open(file_name, 'r') as f:
        for line in f:
            line_list.append(line)
    return line_list[::-1]

def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))

if __name__ == "__main__":
    main()