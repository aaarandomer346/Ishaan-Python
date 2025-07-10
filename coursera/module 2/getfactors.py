def get_factors1(x):
    factors = []

    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
    return factors
print(get_factors1(int(input("Give a number you want to find factors of: "))))