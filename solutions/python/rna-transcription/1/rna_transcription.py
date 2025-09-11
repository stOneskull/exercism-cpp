def to_rna(dna_strand):
   
    compliments = dict(
        G = 'C',
        C = 'G',
        T = 'A',
        A = 'U'
    )
        
    rna_strand = ''
    
    for nucleotide in dna_strand:
        if nucleotide not in 'GCTA':
            raise ValueError("unknown nucleotide: {}".format(nucleotide))
        rna_strand += compliments[nucleotide]

    return rna_strand