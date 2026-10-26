import math

# Display menu to the user
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("Bond       - to calculate the amount you'll have to pay on a home loan\n")

# Ask user to choose a calculator
while True:
    choice = input("Enter either 'investment' or 'bond' to proceed: ").lower().strip()

    if choice in ("investment", "bond"):
        break
    else:
        print("Invalid selection. Please enter either 'investment' or 'bond'.")

# -----------------------------
# INVESTMENT CALCULATOR
# -----------------------------

if choice == "investment":

    # Validate deposit amount
    while True:
        try:
            amount = input("Enter the amount of money you are depositing: ")
            amount = amount.replace(",", "").replace("$", "").strip()
            amount = float(amount)
            break
        except ValueError:
            print("Invalid amount. Please enter a number such as 1000 or 1,000.50.")

    # Validate interest rate
    while True:
        try:
            rate = input("Enter the interest rate (e.g. enter 8 for 8%): ")
            rate = rate.replace("%", "").replace(",", "").strip()
            rate = float(rate) / 100
            break
        except ValueError:
            print("Invalid rate. Please enter a number such as 8 or 8.5.")

    # Validate years
    while True:
        try:
            years = int(input("Enter the number of years you plan on investing: "))
            if years > 0:
                break
            print("Years must be a positive whole number.")
        except ValueError:
            print("Please enter a valid whole number.")

    # Validate interest type
    while True:
        interest_type = input("Enter 'simple' or 'compound' interest: ").lower().strip()
        if interest_type in ("simple", "compound"):
            break
        print("Invalid interest type. Please enter either 'simple' or 'compound'.")

    # Calculate simple or compound interest
    if interest_type == "simple":
        total = amount * (1 + rate * years)
    else:
        total = amount * math.pow((1 + rate), years)

    print(f"\nYour investment will be worth: ${total:.2f}")

# -----------------------------
# BOND CALCULATOR
# -----------------------------       

elif choice == "bond":

    # Validate house value
    while True:
        try:
            house_value = input("Enter the present value of the house: ")
            house_value = house_value.replace(",", "").replace("$", "").strip()
            house_value = float(house_value)
            break
        except ValueError:
            print("Invalid amount. Please enter a number such as 250000 or 250,000.")

    # Validate interest rate
    while True:
        try:
            rate = input("Enter the interest rate (e.g. enter 7 for 7%): ")
            rate = rate.replace("%", "").replace(",", "").strip()
            rate = float(rate) / 100
            break
        except ValueError:
            print("Invalid rate. Please enter a number such as 7 or 7.5.")

    # Validate months
    while True:
        try:
            months = int(input("Enter the number of months you plan to repay the bond: "))
            if months > 0:
                break
            print("Months must be a positive whole number.")
        except ValueError:
            print("Please enter a valid whole number.")

    # Convert annual rate to monthly decimal rate
    monthly_rate = rate / 12

    # Bond repayment formula
    repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate) ** (-months))

    print(f"\nYour monthly repayment will be: ${repayment:.2f}")