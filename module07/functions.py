# Self Assessment Questions:
# 1: The first code I spotted in Excercise 5 was the missing colon at the end of the for loop. I found it from running a print statement, the SyntaxError was the first to appear. For me personally, I think it shows that my coding instincts are still developing and that I can notice and solve the errors when they are pointed out to me. But fixing errors like the total = sale went right over my head because I do not have the skills yet to catch a bug that does not interrupt the code.
# 2: apply_discount(price, tier) works as a way to calculate the discounted price based on what tier the customer lands in. It's inputs are the original price and the customer's tier, and it returns the discounted price. A colleague can use the function without reading the body because the function name and parameters clearly indicate its purpose and usage.
# 3: I used AI on exercise 5 to help explain the errors in the code. It explained to me in plain english what the code error meant and that helped me to come to a solution for the errors. The AI built my understanding of how to spot bugs from an error line and how to reason about the code logically.

# Exercise 1:

# Define calculate tax function
def calculate_tax(price, rate):
    return price * rate

# Calling the function
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# Exercise 2:

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85  
    elif tier == "silver":
        return price * 0.90  
    elif tier == "bronze":
        return price * 0.95  
    else:
        return price  

# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3:

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold") # used below
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4:

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# Exercise 5:

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # The previous code was incorrectly using = and would overwrite the total instead of adding the current sale to it. To fix this, we use += to add the total plus the current sale.
print(f"Total: ${total}")

count = 0
for sale in sales: # The code did not have a colon, so the error was occuring because Python requires a colon at the end of a for loop declaration. The fix was to add the colon. 
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # i is greater than or equal to the length of the sales list, which will cause an IndexError. The fix is to use < instead of <=.
    print(sales[i])
    i += 1

# Exercise 6:

x = 100 # apple # global

def double_it():
    global x
    # x = 999 # another apple (not the same apple as above) # local
    return x * 2

print(x) # prints the global x before calling double_it()
print(double_it()) # prints double the global x
print(x)  # prints the global x after calling double_it()

# Scope is global for the variable x, as shown by the use of the global keyword inside the double_it function.