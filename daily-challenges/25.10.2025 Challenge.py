# start of main.py

def complementary_dna(strand):
    complement = ''
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

    for char in strand:
        complement += complements[char]

    return complement

def complementary_dna_2(strand):
    return strand.translate(str.maketrans('ATCG', 'TAGC'))

# end of main.py

