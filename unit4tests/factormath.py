def get_hcf(first, last):
    l1 = []
    for i, k in first:
        for j, l in last:
            if (i == j and k > l):
                l1.append((j, l))
                break
            elif (i == j and k < l):
                l1.append((i, k))
                break
    return l1

def get_lcm(first,last):
    first.extend(last)
    first.sort()
    for i in range(len(first) - 2):
        if (first[i][0] == first[i+1][0]):
            if (first[i][1] < first[i+1][1]):
                first.remove(first[i])
    return first

# def multiply(first, last):
#     result = []
#     first.extend(last)
#     first.sort()
#     for i in range(len(first) - 2):
#         if (first[i][0] == first[i+1][0]):
#             result.append((first[i][0],first[i][1]+first[i+1][1]))
#             first.remove(first[i+1])
#             first.remove(first[i])
#     result.extend(first)
#     return result


def multiply(first, last):
    result = []
    for i in first:
        for j in last:
            if i[0] == j[0]:
                result.append((i[0],i[1]+j[1]))
                last.remove(j)
                break
        else:
            result.append(i)
    result.extend(last)
    result.sort()
    print(result)
    return result
