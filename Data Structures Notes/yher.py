def binarySearch1(arr, l, r, x):
    # Check base case

    if r >= l:
        mid = int(l + (r - l) / 2)

        # If element is present at the middle itself

        if arr[mid] == x:

            return mid

        # If element is smaller than mid, then it

        # can only be present in left subarray

        elif arr[mid] > x:

            return binarySearch1(arr, l, mid - 1, x)

        # Else the element can only be present

        # in right subarray

        else:

            return binarySearch1(arr, mid + 1, r, x)

    else:

    # Element is not present in the array

        return -1


def binarySearch2(arr, l, r, x):
    while l <= r:
        mid = int(l + (r - l) / 2)

        # Check if x is present at mid

        if arr[mid] == x:

            return mid

        # If x is greater, ignore left half

        elif arr[mid] < x:

            l = mid + 1

        # If x is smaller, ignore right half

        else:

            r = mid - 1

        # If we reach here, then the element was not present

        return -1


print(binarySearch1([1,2,3,4], 0, 3, 3))
print(binarySearch2([1,2,3,4], 0, 3, 3))