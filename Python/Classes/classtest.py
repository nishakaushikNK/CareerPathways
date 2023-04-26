class Cake:
    def __init__(self,flavor,frosting,shape):
        self.flavor = flavor,
        self.frosting = frosting,
        self.shape = shape
    
    def bake(self):
        print(f"Baking the cake for flavor {self.flavor} frosting - {self.frosting} in shape - {self.shape}")
        print("Hello" + "Cake")

# heartCake = Cake("chocolate","white","heart");
# heartCake.bake();

# cakeForMe = Cake("vanilla","pink","round");
# cakeForMe.bake();

class Cookie:
    def __init__(self,flavor,icing):
        self.flavor = flavor,
        self.icing = icing
    
    def bake(self):
        print(f"Baking the cookie for flavor {self.flavor}  in icing - {self.icing}")
   
# cookie1 = Cookie("chocolate","white");
# cookie1.bake();

class Cupcake(Cake):
    def __init__(self,flavor,frosting,shape,topping):
        super().__init__(flavor,frosting,shape)
        self.topping = topping

    def bake(self):
        print(f"Baking the cake for flavor {self.flavor} frosting - {self.frosting} on topping - {self.topping}")

class SugarCookie(Cookie):
    def __init__(self,flavor,icing,sprinkles):
        super().__init__(flavor,icing)
        self.sprinkles = sprinkles

    def bake(self):
        print(f"Baking the cake for flavor {self.flavor} icing - {self.icing} on sprinkles - {self.sprinkles}")

def bake_dessert(dessert):
    dessert.bake()

myCake = Cake("chocolate","vanilla","round");
mycookie = Cookie("chocolate chip","vanilla");

bake_dessert(myCake);
bake_dessert(mycookie);