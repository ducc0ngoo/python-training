employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
for employee in employees:
    name = employee[0]
    hours_worked = employee[1]
    hourly_rate = employee[-1]
    weekly_wage = hours_worked * hourly_rate
    print(f"{name} get ${weekly_wage:.2f} this week")
