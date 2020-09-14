def get_indices_of_item_weights(weights, length, limit):
    hash_table = {}

    for i in range(length):
        if weights[i] in hash_table.keys():
            hash_table[weights[i]] = [hash_table[weights[i]], i]
        else:
            hash_table[weights[i]] = i

        remaining_weight = limit - weights[i]
        if remaining_weight == weights[i]:
            if isinstance(hash_table[remaining_weight], list):
                indices = sorted(hash_table[remaining_weight], reverse=True)
                return indices
            else:
                continue

        if remaining_weight in hash_table.keys():
            weights = [remaining_weight, weights[i]]
            indices = sorted([hash_table[weight] for weight in weights], reverse=True)
            return indices

    return None
