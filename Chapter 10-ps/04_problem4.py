class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square of {self.n} is {self.n ** 2}")
   
    def cube(self):
        print(f"The cube of {self.n} is {self.n ** 3}")
    
    def square_root(self):
        print(f"The square root of {self.n} is {self.n ** 0.5}")
   
    @staticmethod
    def hello():
        print("Hello there! I am a static method.")


a = Calculator(4)
a.hello()
a.square()
a.cube()
a.square_root()