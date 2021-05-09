'''
    Bubble Sort (O(n^2))

    Source: https://www.youtube.com/watch?v=UOuH8IVFAGk
    Title: Bubble Sort algorithm implementation in Python
    Author: Engineer Man
'''

def sort(arr):
    while True:
        corrected = False  # determines whether the function iterates again
        for i in range(0, len(arr) - 1):  # iterate over the array
            if arr[i] > arr[i+1]:  # check whether the order is right
                arr[i], arr[i+1] = arr[i+1], arr[i]  # swap elements
                corrected = True
            if not corrected:
                return arr

# best O(n)
print(sort([1, 2, 3, 4, 5]))

# average O(n^2)
print(sort([4, 2, 3, 1, 6, 5]))

# worst O(n^2)
print (sort([6, 5, 4, 3, 2, 1]))
