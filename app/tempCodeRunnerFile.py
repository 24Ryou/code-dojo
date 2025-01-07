def DNA_strand(dna):
    # code here
    s = str.maketrans('ATCG', 'TAGC')
    return dna.translate(s)