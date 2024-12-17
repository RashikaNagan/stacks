numbers = [9, 23, 53, 61, 22, 35, 1234, 2]

def mergesort(numbers):
    if len(numbers) <= 1:
        return numbers
    
    middleindex = len(numbers) // 2

    lefthalf = numbers[:middleindex]
    righthalf = numbers[middleindex:]

    lefthalf = mergesort(lefthalf)
    righthalf = mergesort(righthalf)

    merge = []
    i = 0
    j = 0
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] > righthalf[j]:  
            merge.append(lefthalf[i])
            i += 1
        else:
            merge.append(righthalf[j])
            j += 1

    merge.extend(lefthalf[i:])
    merge.extend(righthalf[j:])

    return merge

print(mergesort(numbers))