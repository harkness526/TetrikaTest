
def search_pairs(array, k):
    result = []
    for i, a in enumerate(array):
        for j,b in enumerate(array):
            if i != j and a + b == k:
                if b < a:
                    a,b = b,a 
                if (a,b) not in result:
                    result.append((a,b))
                break
    return result

array = [1, 2, 6, 5, 3, 4, 7, 8, 3, 2]
print(search_pairs(array, 5))