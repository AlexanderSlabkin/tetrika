from collections import Counter


cnt = Counter()

def search_pairs(array, k):
    pairs = []
    for i in array:
        cnt[i] += 1

    for i in cnt:
        complement = k - i

        if (i, complement) not in pairs:
            if complement in cnt and i != complement:
                pairs.append((complement, i))
                
            elif i == complement and cnt[i] > 1:
                pairs.append((complement, i))


    return pairs


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 3, 8, 2], 5))
