import numpy as np
# Approach based on reference:
# https://www.youtube.com/watch?v=o7VCeCxHCTI&ab_channel=MarkKeith
height = [60, 62,65, 68, 70, 74]
weight = [140, 138, 150, 166, 190, 250]
result = np.corrcoef(height, weight)
print(result)
print()


# Same result using matrix and getting same result
matrix = np.array([[60, 62,65, 68, 70, 74], [140, 138, 150, 166, 190, 250]])
# print(matrix)
result2 = np.corrcoef(matrix)
print(result2)

# Transpose matrix to see difference in results
result3 = np.corrcoef(matrix.transpose())
print(result3)


## =================================================