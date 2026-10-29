def mean(values):
    if not values: raise ValueError("List cannot be empty.")
    return sum(values) / len(values)

def maximum(values):
    if not values: raise ValueError("List cannot be empty.")
    return max(values)

def minimum(values):
    if not values: raise ValueError("List cannot be empty.")
    return min(values)
