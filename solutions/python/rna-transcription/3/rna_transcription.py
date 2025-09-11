def to_rna(dna_strand):

    compliments = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}

    rna_strand = ''

    for nucleotide in dna_strand:
        if nucleotide not in compliments:
            raise ValueError(f"unknown: {nucleotide}")
        rna_strand += compliments[nucleotide]

    return rna_strand
