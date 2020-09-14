from collections import Counter

def intersection(arrays):
    our_table = Counter()
    for i in range(len(arrays)):
        for j in arrays[i]:
            our_table[j] += 1

    result = [key for key in our_table.keys() if our_table[key] == len(arrays)]

    return result

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
