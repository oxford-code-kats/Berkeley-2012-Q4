def dissimilarity(a, b):
    if a == b:
        return 0 
    if len(a) > 0 and len(b) > 0 and a[0] == b[0]:
        return dissimilarity(a[1:], b[1:])
    return len(a+b)
