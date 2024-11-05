def find_single(arr):
    i = 0
    while i < len(arr):
        if arr[i] in arr[i + 1:]:
            new_arr = []
            for x in arr:
                if x != arr[i]:
                    new_arr.append(x)
            arr = new_arr
        else:
            return arr[i]
    return None

print(find_single([2, 2, -1, -1]))
print(find_single([4, 1, 2, 1, 2]))










    