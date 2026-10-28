# 1. The first bug I noticed was the syntax error. I found it by using the traceback. It tells me that I know where to find an error (via a traceback) and run through possible options to solve it. 
# 2. It takes the price and discount tier, figures out what discount to give, and then outputs the discounted price. The inputs are price and tier. It returns a new price after a discount is applied.  
# 3. I used Microsoft Copilot to assist with Exercise 5. I found that it was helpful in explaining some of the less obvious errors (= vs +=). I learned something new to add to my process of bug solving. 

#Exercise 1

# Define calculate tax function 

def calculate_tax(price, rate):
    return price * rate 

# Calling the function 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08) 

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50 

#Exercise 2 


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

# Exercise 3 

# Write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: $ {discounted:.2f}") 
print(f"After Tax: $ {after_tax:.2f}")

#Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

#Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

#Exercise 5

# What i think each bug means: 
# Syntax error simply is lacking a colon. The program cannot move on. 
# Index error: the program might be calling something out of its range. 
# Logic error: the total is not adding up properly. I am not sure why. 

# The fixes:
# Syntax error: I added a colon to the end of the for loop.
# Index error: I changed the while loop to be less than the length of the sales list.
# Logic error: I added a + sign to the total variable in the for loop so it added all the values up.

# Yes. AI seems to be able to help identify and explain the errors. It also seemed to be able to provide guidance in how to fix them when requested. 

# Exercise 6 

x = 100 #apple (global variable)
def double_it():
    x = 999 # another apple (local variable) 
    return x * 2

print(x) 
print(double_it())
print(x) 