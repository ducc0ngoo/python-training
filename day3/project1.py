name = input("Please enter your name: ").strip().title()
hourly_wage = float(input("Please enter your hourly wage: "))
hours_worked = float(input("Please enter the hours you worked: "))
total_earnings = hourly_wage * hours_worked

#Regina George earned $800 this week.
print(f"{name} earned ${total_earnings:.3f} this week.")
