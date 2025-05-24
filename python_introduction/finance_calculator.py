# collect user finance data
monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses:"))

# calculate user montly savings
Monthly_savings = monthly_income - monthly_expenses

# calculate user annual savings
Projected_savings = Monthly_savings * 12 + (Monthly_savings * 12 * 0.05)

# output of user financials
print("Your montly savings are", Monthly_savings)
print("Projected savings after one year, with interest, is:", Projected_savings)