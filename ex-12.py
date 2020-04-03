import sys

for x in range(1, 11):
    sys.stdout.write("[\t")
    for y in range(1, 11):
        sys.stdout.write(str(x*y)+'\t')
    sys.stdout.write("]\n")
