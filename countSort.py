""""""
"""COUNTSORT PARA NUMEROS"""
def countsortNum(arr):
    # Create an array with all values set to zero
    output = [0 for i in range(len(arr))]

    # Create a count array to store count of individual
    # number and initialize count array as 0
    count = [0 for i in range(256)]

    # Store count of each number
    for i in arr:
        count[i] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this number in output array
    for i in range(256):
        count[i] += count[i - 1]

    # Build the output number array
    for i in range(len(arr)):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    return output


"""COUNTSORT PARA CARACTERES"""
def countSort(arr):
    # The output character array that will have sorted arr
    output = [0 for i in range(len(arr))]

    # Create a count array to store count of individual
    # characters and initialize count array as 0
    count = [0 for i in range(256)]

    # For storing the resulting answer since the
    # string is immutable
    ans = ["" for _ in arr]

    # Store count of each character
    for i in arr:
        count[ord(i)] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this character in output array
    for i in range(256):
        count[i] += count[i - 1]

    # Build the output character array
    for i in range(len(arr)):
        output[count[ord(arr[i])] - 1] = arr[i]
        count[ord(arr[i])] -= 1

    # Copy the output array to arr, so that arr now
    # contains sorted characters
    for i in range(len(arr)):
        ans[i] = output[i]
    return ans


# Driver program to test above function
arr = "geeksforgeeks"
ans = countSort(arr)
print("Sorted character array is % s" % ("".join(ans)))

vector = [10, 5, 9, 2, 3, 6, 6]
vector = countsortNum(vector)
for i in vector:
    print(i)
