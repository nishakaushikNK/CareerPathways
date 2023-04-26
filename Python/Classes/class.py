class Cake:
    def __init__(self, flavor, frosting, shape):
        self.flavor = flavor
        self.frosting = frosting
        self.shape = shape

    def bake(self):
        print(f"Baking a {self.shape} {self.flavor} cake with {self.frosting} frosting.")

class Cookie:
    def __init__(self, flavor, shape, icing):
        self.flavor = flavor
        self.shape = shape
        self.icing = icing

    def bake(self):
        print(f"Baking {self.shape} {self.flavor} cookies with {self.icing} icing.")

class Cupcake(Cake):
    def __init__(self, flavor, frosting, shape, topping):
        super().__init__(flavor, frosting, shape)
        self.topping = topping

    def bake(self):
        print(f"Baking a {self.shape} {self.flavor} cupcake with {self.frosting} frosting and {self.topping} topping.")

class SugarCookie(Cookie):
    def __init__(self, flavor, shape, icing, sprinkles):
        super().__init__(flavor, shape, icing)
        self.sprinkles = sprinkles

    def bake(self):
        print(f"Baking {self.shape} {self.flavor} cookies with {self.icing} icing and {self.sprinkles} sprinkles.")

def bake_something(something):
    something.bake()

my_cake = Cake("chocolate", "vanilla", "round")
my_cookie = Cookie("chocolate chip", "round", "chocolate")

bake_something(my_cake)
bake_something(my_cookie)
