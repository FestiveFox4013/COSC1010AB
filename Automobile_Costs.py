def main():
    # Prompts for expenses
    loan = float(input("Enter your monthly car loan payment: "))
    insurance = float(input("Enter your monthly insurance cost: "))
    gas = float(input("Enter your monthly gas cost: "))
    oil = float(input("Enter your monthly oil cost: "))
    tires = float(input("Enter your monthly tire cost: "))
    maintenance = float(input("Enter your monthly maintenance cost: "))

    # Calculate total monthly and annual costs
    total_monthly = loan + insurance + gas + oil + tires + maintenance
    total_annual = total_monthly * 12

    # Shows results
    print(f"\nTotal monthly cost: ${total_monthly:,.2f}")
    print(f"Total annual cost: ${total_annual:,.2f}")


if __name__ == "__main__":
    main()