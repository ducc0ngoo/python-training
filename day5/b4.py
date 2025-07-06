hours_worked = float(input("Please enter the hours you worked this week: "))
hourly_wage = float(input("Please enter your hourly wage: "))

total_earning = hours_worked * hourly_wage

if hours_worked > 40:
    total_earning = 40 * hourly_wage + (hours_worked - 40) * 1.1 * hourly_wage
print(f"The final wage of this week is: ${total_earning:.2f}")
