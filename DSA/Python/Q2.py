def climb_stairs(n):
if n == 0:
        return 1
    elif n == 1:
        return 1
    
    # Initialize the base cases
    ways = [0] * (n + 1)
    ways[0], ways[1] = 1, 1
    
    # Fill the array with the number of ways to reach each step
    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    
    return ways[n]
if __name__ == "__main__":
    n = 2
    print(climb_stairs(n))
