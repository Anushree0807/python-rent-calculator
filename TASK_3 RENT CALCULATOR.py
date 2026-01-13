rent= int(input("Enter the amount of the rent: "))
food= int(input("Enter the amount of the food: "))
electricity_spent = int(input("Enter the amount of the electricity spent: "))
charge_per_unit = int(input("Enter the charge per unit: "))
number_of_persons=int(input("Enter the number of persons living in room: "))

electricity_bill  = electricity_spent * charge_per_unit

Amount_to_be_paid_by_one_person = (rent + food + electricity_bill) / number_of_persons

print(Amount_to_be_paid_by_one_person)
