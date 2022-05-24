class Customers:
    greeting = "Welcome to Coffee Palace"
    def __init__(self, Name, Beverage, Food, Total):
        self.Name = Name
        self.Beverage = Beverage
        self.Food = Food
        self.Total = Total
        
C_1 = Customers("Nate", "Espresso", "Pastrami on rye", 220)
C_2 = Customers("Elaine", "Strawberry frappuccino", "Tuna wrap", 270)
C_3 = Customers("Samirah", "Iced caffe latte", "Cinnamon roll", 225)
C_4 = Customers("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
C_5 = Customers("Paz", "Iced tea", "Blueberry pancakes", 315)

print(Customers.greeting)
print(C_2.Name)
print(C_2.Beverage)
print(C_2.Food)
print(C_2.Total) 
print(C_4.Name)
print(C_4.Beverage)
print(C_4.Food)
print(C_4.Total)