def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(10):
    print(fibonacci(i), end=' ')  # Çıktı: 0 1 1 2 3 5 8 13 21 34

