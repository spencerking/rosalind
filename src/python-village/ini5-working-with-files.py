def main(file):
    f = open(file, "r")
    output = open("outfile.txt", "a")
    i = 1
    for line in f:
        if i % 2 == 0:
            output.write(line)
        i += 1

    f.close()
    output.close()
            
main("rosalind_ini5.txt")
