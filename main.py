print("Welcome to tip calculator.")

totalBill = float(input("What was the total bill? $"))
tipPercaent = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
numPeople = int(input("How many people to split the bill? "))

cost = (totalBill * (1 + (tipPercaent / 100))) / numPeople
cost = round(cost, 2)
print(f"Each person should pay: ${cost}") 
