shipping_method = input("What shipping method would you like? \n Ground Shipping \n Ground Shipping Premium \n Drone Shipping ")
weight = input("How many pounds is your package? ")

print(f"You choose {shipping_method} for delivery of a {weight}lbs package. Is this correct?")
decision = input("Yes or No")


#Ground Shipping
def ground_shipping(weight):
  if weight <= 2:
    price = (weight * 1.50) + 20
    print(f"The cost of Ground Shipping with a package weight of {weight}lbs is ${price}.")
  elif weight > 2 and weight <= 6:
    price = (weight * 3.00) + 20
    print(f"The cost of Ground Shipping with a package weight of {weight}lbs is ${price}.")
  elif weight > 6 and weight <= 10:
    price = (weight * 4.00) + 20
    print(f"The cost of Ground Shipping with a package weight of {weight}lbs is ${price}.")
  elif weight > 10:
    price = (weight * 4.75) + 20
    print(f"The cost of Ground Shipping with a package weight of {weight}lbs is ${price}.")
  else:
    print("Please enter a valid weight.")

#print(ground_shipping(weight))


ground_shipping_premium = 125.00

def drone_shipping(weight):
  if weight <= 2:
    price = (weight * 4.50) + 0
    rounded_price = round(price, 2)
    print(f"The cost of Drone Shipping with a package weight of {weight}lbs is ${rounded_price}.")
  elif weight > 2 and weight <= 6:
    price = (weight * 9.00) + 0
    rounded_price = round(price, 2)
    print(f"The cost of Drone Shipping with a package weight of {weight}lbs is ${rounded_price}.")
  elif weight > 6 and weight <= 10:
    price = (weight * 12.00) + 0
    rounded_price = round(price, 2)
    print(f"The cost of Drone Shipping with a package weight of {weight}lbs is ${rounded_price}.")
  elif weight > 10:
    price = (weight * 14.25) + 0
    rounded_price = round(price, 2)
    print(f"The cost of Drone Shipping with a package weight of {weight}lbs is ${rounded_price}.")
  else:
    print("Please enter a valid weight.")

#print(drone_shipping(weight))


def cheapest_method(shipping_method):
  if shipping_method == "Drone Shipping":
    print(drone_shipping(weight))
  elif shipping_method == "Ground Shipping":
    print(ground_shipping(weight))
  elif shipping_method == "Ground Shipping Premium":
    print(f"The cost of Ground Shipping Premium with a package weight of {weight}lbs is {ground_shipping_premium}")
  else:
    print("Please enter a valid shipping method: Drone Shipping, Ground Shipping, or Ground Shipping Premium")


while true:
    if decision == "Yes" or decision == "yes":
        cheapest_method(shipping_method)
    else:
        print("Please enter Yes or No")




