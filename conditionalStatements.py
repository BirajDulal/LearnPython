print("This is practice for conditional statement")
# Write a  program to input electricity unit charges and calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill
print("Welcome to electric bill generator!!")
unitElectricity = int(input("Enter your electricity unit for this month: \n"))
bill = 0
if unitElectricity <= 50:
    bill = unitElectricity * 0.5
elif unitElectricity <= 150:
    bill = unitElectricity * 0.5
    remaningBill = unitElectricity - 50
    bill = bill + (remaningBill * 0.75)
elif unitElectricity <= 250:
    bill = unitElectricity * 0.5
    remaningBill = unitElectricity - 50
    bill = bill + (remaningBill * 0.75)
    remaningBill = remaningBill - 100
    bill = bill + (remaningBill * 1.20)
elif unitElectricity > 250:
    bill = unitElectricity * 0.5
    remaningBill = unitElectricity - 50
    bill = bill + (remaningBill * 0.75)
    remaningBill = remaningBill - 100
    bill = bill + (remaningBill * 1.20)
    remaningBill = remaningBill - 100
    bill = bill + (remaningBill * 1.50)
else:
    print("Please enter the correct electricity unit!!")
finalBill = bill + (bill*0.20)
print(f"Your electricity bill for this month is{finalBill}$")
    
  ## next method  
eBill = int(input("What is your bill? "))
bill = 0
if eBill <= 50:
    bill = eBill * 0.5
elif eBill <=150:
    bill = 25 + (eBill-50) * 0.75
elif eBill <=250:
    bill = 100 + (eBill-150)*1.20
elif eBill > 250:
    bill = 220 + (eBill-250)*1.5
else:
    print("Please enter valid information")
finalBill = bill + (bill*0.2)
print(f"Your final bill is {finalBill}$")