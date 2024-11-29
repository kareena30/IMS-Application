import random

# Function to handle restocking logic
def restock_inventory(available_items, inventory_records, current_day):
    print(f"Day {current_day}: Starting restock process...")
    print("Inventory before restocking:", available_items)

    # Restocking logic, only on designated days
    if current_day % 7 == 0:
        needed_stock = 2000 - available_items
        available_items += needed_stock
        print(f"Restocked {needed_stock} units.")
    else:
        needed_stock = 0
        print("No restocking today.")

    print("Inventory after restocking:", available_items)
    print("Restock process completed.")

    # Update the inventory records
    inventory_records.append({
        'day': current_day,
        'sold_units': 0,  # This will be updated by the sales function
        'restocked_units': needed_stock,
        'available_units': available_items
    })
    return available_items

# Function to simulate daily sales
def simulate_sales(available_items, inventory_records):
    if available_items > 0:  # Ensuring there are items to be sold
        sold_units = random.randint(0, min(200, available_items))
        available_items -= sold_units
        print(f"Sold {sold_units} units today.")
        inventory_records[-1]['sold_units'] = sold_units  # Update the last record with actual sales
    return available_items

# Main function to control the script
if __name__ == "__main__":
    inventory_records = []
    available_items = 2000  # Initial inventory
    for day in range(15):  # Simulate 15 days
        if day % 7 != 0:  # Simulate sales on non-restocking days
            available_items = simulate_sales(available_items, inventory_records)
        available_items = restock_inventory(available_items, inventory_records, day)
    
    # Print the records to see the output
    for record in inventory_records:
        print(record)
