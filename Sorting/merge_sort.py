brr = [2, 3, 1, 6, 4, 5]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        l = 0
        r = 0
        k = 0
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                arr[k] = left[l]
                l += 1

            else:
                arr[k] = right[r]
                r += 1
            k += 1

        while l < len(left):
            arr[k] = left[l]
            l += 1
            k += 1

        while r < len(right):
            arr[k] = right[r]
            r += 1
            k += 1

print(brr)
merge_sort(brr)
print(brr)
