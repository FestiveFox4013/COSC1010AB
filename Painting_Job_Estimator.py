SQ_FT_PER_GALLON = 112
LABOR_HOURS_PER_GALLON = 8
LABOR_RATE_PER_HOUR = 35.00

def main():
    print("--- Paint Job Cost Estimator ---\n")
    
    # Inputs for area and price.
    try:
        square_feet = float(input("Enter the square feet of wall space to be painted: "))
        paint_price_per_gallon = float(input("Enter the price of the paint per gallon: $"))
        
        if square_feet < 0 or paint_price_per_gallon < 0:
            print("Error: Input values cannot be negative.")
            return
            
    except ValueError:
        print("Error: Please enter valid numerical values.")
        return

    gallons_required = square_feet / SQ_FT_PER_GALLON
    hours_labor_required = gallons_required * LABOR_HOURS_PER_GALLON
    
    cost_of_paint = gallons_required * paint_price_per_gallon
    labor_charges = hours_labor_required * LABOR_RATE_PER_HOUR
    total_cost = cost_of_paint + labor_charges

    # This part of the code will be used to show the results of the calculated values.
    print("\n" + "="*35)
    print("       ESTIMATED CHARGES       ")
    print("="*35)
    print(f"Gallons of paint required : {gallons_required:.2f}")
    print(f"Hours of labor required   : {hours_labor_required:.2f}")
    print(f"Cost of the paint         : ${cost_of_paint:,.2f}")
    print(f"Labor charges             : ${labor_charges:,.2f}")
    print(f"-----------------------------------")
    print(f"Total cost of paint job   : ${total_cost:,.2f}")
    print("="*35)

if __name__ == "__main__":
    main()