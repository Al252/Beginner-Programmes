class Functions:
    def factors(self, num):
        fact = []
        for a in range(1, num+1):
            if num % a == 0:
                fact.append(a)
        return fact

    def fibonacci(self, limit):
        a = 0
        b = 1
        fib = []
        while b < limit:
            fib.append(a)
            b = a + b
            a = b - a
        return fib

    def p_num(self, limit):
        prime = []
        composite = []
        u = list(range(2, limit))
        for a in range(2, limit):
            for b in range(2, a):
                if a % b == 0:
                    composite.append(a)
                    break
            else:
                prime.append(a)
        return prime

func = Functions()
print(func.p_num(100))
