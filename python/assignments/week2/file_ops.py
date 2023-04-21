def read_file(file_name):
    """ Reads in a file.

    Args:
        file_name: the name of the file to be read

    Returns:
        string: contents of the given file.
    """
    ### WRITE SOLUTION HERE
    f = open(file_name, "r")
    return f.read()

def read_file_into_list(file_name):
    """ Reads in a file and stores each line as an element in a list

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list where each element is a line in the file.
    """
    ### WRITE SOLUTION HERE
    with open(file_name, mode="r") as file:
        return file.readlines()
    
def write_first_line_to_file(file_contents, output_filename):
    """ Writes the first line of a string to a file.

    We determine the first line to be everything in a string before the
    first newline ('\n') character.

    Args:
        file_contents: string to be split and written into output file
        output_filename: the name of the file to be written to
    """
    ### WRITE SOLUTION HERE
    str_list = file_contents.split("\n")
    file2 = open(output_filename, "w")
    file2.write(str_list[0])
    return

def read_even_numbered_lines(file_name):
    """ Reads in the even numbered lines of a file

    Args:
        file_name: the name of the file to be read

    Returns:
        list: a list of the even-numbered lines of the file
    """
    ### WRITE SOLUTION HERE
    with open(file_name, 'r') as f:
        return list(f)[1::2]

def read_file_in_reverse(file_name):
    """ Reads a file and returns a list of the lines in reverse order

    Args:
        file_name: the name of the file to be read

    Returns:
        list: list of the lines of the file in reverse order.
    """
    ### WRITE SOLUTION HERE

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