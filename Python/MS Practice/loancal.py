L = float(input('Cost of Loan: '))
i = float(input('Interest Rate(In Decimals): '))
n = float(input('Number of Years: '))
#Formula for monthly payment holds for when n > 1
M = ((L*i*n*(1+i))/(((1+i)*n)-1))
print(f'Monthly Payment: {M}')
