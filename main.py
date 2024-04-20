print("WELCOME TO FIBONACII GENERATOR")
print("EXAMPLE 'Fibonacci [Index]: Number'")
print("GIVE A NUMBER STARTING (COUNTING WILL START FORM ZERO)")
terms = int(input("NO OF TERMS:"))
Fibonacci = [0, 1]
a = 0
b = 1
for i in range(0, terms):
    c = a + b
    Fibonacci.append(c)
    a = b
    b = c
    print("Fibonacci [", i, "]: ", Fibonacci[i])