import itertools

def hamming(s, t):
    distance = 0
    for (base1, base2) in zip(s, t):
        if base1 != base2:
            distance += 1
            
    return distance

print(hamming("AACCTGTTGTGGCTGTCGTCCCCTTCGACCAGCATATACCCGGGCGTGATCTACCCGTTCTTAGCAGCCGCTGAAGGTAACTTGAGACAGGATGGTCACGTGAGACTGCATCACCGGTTCTGTCAGGCAGGTACACGCTGTTAATGTAATACTAGCTCTCGCTAGATATAATGAATGTTCATGGAGCGGGATAATCCGCCCGAACTTGGTCACGTCGAGCGGTGGTCCCACGGGCATCTTTCGACAACATGGGATAAGAACCATGACACTAAGATTCTGAAGCGCGCCAGAGTTGGTGAGGACACCGAGTGCGAGTAGGATTCCCGTTCCCTATTCCAGGGCTGCTTTTAGCAGGACCGGCCTTTGAGCGTGACGTTCTCCAGGTTCTCGGACCACCAACGGGAACGACCGAGACGGAATTCCGGGTAGTCTTAAGGACCAAATGACATTTTCCTGGAGTGGCAAACCCGATAAGAGCGTTGGGGTATATAGCGACCTGTTTTCGCCGGCCCTAACCGTACGCAACTACCGCCCCACGCGAGCTAGGGGGGACGATCTGACTTTGGCGACGGATTTAGCACGGTGTACTCCTCAATATTCCGAGATTGCCACGACATAGATACAGTTCAGGATAGTCCACAGCTCGCGTCCACAGGACTTTTCCTGGCAAAATTATAGGAACTGACATCCGTTTCAACAGAGCCAATTTCCAATGGACGACTGCGGTCCGCCACTTAGGAAGGGTGACATCCGTCGCGGCTTGCGCCAGTGACATGTTAAAGTAGCGGTACAGAAATCGCGGACTGCTTGGGTCAGGTCCGACGGGGGTACGTATACGCTGTAGTTGACGGAAGTGCGAAGGATGTATCAGCTATCGTCAGGCTCCTGCTGCGACTGTAGTACAAGTTTTCCTCTGACTTTATCCCCACAACTTTCAGCGAGAG", "ACTCTGCGCCGGGTCTATCCTCCTGCGATCACCTCAGTCCAGGGCGTAAAATACCGTTCGTGAGCGTATGATACCGTTAAACTGATCCAGGATGCTACCTGGCGCGCAGCCGACATGTCCTGTACGTCAGGGAGAAGCTCATGTGGTGATCGCGACTTTTCTCAAATTGAAAGAATCCTGCTTTTGCAGGAAGTTGCTCCCGTCGTCGGACAGGTCACTTGGTGACTTGACAGACAGCTTTCCTCCCCATTGCATCAAATAAAAGGAACTTAGAAACCCCAGCGCGGCGTTGCTGGTCGCGAGGCCCATGGCCAGTTGAATCCGGGGTTTTGGCGTAAGTGTACTTTCTAAATCCACCGTCCGTTGTGCGTGAAACTCGGCATACGCGCTAGCCACCTGCGCAAACCACATAGTCTGGACGCCGACTCGTAACAACGTCACACACCCCTGCTCCTGGTGTACGATCCCTAATCTGAACCCATGGGCATCTAGCGACCTTTGTCACTTGGGCCGAGTCTCACATATCCTACGCCCGACCCCCATCAGAGAGCGTCCCCTGAAGCCTGTGACATGTTGACATGGTTGGACTATGCGATAATCACCGTTTATCACCTGCTCGCAGTGTATCTCAGTTGTTCGCGGGTAAACATAACAGGAGTTGACTTGCCAATCTTTGACGACCAGGGATCCCTTTCAGTCGGCGCCGTATCCCTGTGATTGCAGCTAGTGTCCGGGGAAGACGCAGTACATACTTCGTAACAGGGCAGAGCCCGCTGTCCGGGGTATCATAGTGTACGAACGTACAGTTCTGGTCGGGGCAAGCCTCCTTACTGATTCTATCCGGTTGTCTTGGTAGCGTGTTATGGAAACTGGCCCTTTAGGCACCCGTGGCGACATTTGCCAGCGCGGTTCTATGACTGCAAGCGCTTAAGTTGCGTTCATAG"))
