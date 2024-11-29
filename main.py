import random
import csv
import os
import sys

def check_dependencies():
    required_modules = {'pandas', 'openpyxl'}
    for module in required_modules:
        try:
            __import__(module)
        except ImportError:
            response = input(f"The required module '{module}' is not installed. Would you like to install it now? (yes/no): ")
            if response.lower() == 'yes':
                try:
                    import subprocess
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', module])
                    __import__(module)
                    print(f"{module.capitalize()} installed successfully.")
                except subprocess.CalledProcessError:
                    print(f"Failed to install '{module}'. Please install it manually.")
                    sys.exit(1)
            else:
                print(f"{module.capitalize()} is required to run this program. Exiting.")
                sys.exit(1)

def generate_stock_data(days):
    inventory = 2000  # Initial stock level
    records = []
    for day in range(days):
        sold_units = random.randint(0, min(200, inventory))
        inventory -= sold_units
        restocked_units = 0
        if day % 7 == 0 and day != 0:
            restocked_units = 2000 - inventory
            inventory = 2000
        records.append({
            'day': day,
            'sold_units': sold_units,
            'restocked_units': restocked_units,
            'available_units': inventory
        })
    return records

def generate_excel_report(records):
    import pandas as pd
    df = pd.DataFrame(records)
    filename = f'inventory_report_{pd.Timestamp.now().strftime("%Y%m%d%H%M%S")}.xlsx'
    df.to_excel(filename, index=False)
    print(f"Report generated successfully: {filename}")
    return filename

def check_report(filename):
    import pandas as pd
    try:
        df = pd.read_excel(filename)
        expected_rows = 50
        actual_rows = len(df)
        if actual_rows == expected_rows:
            print(f"Report check successful: The report contains {actual_rows} entries.")
        else:
            print(f"Report check failed: Expected {expected_rows} entries, but found {actual_rows}.")
    except Exception as e:
        print(f"Failed to check the report: {e}")

def main():
    print("Checking for necessary dependencies...")
    check_dependencies()
    print("Starting Inventory Management System...")
    latest_report_filename = None

    while True:
        print("\n1. Generate Report")
        print("2. Report Check")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            inventory_records = generate_stock_data(50)
            latest_report_filename = generate_excel_report(inventory_records)
        elif choice == '2':
            if latest_report_filename:
                check_report(latest_report_filename)
            else:
                print("No report has been generated yet.")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
