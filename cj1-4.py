class Animal:
    def __init__(self,arms,legs,eyes,tail,furry,name):
        assert isinstance(arms, float), "Length of arms must be a float"
        assert isinstance(legs, float), "Length of legs must be a float"
        assert isinstance(eyes, int), "Number of eyes must be an int"
        assert isinstance(tail, bool), "Please answer with true or false if it has a tail"
        assert isinstance(furry, bool), "Please answer with true or false if its furry"



        self.arms = arms
        self.legs = legs
        self.eyes = eyes
        self.tail = tail
        self.furry = furry
        self.name = name

    def describe(self):
        print(f"This animal's arms are {self.arms} long\n")
        print(f"This animal's legs are {self.legs} long\n")
        print(f"This animal has {self.eyes} many eyes\n")
        print(f"It's {self.tail} that this animal has a tail\n")
        print(f"It's {self.furry} that this animal is furry\n")
        print(f"This animal is a {self.name}!\n")


favorite_animal = Animal(2.5,3.0,4,False,True,"Tarantula")
favorite_animal.describe()