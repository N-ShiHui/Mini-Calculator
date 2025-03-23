import csv

log_book = {"product": [],
            "measurement": [], 
            "location1": [],
            "location2": [],
            "travel_fare": [],
            "savings($)": []}
product = input("What is the item you bought?")
measurement = input("How do you measure the product? (g/ml/items):")

if measurement == 'g' or 'ml':
    weight1 = float(input("How heavy was the product on the previous purchase?"))
    price1 = float(input("How much did the previous merchant sell for? $"))
    weight2 = float(input("How heavy did you purchase it this time?"))
    price2 = float(input("How much did the current merchant sell for? $"))
elif measurement == 'item':
    print("Product is unmeasurable and will be considered as 1 item.")
else:
    print("Invalid input, please choose a valid option.")

location1 = input(f"Where did you previously purchase the {product}?")
location2 = input("What is the new location you bought this from?")
travel = input("Are you required to travel to acquire the item? Y/N")
if travel == 'Y':
    travel_fare = float(input("How much were your total travelling expenses? $"))
    price = price1/weight1 * weight2 # Price of product bought at initial rates
    savings = price - price2 - travel_fare
    print(f"Total amount saved: ${savings:.2f}")
elif travel == 'N':
    price = price1/weight1 * weight2
    savings = round(price - price2, 2)
    print(f"Total amount saved: ${savings:.2f}")
else:
    print("Please enter a valid choice.")

# Append new information to records
log_book["product"].append(product)
log_book["measurement"].append(measurement)
log_book["location1"].append(location1)
log_book["location2"].append(location2)
log_book["travel_fare"].append(travel_fare)
log_book["savings($)"].append(savings)

# Open csv file for writing, then change the code to append mode after first creation to add new record in the csv file.
'''
with open("log_book.csv", "w", newline="") as fp:
    # Create a writer object
    writer = csv.DictWriter(fp, fieldnames=log_book.keys())

    # Write header row
    writer.writeheader()

    # Write the data rows
    writer.writerow(log_book)
    print('Done writing dict to a csv file.')
'''
with open("log_book.csv", "a") as fp:
    
    # Create a writer object
    writer = csv.DictWriter(fp, fieldnames=log_book.keys())

    # Write the data rows
    writer.writerow(log_book)
    print('Csv file updated.')

# Open csv file for reading
with open("log_book.csv", "r") as infile:
    # Create a reader object
    reader = csv.DictReader(infile)

    # Iterate through the rows
    for rows in reader:
        print(rows)