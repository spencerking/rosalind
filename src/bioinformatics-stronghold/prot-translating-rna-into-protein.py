codonTable = {"UUU": "F",
              "UUC": "F",
              "UUA": "L",
              "UUG": "L",
              "UCU": "S",
              "UCC": "S",
              "UCA": "S",
              "UCG": "S",
              "UAU": "Y",
              "UAC": "Y",
              "UAA": "Stop",
              "UAG": "Stop",
              "UGU": "C",
              "UGC": "C",
              "UGA": "Stop",
              "UGG": "W",
              "CUU": "L",
              "CUC": "L",
              "CUA": "L",
              "CUG": "L",
              "CCU": "P",
              "CCC": "P",
              "CCA": "P",
              "CCG": "P",
              "CAU": "H",
              "CAC": "H",
              "CAA": "Q",
              "CAG": "Q",
              "CGU": "R",
              "CGC": "R",
              "CGA": "R",
              "CGG": "R",
              "AUU": "I",
              "AUC": "I",
              "AUA": "I",
              "AUG": "M",
              "ACU": "T",
              "ACC": "T",
              "ACA": "T",
              "ACG": "T",
              "AAU": "N",
              "AAC": "N",
              "AAA": "K",
              "AAG": "K",
              "AGU": "S",
              "AGC": "S",
              "AGA": "R",
              "AGG": "R",
              "GUU": "V",
              "GUC": "V",
              "GUA": "V",
              "GUG": "V",
              "GCU": "A",
              "GCC": "A",
              "GCA": "A",
              "GCG": "A",
              "GAU": "D",
              "GAC": "D",
              "GAA": "E",
              "GAG": "E",
              "GGU": "G",
              "GGC": "G",
              "GGA": "G",
              "GGG": "G",
              }

def translate(s):
    result = ""
    i = 3
    while i <= len(s):
        if codonTable[s[i-3:i]] != "Stop":
            result += codonTable[s[i-3:i]]
        else:
            break
        i += 3
    return result

