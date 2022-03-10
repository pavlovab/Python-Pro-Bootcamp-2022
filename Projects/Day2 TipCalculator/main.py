print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
num_of_people = int(input("How many people to split the bill? "))

tip = tip_percentage / 100 * bill
bill = bill + tip_percentage 
amount_per_person = bill / num_of_people 
final_amount = "{:.2f}".format(amount_per_person)

print(f"Each person should pay: ${final_amount}")

