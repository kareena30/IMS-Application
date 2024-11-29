import random

def daily_sales(available_items, inventory_records, current_day):
    # Restocking logic: every 7 days
    if current_day % 7 == 0:
        needed_stock = 2000 - available_items
        available_items += needed_stock
        restocked_units = needed_stock
    else:
        restocked_units = 0

    # Ensure sales only occur if there is inventory available
    if available_items > 0:
        sold_units = random.randint(0, min(200, available_items))
        available_items -= sold_units
    else:
        sold_units = 0  # No sales can occur if no inventory is available

    # Append this day's sales data to inventory records
    inventory_records.append({
        'day': current_day,
        'sold_units': sold_units,
        'restocked_units': restocked_units,
        'available_units': available_items
    })
    return available_items

# Testing the daily_sales function
if __name__ == "__main__":
    inventory_records = []
    available_items = 500  # Starting inventory for testing

    # Simulate sales for a series of days
    for day in range(1, 21):  # Simulate for 20 days to see multiple restocking events
        print(f"Day {day}:")
        available_items = daily_sales(available_items, inventory_records, day)
        print(inventory_records[-1])  # Print the record for the current day

    # Optionally, print all records at the end
    print("\nFull inventory records:")
    for record in inventory_records:
        print(record)
