def slices(series, length):
    if not series:
        raise ValueError("no series given")
    if length < 1 or length > len(series):
        raise ValueError(f"invalid length {length}")

    sliced = []

    start = 0
    while len(series) >= start + length:
        sliced.append(series[start:start+length])
        start += 1

    return sliced
