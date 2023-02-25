def fibonacci(num):
    a = 0
    b = 1
    if num == a or num == b:
        return True
    else:
        while b <= num:
            temp = b
            b = a + b
            a = temp
            if b == num:
                return True
        return False

num = int(input("Digite um número: "))
a = 0
b = 1
fib = [a, b]
while b < num:
    temp = b
    b = a + b
    a = temp
    fib.append(b)

if num in fib:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
    
