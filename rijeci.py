n = int(input())
a_count = 1  # Initial 'A' count
b_count = 0  # Initial 'B' count

for _ in range(n):
    
    new_a_count = b_count
    new_b_count = a_count + b_count

    a_count = new_a_count
    b_count = new_b_count

print(a_count, b_count)
