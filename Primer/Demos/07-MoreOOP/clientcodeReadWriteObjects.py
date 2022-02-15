from accounting3 import BankAccount

# Create and use objects.
accounts = []
accounts.append(BankAccount("Huey"))
accounts.append(BankAccount("Louis"))
accounts.append(BankAccount("Dewey"))

accounts[0].deposit(100)
accounts[1].withdraw(200)
accounts[2].deposit(300)

# One way to write lines to a file.
with open("accounts1.txt", "w") as fhOut:
    for acc in accounts:
        fhOut.write(acc.toString() + "\n")

# Another way to write lines to a file.
with open("accounts2.txt", "w") as fhOut:
    fhOut.writelines([acc.toString() + "\n" for acc in accounts])
        
# Read the file to recreate objects.
accountsReadIn = []
with open("accounts1.txt", "r") as fhIn:
    for line in fhIn:
        account = BankAccount.fromString(line)
        accountsReadIn.append(account)

print("Here are the accounts read in: ")        
for acc in accountsReadIn:
    print(acc.toString())
