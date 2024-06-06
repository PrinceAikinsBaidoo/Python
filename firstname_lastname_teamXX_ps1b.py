annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semiannual raise, as a decimal: "))
monthly_expenses = float(input("Enter your monthly living expenses: "))
#total_savings = 0

monthly_salary = annual_salary / 12
portion_down_payment = 0.25 * total_cost
# Calculating for the monthly salary that remains after subtracting the monthly expenses.
net_monthly_salary = monthly_salary - monthly_expenses

# Calculating for the portion of the monthly salary saved
actual_portion_saved = portion_saved * net_monthly_salary
months = 0
current_savings = 0

# Finding the number of months to save until the current_savings = portion_down_payment
while current_savings <= portion_down_payment:
    # Increasing months by 1
    months += 1

    # increasng monthly salary on 6th-month bases
    if months % 6 == 0:
        monthly_salary = monthly_salary + (monthly_salary * semi_annual_raise)
        net_monthly_salary = monthly_salary - monthly_expenses
        actual_portion_saved = portion_saved * net_monthly_salary
        
    # Finding monthly current_savings
    current_savings = current_savings + (current_savings * 0.04/12) + actual_portion_saved

    
   
print(f"Number of months: {months}")