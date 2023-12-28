# Python3 program to find Closest number in a list
# Reference: https://www.geeksforgeeks.org/python-find-closest-number-to-k-in-given-list/

def closest(lst, K):
    return lst[min(range(len(lst)), key=lambda i: abs(lst[i] - K))]


# Driver code
lst = [3.64, 5.2, 9.42, 9.35, 8.5, 8]
K = 9.1
print(closest(lst, K))
