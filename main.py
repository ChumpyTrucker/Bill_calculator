
print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $ "))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? % "))
people = int(input("How many people to split the bill? "))

person = total_bill / people
tip = person / 100 * percentage_tip
bill = person + tip
# final_bill = round(bill, 2)
final_bill = "{:.2f}".format(bill)


print(f"Each person should pay: $ {final_bill} ")
