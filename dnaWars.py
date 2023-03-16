Codon_Dict = {'T' : {'T' : {'T' : "Phenylalanine", 'C' : "Phenylalanine", 'A' : "Leucine", 'G' : "Leucine"},
                     'C' : {'T' : "Serine", 'C' : "Serine", 'A' : "Serine", 'G' : "Serine"}, 
                     'A' : {'T' : "Tyrosine", 'C' : "Tyrosine", 'A' : "Stop (Ochre)", 'G' : "Stop (Amber)"}, 
                     'G' : {'T' : "Cysteine", 'C' : "Cysteine", 'A' : "Stop (Opal)", 'G' : "Tryptophan"}}, 
                'C' : {'T' : {'T' : "Leucine", 'C' : "Leucine", 'A' : "Leucine", 'G' : "Leucine"}, 
                       'C' : {'T' : "Proline", 'C' : "Proline", 'A' : "Proline", 'G' : "Proline"}, 
                       'A' : {'T' : "Histidine", 'C' : "Histidine", 'A' : "Glutamine", 'G' : "Glutamine"}, 
                       'G' : {'T' : "Arginine", 'C' : "Arginine", 'A' : "Arginine", 'G' : "Arginine"}}, 
                'A' : {'T' : { 'T' : "Isoleucine", 'C' : "Isoleucine", 'A' : "Isoleucine", 'G' : "Methionine"}, 
                       'C' : {'T' : "Threonine", 'C' : "Threonine", 'A' : "Threonine", 'G' : "Threonine"}, 
                       'A' : {'T' : "Asparagine", 'C' : "Asparagine", 'A' : "Lysine", 'G' : "Lysine"}, 
                       'G' : {'T' : "Serine", 'C' : "Serine", 'A' : "Arginine", 'G' : "Arginine"}}, 
                'G' : {'T' : { 'T' : "Valine", 'C' : "Valine", 'A' : "Valine", 'G' : "Valine"}, 
                       'C' : {'T' : "Alanine", 'C' : "Alanine", 'A' : "Alanine", 'G' : "Alanine"}, 
                       'A' : {'T' : "Aspartic acid", 'C' : "Aspartic acid", 'A' : "Glutamic acid", 'G' : "Glutamic acid"}, 
                       'G' : {'T' : "Glycine", 'C' : "Glycine", 'A' : "Glycine", 'G' : "Glycine"}}}

sequence = "CGATTGCGTATAAGCACCAA"

def codonSequenceReader(seq):
    codonLength = 3
    currentCodon = ""
    codonList = []
    for i in range(len(seq)):
        currentCodon += seq[i]
        if len(currentCodon) == codonLength or i == len(seq)-1:
            codonList.append(currentCodon)
            currentCodon = ""

    dict = {}
    for i in codonList:
        if len(i) == 3:
            dict["{}".format(i)] = Codon_Dict[i[0]][i[1]][i[2]]
        elif len(i) == 2:
            dict["{}".format(i)] = Codon_Dict[i[0]][i[1]]
        else:
            dict["{}".format(i)] = Codon_Dict[i[0]]

    return dict
        
print(codonSequenceReader(sequence))
