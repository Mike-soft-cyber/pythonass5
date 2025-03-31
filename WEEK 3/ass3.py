def calculate_discount(price, discount_percent):
    if discount_percent >= 0.2:
       print(price * discount_percent)
    else:
        print(price)

original = float(input("Enter the price:"))
discount = float(input("Enter the discount:"))
calculate_discount(original, discount)