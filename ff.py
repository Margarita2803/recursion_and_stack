def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

def sum_list(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + sum_list(arr[1:])

arr = [3, 5, 8]
print(sum_list(arr))

