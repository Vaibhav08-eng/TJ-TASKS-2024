def generate_pascal_triangle(n):
    #write your code here
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    print(triangle)

if __name__ == "__main__":
    n = 5
    generate_pascal_triangle(n)
