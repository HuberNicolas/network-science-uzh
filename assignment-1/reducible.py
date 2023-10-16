import numpy as np
from itertools import permutations

n = 5  # matrix size

A = np.array([[0, 1, 1, 0, 0], [1, 0, 1, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0]])

# Generate all permutations of the identity matrix
perms = list(permutations(range(n)))
f = len(perms)  # number of permutations

# Create a list to store P_T * A * P for each permutation
result_list = []

# Create a list to store results with specific zeros below the diagonal
results_with_zeros_below_diag = []

for perm in perms:
    P = np.eye(n)[list(perm), :]
    P_T = P.T
    result = np.dot(np.dot(P_T, A), P)
    result_list.append(result)

    # Check if specific off-diagonal elements are zero
    # indices_to_check = [(1, 0), (2, 0), (2, 1), (3, 0), (3, 1), (3, 2),  (4, 0), (4, 1), (4, 2), (4, 3), ] # all indices; use as template
    
    indices_to_check = [(1, 0), (2, 0), (3, 0), (4, 0)]
    print(f"Case 1: {indices_to_check}")
    if all(result[i, j] == 0 for i, j in indices_to_check):
        results_with_zeros_below_diag.append(result)
        #print(result)
        #print(P)
        #print(P_T)
   
    indices_to_check = [(2, 0), (2, 1), (3,0), (3, 1), (4, 0), (4, 1)]
    print(f"Case 2: {indices_to_check}")
    if all(result[i, j] == 0 for i, j in indices_to_check):
        results_with_zeros_below_diag.append(result)
        #print(result)
        #print(P)
        #print(P_T)
    
    indices_to_check = [(3, 0), (3, 1), (3,2), (4, 0), (4, 1), (4, 2)]
    print(f"Case 3: {indices_to_check}")
    if all(result[i, j] == 0 for i, j in indices_to_check):
        results_with_zeros_below_diag.append(result)
        #print(result)
        #print(P)
        #print(P_T)
    
  
    
    indices_to_check = [(4, 0), (4, 1), (4, 2), (4, 3)]
    print(f"Case 4: {indices_to_check}")
    if all(result[i, j] == 0 for i, j in indices_to_check):
        results_with_zeros_below_diag.append(result)
        #print(result)
        #print(P)
        #print(P_T)

    # Print the result for the current permutation
    #print(f"Result for permutation {perm}:")
    #print(result)
    

# Remove duplicates while preserving order
unique_results = []
for result in results_with_zeros_below_diag:
    if not any(np.array_equal(result, unique_result) for unique_result in unique_results):
        unique_results.append(result)

# Access and print the unique matrices
for i, result in enumerate(unique_results):
    print(f"Unique result with specific zeros below the diagonal for permutation {i}:")
    print(result) 

print('Calculation finished')
