class Bucket:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.has = 0

    @property
    def space(self):
        return self.size - self.has


def measure(bucket_one, bucket_two, goal, start_bucket):
    if goal > max(bucket_one, bucket_two):
        raise ValueError("Goal cannot be larger than both buckets")
    
    one = Bucket("one", bucket_one)
    two = Bucket("two", bucket_two)
    
    if start_bucket == "one":
        bucket, other = one, two
    elif start_bucket == "two":
        bucket, other = two, one
    else:
        raise ValueError("start_bucket must be 'one' or 'two'")
    
    if bucket.size == goal:
        return 1, bucket.name, 0
    if other.size == goal:
        return 2, other.name, bucket.size
    
    return go(bucket, other, goal)


def go(bucket, other, goal):
    moves = 0
    seen = set()
    
    while bucket.has != goal and other.has != goal:
        state = (bucket.has, other.has)
        if state in seen:
            raise ValueError("Unsolvable with given values")
        seen.add(state)

        if bucket.has == 0:
            bucket.has = bucket.size  
        elif other.space == 0:
            other.has = 0
        else:
            pour = min(bucket.has, other.space)
            bucket.has -= pour
            other.has += pour
            
        moves += 1
        
    if bucket.has == goal:
        return moves, bucket.name, other.has
    return moves, other.name, bucket.has
