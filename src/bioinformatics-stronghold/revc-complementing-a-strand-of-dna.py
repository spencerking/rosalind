def reverseComplement(s):
    result = ""
    for base in s[::-1]:
        if base == "A":
            result += "T"
        elif base == "T":
            result += "A"
        elif base == "C":
            result += "G"
        elif base == "G":
            result += "C"

    return result

print(reverseComplement("AGGATAGCCGTCTGTCTTTCTCACTTGAGTACTGATGAAAAGGCAAGTGAGAAGGACAGGATTATCCTGAACCGCCTAGCTTCGTTTTGAGCCGGCATATCGCCTGCCTGATGTCGTGTTTACTTACGCGCCCGCAAAGTTTCCAGGAAAAGCCATCGGTTTTAATGGAGATCGTCCGTGTCGGCGTATGCAGCATACTCCTAGTGAGTGGTCGGCCGCGGTATGGCTGATACCTAGCACCCGCTACGGCCTGAGAGCTCAGACAACTGAGGCAATATTATAAAACTCATAAAAGTGCCTCTTTGTCTCCGAGCGGAGTGTTCCGCATTTCGCATTCCAGTATGGGCTGCACCCGGGCAACTGGGGCGCGGCCGATCTTTCGAATAGCATATGGGTGAGTATGGTGGAATTTCTGGAGACTCACACCTGCATTAGAAGACAAAGTGAAACTGATTCATCAGCTGTACCCGTACCAAAGGCGTAAGCTGCCTGCTCCTGTCCGGGGAGTGGAGTCTGATGGGATTAGTTACTATGATTGAGTGCGACCACCCCCAAGCAACGCGCTCTAGACTAGATTACCGAGTCCAACGACTTGCCCTCTGTACTCGTAGGTGCCTCCCTTCGCACAGACGTGGCGCTCTTTTGTCCAACTTTGTGTTAAGTAAGCGTTTTTACGTACTATATACGCACGCAAACGCGGCTCTGTTTATGTATCGGGGTCATTGGCTCCCACAAAAACGTCTTACATTACTTGGCCAGGTAATTGGAGAATCGATTACAAGCGCCTAGTAACGACAAGATCTTGCCACGTCCCAAGCTCCCAACGTTACTGGGACTACCATGCGGTGGCTTGGGATGAAGTGAGATTCTCAGAAAGAGATAAGGGGTTTCTGGTTTGGCGCATAATGCTAACTTTGCCTCTATACAAGCGAATGCGTGGGATCAATTGTCACGTAATGTCTTACGGCACAGATGCATTCAATACTAAGA"))
