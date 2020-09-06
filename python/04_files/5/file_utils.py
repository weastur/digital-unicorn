def count(file_name):
    with open(file_name, "r") as in_file:
        return len(in_file.readlines())