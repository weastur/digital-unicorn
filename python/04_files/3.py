with open("03_in.txt", "r") as in_file:
    with open("03_out.txt", "w") as out_file:
        for line in in_file:
            out_file.write(
                ' '.join(reversed(line.split())) + '\n'
            )