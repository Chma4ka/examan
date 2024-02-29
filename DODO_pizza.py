class Pizzeria:
    def __init__(self,name, dough, sauce, toppings, price):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.toppings = toppings
        self.price = price
    def Pizza_preparing(self):
        return f'Местится тесто'
    def Pizza_baking(self):
        return f'Пицца жарится в печке'
    def Pizza_cutting(self):
        return f'Пицца нарезается на 8 кусочков'
    def Pizza_boxing(self):
        return f'Пицца упаковывается'
class PepperoniPizza(Pizzeria):
    def __init__(self):
        super().__init__('Пепперони', "Толстая", "Томатный соус", "Колбаса", "3500тг")
        
class BBQPizza(Pizzeria):
    def __init__(self):
        super().__init__('BBQ пицца', "толстая", "BBQ соус", "курочка", '2500тг')
    def add_topping(self, topping):
        self.toppings = topping

class SeafoodPizza(Pizzeria):
    def __init__(self):
        super().__init__('Морская пицца', "тонкое", "кетчуп", "морепродукты", "4500тг")



class Order:
    def __init__(self):
        self.pizzas = []
    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
    def calculate_total(self):
        return sum(pizza.price for pizza  in self.pizzas)
class Terminal:
    def __init__(self, pizza_1):
        self.pizzas = pizza_1
    def menu(self):
        for index, pizza in enumerate(self.pizzas):
            print(index + 1,'. ', pizza.name, '-', pizza.price)

        empty_list = []
        while True:
            choice = input("Выберите пиццу: ")
            if self.pizzas[int(choice) - 1]:
                print(self.pizzas[int(choice) - 1].name)
                empty_list.append(self.pizzas[int(choice)-1].name)
                print("Хотите заказать еще пиццу\n",'да/нет','?')
                second_choice = input()
                if second_choice == "да":
                    continue
                if choice == 2:
                    
                if second_choice == 'нет':
                    break
        print('Заказ завершен')
        


        # return('Выберите пиццу:\n1. Пепперони - 3500тг\n2. BBQ пицца - 2500тг\n3. Морская пицца - 4500тг')
    def take_order(self, taking_order):
        self.taking_order = taking_order
        return f'Выбрана {taking_order} пицца'
    


if __name__ == "__main__":
    Pizza = Terminal([PepperoniPizza(),BBQPizza(),SeafoodPizza()])
    print(Pizza.menu())