def slices(series, length):

    if length < 1 or length > len(series):
        raise ValueError("invalid length given: {}".format(length))

    the_slices = []

    start = 0

    while start + length <= len(series):
        the_slices.append(series[start:start+length])
        start += 1

    return the_slices