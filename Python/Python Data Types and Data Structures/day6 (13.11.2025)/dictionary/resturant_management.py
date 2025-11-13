menu={
    "coffee":2,
    "pasta": 3,
    "pizza":5,
    "burger": 6,
    "chicken": 10
}

print("""
Welcome. Please Order Food!

Coffee: $2
Pasta: $3
Pizza: $5
Burger: $6
Chicken: $10
""")

item1=input("Enter item name: ")
total_price=0

if item1 in menu:
    total_price+=menu[item1]
    print(f"you ordered {item1} and price is {total_price}")
else:
    print("invalid")