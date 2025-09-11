class Bucket:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.empty()

    def fill(self):
        self.has = self.size

    def empty(self):
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
        
        if other.has == goal:
            bucket, other = other, bucket
            continue
            
        if not bucket.has:
            bucket.fill()
            moves += 1
            if other.size == goal:
                other.fill()
                moves += 1
            continue
            
        if not other.space:
            other.empty()
            moves += 1

        pour = min(bucket.has, other.space)
        bucket.has -= pour; other.has += pour
        moves += 1

    return moves, bucket.name, other.has
