def countNucleotides(s):
    result = {"A": 0, "C": 0, "G": 0, "T": 0}

    for base in s:
        result[base] += 1
    
    return result

counts = countNucleotides("CTTGAACATTTGTTAGACCACAGTTAGATGCGATTAATTTATAACGCCGACGGATTATTTTTTACAACCATTTCTACGTCTTCACATACACCGGCGGCGCGTCTATCTTGCTTCTTGTCCCATCCATGCTAATACCAAGTGGACCGAGGCCCCGTTTCCCAAGTGCCGAAAAACAATGGCGTCGTTGGAAAAGATTTCATAAGAGCGCAAAACGGCTCCCGTATATCTAGGGCTCGGGCTGGGCCTATAAGTTGATCAGTAAAGCGCTTTCAGTTAAGTTGCAAAGTTACTTCCGACCGCCGCGCCATTAAAGTACAAAACAACCTACAAAACGCCTTACTTATTAGAGTACATACAGCACTAATCCCACTAAAAAACGATAAGTTAATATTGTTCACGTAAGAAACCAGTTGTAAGACGGTATGTCACGATCCTGCCTCTATAGAACTTCTATGTCGGCGTGACAAAAACTTTTTTACCTGTATTTCGTCTGGTTGCCGTCGTGCCGCGTACGCGAGTTCTTTCTGATTTCACGACACTGGACCTCCAAAGAAAAGCAGCACAAGGACTCGTACCTCAAGGGCTTCTATTCCAACTGATGCGGGCGTCTATCTCGGATCGATCCACCGAACGAAACCTTAGCTTACTCGACTATCCGGTGCTCCGATCGGATATCATATGTACCATCTCGCAATATATGTAATGGACGATAAGGAAATGGTCGTGGCCCCGTCTGGTCTTCAACAAACGCAAAACTCCCTGCAATCAGTAGTATGGTATCCCTGAGAACACTTGTATTACATGGTCCCGGTTCTCTCCCGAGAAATTGTTGTTAGAACTGGAGCTACCCTGATGGCAGACATGCGTGGCTGTTCTTTAG")
print(str(counts["A"]) + " " + str(counts["C"]) + " " + str(counts["G"]) + " " + str(counts["T"]))