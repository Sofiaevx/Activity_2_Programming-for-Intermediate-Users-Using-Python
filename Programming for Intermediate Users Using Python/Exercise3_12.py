x = 500
if x > 100:
    raise Exception("x is bigger than 100")

try:
    print(variable_1)
except:
    print("variable_1 is not defined")

for i in range(6):
    print("I'm so happy!")

try:
    print(12 * 6)
except:
    print("cannot be performed")
else:
    print("cannot be performed")


best_burger = "Burger King"
number_2_burger = "Mcdonalds"

assert best_burger == "Burger King"
assert number_2_burger == "Mcdonalds"