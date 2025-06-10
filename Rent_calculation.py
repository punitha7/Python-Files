rent = int(input("Enter the rent : "))
roomates = int(input("number of roomates : "))
food_expense = int(input("Enter the food expense : "))
Grocerry_expense = int(input("Enter the grocerry expense : "))
Electricity_expense = int(input("Enter the electricity cost : "))
Electricity_unit = int(input("how many units run: "))
Electricity_calculation = (Electricity_expense*Electricity_unit)
Total_expense = food_expense + Grocerry_expense+ Electricity_calculation
Rent_calculation = (rent + Total_expense) / roomates

print(f" Rent per each person for the month is {Rent_calculation}")
