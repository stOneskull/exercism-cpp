def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("strand lengths not equal")
    differences = 0
    for i, nuc in enumerate(strand_a):
        if nuc != strand_b[i]:
            differences += 1
    return differences