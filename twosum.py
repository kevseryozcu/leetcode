def Solution(arr, target):
    hashmap = dict();
    for n in range(len(arr)):
        if target - arr[n] in hashmap: return [hashmap[target - arr[n]], n]
        hashmap[arr[n]] = n
    return [-1, -1]


print(Solution(arr=[3, 5, 7, 1], target=4))
