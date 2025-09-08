principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
n = int(input("Enter the number of times interest is compounded per year (e.g., 1 for annually, 4 for quarterly, 12 for monthly): "))
time = float(input("Enter the number of years the money will be invested: "))
future_value = principal * (1 + rate / n)**(n * time)
compound_interest = future_value - principal
print(f"\nFuture Value (including interest): ${future_value:.2f}")
print(f"Total Compound Interest Earned: ${compound_interest:.2f}")