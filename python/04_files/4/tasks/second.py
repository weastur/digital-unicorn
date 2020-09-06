def solve():
    with open("02_in.txt", "r") as in_file:
        with open("02_out.txt", "w") as out_file:
            out_file.write(
                str(
                    len(in_file.readlines())
                )
            )
