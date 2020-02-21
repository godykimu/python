#Input data from user
recepientName = input("Enter name of Recepient: ")
recepientPhone = input("Enter Phone Number: ")
amount = int(input("Enter Amount: "))

#Notify user
print("Send Kes {} to {} of {}?".format(amount,recepientName,recepientPhone))

#User confirmation
confirm = int(input("Press 1 to proceed: "))
if (confirm == 1):
    balance = 3000
    while amount > balance:
        print("Insufficeint Balance, your Balance is {}".format(balance))
        break
    
else:
    newBalance = balance - amount
    print("Confirmed Kes {} sent to {} {}, New Wallet Balance is Kes {}".format(amount,recepientPhone,recepientName,newBalance))