print(translate("AUGCAGGCAACUAUCAGAUCUAAUAUCAACGGUUCCGUACGAUUAUUGGUGAACUUCCGCCUUUGCGCUGCCCUAGGGUUGUCAACGUUGCAUGCCAGUGGUGCAACAGUUAGUAUCACUCUGGGGAAAAUCAGUCGGGUUGGUCAGACAUCGGUGAGCGUAUCAUGGAAAAGCUUCCCACAUGCGUGGUGGCUGAGGAUCUCUCUAACGAAGAUGCGUCUACCAGCGCUUGCAGCGAUCGUCGCGGCACCUAGAGCUUACUGGAUCUUACGGUUCUCGCAUGCGCGCCCGGUUAGACGUGUGCAAAGGACGCCGUACUACCAAUGCUUGGCGUUUAGUACAUGGCAAAUCUUAGUACAGUGGUCUGAGUGGCAUGCUAGAGCCGUAAUGUCUGGGGUGCUGACGACUCUACCCACAGACAUGCGAGGCGGGAUAUCGAUCGAGACAAGGGCGGUACUCUGCACACGCACGGACGGGCCUAUCCCAGGGACCCCAUUUGUGUCGGGAACGACUUCGGGAAAACGAGCUCGUACUCUACUGUCCCUUAUCGUGCUAGGGUCCCAACGUGACAGAACCACAGUCCUACAGGGAUACUGGGUUCACCUACGCACCGCUCAGUUAGCUUCCGAACUGGCUACCCCAACAUACGCAGGUGUUGGCCCACAUGGCAAGAAGACUUCUUUACUAACUUUGUUAGGCUCAUCAGCGCGCACCGAGGGAACCUGGCCCGCCUCCUUAAACCUUAUGUGUGAGCGAAUCAUCUUUGUGAGUUUGUAUGAACACGUUGGGUGGUACGAGGGAAUUGCACAACACGCGAUAGGUGUAGCGUCACUGGAUGACAACGCGUCGCGCGCGACGAUUUUCGGAGAUAGUCUCAAGAGUUAUGGGUUUUGUCCCCGGUGUCAACCAAAAUGCCAACCUUGCGCCCAUCUUCGAGGAACUGCGUGCGAAAGAGAUUUUUCGUGUCGCCGAAUUGUUUUCCAGAGUCGUCACAGCCGCAGCGGCACCUCCAAUCGUCGGUCGUACCCUGAGAAGCUCUUGAAACACCUGGAAUGGCGUAAUAGAAUUAGCUGGACAAGAGAUCUUACAAGGUCGAAUUGUUCGCGUCAACUUAUCACCCCUCCUGAGACACACCAAGGCGUAAACGCCGUGCUCAGUCCUUACGCUGAAAUAUCUAACUGCCCUAUACCUGUCCGCGAUGCUCUCGAACUCCUAAGCCAUAUCCUCAACGUCAAGAUGUCAGUAACAUCAGCGUUUAUUAUUUUGUACUUUUUAUGCAAGCUGCGGGCGAGCUUUAGGCUCACCCCAAUACCAAGUAGAGAGCCGCCCGGCGUUUACGUGGGGUUACCGGACAUGAAAACAGCUGUAGUCCCUCUGCUAACUGUUUCAGCAUGCGAGCGCGGUAUGCAUCAGGAGAGUGGGGGCAGAGACCAGGUGCCUGUUAAGCACUCAAACGGGAGACUCAACUGGAAUGGUUCUGAUGAAGUAUUUACGCAACGCACUAACGCUCAAGCAUGGCUUGAGACGCUCAUCUCGUUGCGACCUACUCGGCAUAUCAUUACUAAACCGGGACACCGCAAUGGAUCCGACGCUCCUGACCUUAGUCAGAUGUUAAGAGGUUUUCGAACCAACCGUUCAAAUGGCACCUCAGUUCGUGGACCCCCUGCGCUAUCGUCCGUUCUUUAUUCAGCUCAGAGUAAUUCAUCAUUAGCGGGUAAACAUGCGGAUGUCUUAAAGGGACUGAUGGUUAUGUACAAGAUACUACAGUCACCGACGCUAGAAGGGUUUUCAGCAUCGGGAAUGAUUUCACUCCAAUCGCUCGCGUCCAACUACGUCUUCCUCACGACUGUGGGUCUGGACGGCCCAGCAGUUGACGGAGCAUUACGUCCACCGUCUACAUCAAUUGCUAGUUUCAUAAAACAAGCUAUGACCGGAGGCCGAGACACGACUUUCGCUCGGGUGUUGUGUUACCUGGUAAUUCAACCGGACGGGGCCCCCGCCUUGCGAGUGAGCCACUGUUUUAACUCAUUGGCCGCAGGUAAACUAGUCCAACGCAUUGGGAAGAAUUCUAACUCUCCGGCCAGCCCAUACGACAGGAUUCGUCGACUCGGUUGCAAAAUACUGCUCAGCCGCCAUGCACAUUCAUACAAAGUAGAAAACCGUUCAUUAUGCGACCGUUUCAGCAACUGUACACGCUACCCGUUGCUGAUAUGGACUGGGAGUAGGGAGGUAGUAAUGGCACAGCGAGGUCAGGUGACUACCGUCACAAGCCGUGAAAAGCGGCGCAGGGUUUCCGUGCGCUCGCACAGUAACUGUUCUCAAAAUCCAGCGACACAGGCGCGAUCUCUGCGCCCUUUACACCAGAAGCAUGCUCGACCGGCCCGUGCAAGCGUACGGGUAAAGAGAGGAGAUCGUGGAAACUUCGGGCCACGCGUGUGUGCGGGAUAUCGUGACAUUUGUCUUAUCCGCCGGAACCCGGAUUGUGUAAUCAUGGACGACUUUGGGAGGAAAAUUGAUUCAACGCCGAACAGACUUGCCUUUGUGCCCCCUGAGGUGACGGGUCCCAAGCGAUGUUGCAAACAGGCCGGAAUUACGUUGCGCCCAUACUAUAAACUGCUCUCUGGAGUUACUUUUCGGGUUUAUGCCACCAGGGGAAGAAUUUUAGCGGAUACGGUUGGAUCGCGGCGAUCCUAUGGUUUGUGUAAAGUGCCUGCCACGAACCGCGUGCCUUCGAAUUAUACGAGCAAAAAAGGUGUGGGAGGCUGGUCACUCAUACCAAAACGAGACGUAAUAUUACAGCGAGUAAGCGGGCGCGACGGUCAGUUGGUGUUCACCAGUUCAGUGAAAGCGGACUUCACUGGGAACCACGUUGACGGCCAAGGGAGACUGUAUGAGGUUUCUCCCGAUACCUUAAGUAGCAUACCUCCCAAAUGUGCCAGCAUUAAGUCCUAUCACAACAAUAUAGGAAGGCUGUUGAAAGGGGCCACGUGGGCACCCAGGUAUUUCGGGAUCAAAAAACCACCUGCUGUCGUUGAUUACUAUCAACUAGGUCUUAUUAGUAGAAUAUGGGUAAGACGACCCCGGUCUAUCUCGUCUCAAAAUAAUAUAAGCCAGCAUAACACUCUCUGUUAUGUACUGACCUACGAUAUCAUCACCGAUCCCCGUCAAGAUCGUAGAGUAAUCGCCUGGCCUCAACAGUUCUAUAAUGCUUUUGCACACCGGGAGAAUGCUUUUCUCCUGCGACCUCUUUUUUCGUCGUGUUUCCUGCGUCUGGGAACUGUGUUCUUAAGUCGUAACGACACAAUACCGUACCGCGCGGGGGUGGGCUUACUGUUGGCUCUGGACUCGAUCGAGCCCUGUGCUAGAAUGGCGCCCGGUCCGCGUCGUUCAAGGAACUACAAUCCAACAUGGAUCGGGGCUGGGUGUCAAGGUCGAUGCCUAGUGCCCGACAGAUUUGAGGGUGAUCGUCGCUUAUUGAGCAUGACUGCUCGCUCUCUUUUUUCAGUAUCCGUCAGAAUGCCAUAUGACGCGCCAAUGAACCUCAGUGGGAAACAUACUCGUCCUCCUGAUUUCACUGGCGCUAGGUUUAAAAGCUUUGGUGCUUUCGGCCUGACAGCGUCCACAGUCAGGGCUUGUUUUGGUAGGAACUUCACAGUGACGCUCAGCACCCCGGCCCCUCACGACUUACUGGGGAACGUCUUGCUACUGAACAGCUGUAGGACAUGGAAUACCAGCGGGGAUGCAAAUCUGCUGAGUAGCACCCCACCUGACCGAUUCCCCCGCAAUGAGAUAGAUCUUUGCGUUGACGCAAGAAUCUCUAUAGAACUCCGCGCCGCCCUUCUUCCAGUACUACUUCGUUCCUGUAAUUUCGGGUCUUUGGUGACCACGGGUAAUAGAUCCUCACUCGUAGGUCCCACAAUCGCCAUAUUGAGUACAGUUAUACUUGAGGGCAUACGAUGGAGGCGUCUUAACACGAGUCACCUGUACGGAUGCGACGUUCGGUUUGACGAGUGUUUCUUUGCGCGGGUCAACGUCGAGCCUGUUCAAGAAUUCCUAACCGGCUCUAAUGAGGCGAAAGACCGAGUCUUGACUACCCCUUGCCACCCGAGAACCACCCGUAGAACUCACCAUGCUCAUCGAUCGCCCGAGAUCGGACUCUUGACCCCACUUCGCUGUACAUGUACCAACUAUGCUCGGGAAGGUGUGCUAAAAAACACAGAAGGACGAACAGUGGGCAGUCUGGUACCAUGUAUGCUGGGGAGUAGCGUUUGUCACACAUUAAGUCGCCCAGCACGCAGGAACGGUUUCACACUUCCGGUAGGCAAUUACCCGUCGUCAACUGAAGGCGUUUUGACUCCCGCACAGCAGUUCCCUCUCAAAGGCGCGCCAAUCAUCCAAACAUGCUACUGGUGGCAUCACCAGUCCGUCCUGCGGAAUCGCGGGCGCCUGCGUCCCGAGUGGAGCCUGGAGCCCCCCGCGCGACCGGGCAUCACACAUUUGACGCCAGCCUGGUGGGCGAAAGUUCGGGAGGUAUCAAGCCCCCAAGCUCCCUUAGUUCCACGGAGUAUCGACUUCCCGUCUGGUGUGAGGGAACUUGUAUCUACAUUGUUCCAUACUCGAGCCAUAACCAAGGGUAGACCGAGGCGACACAAUCUCAUUCGUUGUGCCAACAAGUCGAAGGCGCUUGCUGGACUUUGUAAUACGCUGUGUGAUAACCCGACAAACUCCCGAGGGUUGACAUGCGCUUGGCAUGACAGCGCAUUUACAGAUAACGAACAUGGACGCCGACCUGGUCAGCCGCUCAUGCACUGCGCAAGUAUUUCGUUCUCUAGUCCCAUUAAAUGCUCUCACUUUGGUGGAACCGAUGUUUCCACAAUGAUUGCUCAAAUGAGCGUAAGGCUCGUAUGUCCGGCUUUUGUCGUUCGCCUCCUGCUGCCAGCGGGGUUGCUCUGUGAUCUGGUCCUAUUUUUCCAGAGUAUUCUCAAAGGCUGCGUGUAUUUGCAGAGAGUAUGGAGACCGCAUCAGGACCUGAACCACAUGAUACAUGAAUCGAUCUGUCACGAAGUGUUGUACCAUCGUGAUAACUUGGAUUGUAAGAAUCGCUUCAAUGCGGAAGCCUUGUGUUCCUUAAAGAAUUUGCGGGGGAUCAUUACGAUUGCGCCACGUGUGUGUGAGAAACUAAUUUACAUGGAGAAAUGCCCCCGUCGAUUAGAGACCUGCAAUGGCUAUAAGGUUCCCACACUACCAACGCCAAAUUCCUUAGAACGAAUAACGGCUACUAUAAUAAUCCGAGCUAGCGGACCAGCUGCUCAUCAUAGCCGUCAAUUGAUUAUGACCGGCAUGUUGACCGAGUUUCCGGGCGCGUCCAAUGCCUCAUUCAUAGGCAAGAGAAGCCAGACACGCUAUAUGACCAAUGUACACAGCUCUGUGAAGAGGUUGAACCUAGGCCACGGUACCGCAGGUAGUGGUCCUGCAACAUACAACUGGCGGUCUCGCACCUGUUCGCGUGGGGCGAGCCUCGUUCGUUCAAGAUACUCGAGUAUUAUGUACAAUUCUUUACUAGGUAACUCGAUACCUUGGCUGUCGUUCGCUACUGCGGAGCUAACUAGUUUACCGCUCGGCCGAUCUAAUUGCCCAGGCAUUGUCGUUCACUAUGAAUUAGUGUCAGUUGAUAUGCCCCUAAAAUAUGUGCGUGUCGUGGGGCUUACCUCUACCGUGAAGUCCCAGAGUGUAGGACUCGAAAAAGCCAUACUUUUUAUAAGAUGUAAGGUCGAUACGAAUUACGGGACACGAUGGUAUCAGGGCCGGCGUGGUAAGGGUCGCAAUCACGACGCGGCCAGCGAAUGUCUAAUAAGAUGGGUGCCAGAACUCGAAUGUGACUGUUCCAAUGGGGCGCUGACCUUGAGUUGUAAGGAGAGAGGCAAUGAAUCAAAUGUAGGUUUGGAUAAUUCUUCCAACGUGGAGGCGCCAACAUCGUGCGGUACCACAAUUUCCGGACGGAGACCCGUUACGCAAUGUCACCAAUUCCUCGGGUCCACCCCAUUCUCGAUCAGAGGGUGCGACGUUGUCGUCGGUAGUUCACGGCCUGCGACGUUUGACGCGGUGAGCGUUCUGGCCUCUUUCAUCAGUUCAAAAAGAAGAUAUAGCGCCAUACCUAUGAGGAAGUCUAAAUUCAGCGUAAUUUACAUACUGGGUUGUGCAUUCCCUGGGGUUCUAGGGUACCAGCCCGGCAAUCUGUCCGAUUCAGGUUACAGGAAAACUCGCACAUAUGGCAGCGAGCCAAGUAAGAUACGAAUAAAUUUAUCUUGUUCACGACUAUACGUCAUAUUGUGUGAUUCUUACCGAAAUCAUCCCACUCGUUGUGGACUGCCGGAUGGUACGCUACGCCAACGUUAUGCUUCGAGGCUCCAUCGAGUUCAUGCGUCGUUGAGUCCGUAUGUGAAAUGGCACUUGAUCAUGAUAAACCGUAUAAGGCCCACCCGUAAAAUGCGACUUACUGUUCAUAGUCCCGGCGCAAGACCGCGACUCUGGUCAUCUUGUGGACGGGCGUGCAGCCAGCGUCUUUGCAUCCCCCCUCGCGUAUAUAUCCAACGAGCGCAUAAGAUUAACGGCUCUGCUCGGGCUAAUUUAGAAGCAGAUCGACUUUCUCACCUAUCUACAUGCGUACUGCCGUUGUGGAUCACAGGGCACUACGCCAGGUUAACCUUCGAUUGUAUAGGCCGCGCCAACGAUUCUGACAUGCACAGUUCGUGCGGAAGACGCCGGGCUCCCCACACUCUCGUGUUAUGCGUCGCGCGUCAUAAAGGCGUCCUGAUUUCUGCUCCCUAUUCAGCAUUCCUUAACUCUCUGUCCCGAGUGCAGAUCCCAUCCUUCCUUCCCCGUAGAAGAUUGGUUCCGUCUCGAAAUGGCUCACGUACACCCUCAUGGCGCACGGGUGCUUACCCCCUUUGGUAUUAUCCAUUUACUCGGAGGACACAAUAUCGAAUUGCUCCCUCGCUUGAAUCUACCGUGUAUAUUGUGGGCCCGUUAUGCCCUCUCUCGUUGUGCAACCCCAUCGCCGACUUUAGGGACUUUCACGCAUGCUAUAGUCUGGACGACUUGCUCUAUAAGGCGCAUAUGUCUACGGUUGCAGAUGCCCUUCAGAUUACAGGGCGUAGUGAACUGAAGAUCAAUGCGCCGGUUAACAAAUAUGUAGGAGCCAUAGGUAUUGACCAGAGUGAUAAUGACUCGAACUAUUCGUCUAGUUUGUUAGAUGAACAUCCAUACAGAUCUCUCGCGCUUUUGGCCCUUAAGGUCCGUCAGUUGCAGUACGCAAGAUGUAGCUGUCGAGUCGUACGUGAACCGACGCGUGGCCAGAAACUUCUUUGGGAGGUAUCGAGCAUUAGUCGGGUGGCCCGUUUUCAUGAUCGGGUCCAGGUUCCCUAUCGGACGAGCGUGUCUAUGGUCUGUGGAUCCCGGCUGUCUACGGGCCUGGACCCCCCUGUACAACUAUCCCACUUGGCACGCCCACUCAGAUGGAUGUCACGGCCAUGGAAGGUUCUGCGAUGUGGGGGACCAUCAAUGAAUUCGCACCGACCCGUCAUUAGGGACCAUCAUCUAGUUUCGUCCGAAGGUGACCGCGUGUGUCGCGAACCCAAGCAUAUGACCUACAACUCUGACAGGACACUGAGAAAUUCAUGGUAUCCAAUUGUGAUGAUGGAUGAUUCUGUGCCGCAAGUCGUUUAUCACUGCCCGAAGCAGAGCCGAGGCCCUUCCCCGAUAUGGUUUACGUUAACAGUGGCAGCACGUGAUGAUCCGGAAGAGAGUAAUGGGGGUCACGCACCUCCGGUCUGGCAGAAGAUCAGUCGACCGCUCGCUGCGAACACCCAAAUGAGGAUGGAUCAAGCCGAAGCGCAACGCUCGCACUCGUCAUUAUUUGCAUCCCAGGACCCUAAGUCCGGCCGAGCCCGGUCAACUAGCAGUUCUUCUUCCUGUACGGUAGUGAGCUAUAGAUCCCUACAUACGUCGGUGCUAUCCACGCUCGCACUCCGUGUGUGUGCCGUUCCUAGCGUCCCAGACCUGGCUCGAAAACGCAGCGGCGCUACUCUCAUGCUGUUUGAUAGAUUACCGGCGCGGAUUUGUGCCGUACUACAAUUUAUAACCUACCAGAAUUAUUGGGGGCGUAGUAAGACACUCACUGCUCACUACCAUCGAUCUGUUACAUCAAUCAGGACGCUGCUGCAUCCAUUUCUAGUUGGCGGGGAGAACCUUGAUAAUAACCGACCUUGGCCCGUUUGCCUGUUGAAGCGUGGUAAACUCAACUCGGUCUCUGUGCAACAGGGCAUGCGUUGGCUAACUACUCCGAUGGCUGCUGGUGAAGGGGCGGUCUGUUGCCCUCAUGAAUCUAUUCGAGGUGUUACGUUGCAAAAUUUGGAGAAUAUCGUACGCGCUGAGGGACCUCGGCUAUCGUGCGGGUUGACUGUUACUAGUGACUUAGGUUUUGCGCACAAAACUUCACAUCAAACGGAGUGGGGGAGCCUUCAUCUGACACUUGUUACCGCACCGUCCGACCGGUGUCUCGGGAACCUCGCUCGUUUAGCUACUCCACGAUCAUAUGCUGGCACUCGAAAUUUCUUGAUUGACCCUUGCAUUGUUAAACUGCAUCUUAUGGACGCUGCCCCCCUCUACAUUCCGAGCCCGGAUUCCUGGGUCUAUGGGUGUAGACGCAGUGGACCCUCUCAUAGAAAUCGUCGGAAUAAUGACAAGUGUCGAUUAUUCUAUUCUGUCACGUUGAAGAAUCCUCCAAAGAAACCCAACCUUGCACAUCGCCGCGGCUACAUGCUACGUACAAUUUUGUCCGGUCGUAUGAUUAUACGUAUAACCGUUCCUAUCCCAGUUUGCUUUGGAUGCAUGUAUAGUUGUAUCACGAAAUUAGCCCGAGAUAUGAUGAGGGCGCUAGCGGAAUUGCCCAUGCCCAAUCGAACAACAAGCGUGGAGGAUCAGGGUUCCUACAUUGAGAUCAGAUGGGUGCCUGAUUUAUCUGCCUCUAAAGGUGUAACUCACGUGACGUGCUCAUUGUGGUCUGGGUCCAGCACGUACGUUCGCGCGAUCGUAUCAUCUGGCUUCACAAACCGCAUCCCGGGCCUACAAUACAGAUGCGUGAUUUGUAGGGAUAGAUACACACCUGGUCCAACGAAUCUAACUCGGCCUGUGGGUUUCCCACCUAUUCCUGCGUUCUUUCAUCUGCUAUCUUUGUGGAGUGCCAGCUCUUGCUUAUGGGCAAAUCGCCAUUUUCCAGUCCAUGACGUUUCAAGCGAUUACCCCUGUCCAGCGGAAGUCCACUGCUCGCGUAUUCGCAUCGGAUGA"))