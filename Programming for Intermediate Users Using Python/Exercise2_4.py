Flavor = ["Vanilla", "Chocolate", "Strawberry", "Cookies n' Cream", "Bubblegum"]
Toppings = ["Almond", "Banana slices", "Chcolate syrup", "Caramel syrup", "White chocolate chips"]

ice_cream = dict(zip(Flavor, Toppings))
print(ice_cream)

ice_cream["Chocolate"] = "blueberries"
print(ice_cream)

ice_cream.update({"Matcha": "Pistachios", "Ube": "Mango slices"})
print(ice_cream)