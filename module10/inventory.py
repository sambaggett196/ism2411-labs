# Reflection:
# 1: The most suprising thing I learned about lists is that they are mutable. It was much easieer to change the contents of a list than I expected coming in. I was also suprised to know that I can use built in fucntions on lists aswell.
# 2: A business situation where a Python list would have been useful was when I used to work retail. The list could have been used to keep track of the inventory and how stock was moving. It would have been useful to have an accurate list of items and their quanities when reordering product.
print("--- Excercise 1: Build the list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Excercise 2: Index Practice ---")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2
print(inventory[middle]) # middle item

print("--- Excercise 3: Slicing Practice ---")
print(inventory[:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every second item

print("--- Excercise 4: Modifying the List ---")
inventory.append("envelope") # add an item to the end
print(inventory) 
inventory.remove("tape") # remove an item
print(inventory)
inventory.sort() # sort the list
print(inventory)

print("--- Excercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeErrror caught:", error)
    print("Tuples protect coordinates: a location should never be changed by accident.")

print(coords)

print("--- Excercise 6: Average List of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("--- Excercise 7: Accumulator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * 0.9, 2)) # 10% discount

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Excercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")
