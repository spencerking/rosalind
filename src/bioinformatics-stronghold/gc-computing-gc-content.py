def gcContent(file):
    f = open(file, "r")
    samples = {}
    currSample = ""
    currCG = 0
    currCount = 0
    
    for line in f:
        line = line.strip()
        if line[0] == ">":
            if currSample != "":
                samples[currSample] = currCG/currCount
                currCG = 0
                currCount = 0

            currSample = line[1::]
            samples[currSample] = 0 # assumes samples are unique
        else:
            for base in line:
                if base == "C" or base == "G":
                    currCG += 1
                currCount += 1

    print(currSample)
    print(currCG)
    print(currCount)
    samples[currSample] = currCG/currCount

    return samples

result = gcContent("./gc-computing-gc-content-sample-input.txt")
print(result)
