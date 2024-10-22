# Driver Code
def number_spiral(y, x):
    #write yout code here
    n = max(abs(x), abs(y))
    
    largest_number = (2 * n) ** 2
    
    if x == n: 
        return largest_number - (n - y)
    elif y == -n: 
        return largest_number - (2 * n) + (n - x)
    elif x == -n: 
        return largest_number - (3 * n) + (y + n)
    else:  
        return largest_number - (n - x)
# Default Test Cases
test_cases = [
    (2, 3),  # Output: 8
    (1, 1),  # Output: 1
    (4, 2),  # Output: 15
]

# Run Test Cases
for y, x in test_cases:
    print(number_spiral(y, x))

# Sample Output:
# 8
# 1
# 15
