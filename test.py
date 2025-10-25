def complementary_dna_2(strand):
    return strand.translate(str.maketrans('ATCG', 'TAGC'))