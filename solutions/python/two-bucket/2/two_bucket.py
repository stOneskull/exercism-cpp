class Bucket:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.has = 0

    @property
    def space(self):
        return self.size - self.has


def measure(bucket_one, bucket_two, goal, start_bucket):
    
    one = Bucket("one", bucket_one)
    two = Bucket("two", bucket_two)
    
    if start_bucket == "one":
        bucket, other = one, two
    elif start_bucket == "two":
        bucket, other = two, one

    moves = 0
    
    while bucket.has != goal:
        
        if not bucket.has:
            bucket.has = bucket.size
            moves += 1
            if other.size == goal:
                bucket, other = other, bucket
            continue

        if not other.space:
            other.has = 0
            moves += 1

        pour = min(bucket.has, other.space)
        bucket.has -= pour; other.has += pour
        moves += 1

    return moves, bucket.name, other.has
