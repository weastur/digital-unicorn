from contextlib import contextmanager

@contextmanager
def mfw(first, second):
    f1 = open(first[0], first[1])
    f2 = open(second[0], second[1])
    yield f1, f2
    f1.close()
    f2.close()

with mfw(('input.txt', 'r'), ('output.txt', 'w')) as (infile, outfile):
    outfile.write(str(len(infile.readlines())))
