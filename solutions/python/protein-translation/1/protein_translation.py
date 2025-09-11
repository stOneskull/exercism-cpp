from textwrap import wrap

RNAdict = dict(
    Methionine = ['AUG'],
    Phenylalanine = ['UUU', 'UUC'],
    Leucine = ['UUA', 'UUG'],
    Serine = ['UCU', 'UCC', 'UCA', 'UCG'],
    Tyrosine = ['UAU', 'UAC'],
    Cysteine = ['UGU', 'UGC'],
    Tryptophan = ['UGG'],
    STOP = ['UAA', 'UAG', 'UGA'],
    )

def proteins(strand):
    codons = wrap(strand, 3)

    protein = []

    for codon in codons:
        for probit, codes in RNAdict.items():
            if codon in codes:
                if probit == 'STOP':
                    return protein
                protein.append(probit)

    return protein
