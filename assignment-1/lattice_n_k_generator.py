import math
def f(N, k):
    length = N-1
    sequence = [0]
    
    distances = list(range(2, math.floor(N/2)+1 +1, 1)) # second + 1 is because range function
    #print(distances)
    
    steps = []
    current_index = 1

    while len(steps) < len(distances):
        for _ in range(min(k, len(distances) - current_index)):  # Repeat up to k times or until the end is reached
            steps.append(current_index)
        current_index += 1
    #print(steps)
    print(N, len(distances))
    steps = steps[:len(distances)]
    print(steps)

    sequence += steps 
    sequence += steps[::-1]
    return sequence
    
print(f(13, 3))
print(f(11, 2))
print(f(9, 2))
# print(f(5, 2))# not working yet :/