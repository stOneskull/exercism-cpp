def slices(series, length):
    if not series:
        raise ValueError("no series given")
    if length < 1 or length > len(series):
        raise ValueError(f"invalid length {length}")

    slicing = len(series) - length + 1
    
    return [
        series[start:start+length]
        for start in range(slicing)
    ]
