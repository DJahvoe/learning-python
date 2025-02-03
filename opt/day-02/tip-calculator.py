total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
total_person = int(input("How many people to split the bill? "))

total_amount = total_bill * (1 + tip_percentage / 100)
total_amount_per_person = total_amount / total_person

print(f"Each person should pay: ${round(total_amount_per_person, 2)}")