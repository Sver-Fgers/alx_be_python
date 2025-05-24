# collect user finance data
income = int(input("Enter your monthly income:"))
expenses = int(input("Enter your total monthly expenses:"))

# calculate user montly savings
monthly_savings = income - expenses

# calculate user annual savings
interest = 5
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# output of user financials
print("Your montly savings are", monthly_savings)
print("Projected savings after one year, with interest, is:", projected_savings)