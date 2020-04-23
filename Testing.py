from abc import ABC, abstractmethod


class AbstractParent(ABC):
    
    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError
    
    def send_to_school(self):
        raise NotImplementedError
    
    def do_work(self):
        print("i`m working")


class Mother(AbstractParent):
    
    def __init__(self, age):
        self.age = age
        print("mother constructor")
    
    def do_house_work(self):
        print("Listening to music")
    
    def send_to_school(self):
        print("Given breakfast and money for a bus")


class Father(AbstractParent):
    
    def __init__(self):
        print("father constructor")
    
    def play_guitar(self):
        print("playing the guitar")
    
    def do_house_work(self):
        print("Sitting on sofa and drinking beer")


class Daughter(Mother, Father):
    
    def hello_friend(self):
        print("hello, my friend")
    
    def __init__(self, age=0):
        Father.__init__(self)
        Mother.__init__(self, age=age)
    
    def do_work(self):
        print("i`m working like a horse")
    
    def __str__(self):
        return "I am %s years old" % self.age


def greet_mother(mother: Mother):
    print("Hello mother")
    mother.do_work()


def greet_father(father: Father):
    print("Hello father")
    father.play_guitar()


if __name__ == '__main__':
    daughter = Daughter()
    
    greet_mother(daughter)
    greet_father(daughter)
    daughter.do_house_work()
    daughters_list = [daughter]
    for x in daughters_list:
        print(x)
    my_set = {1, 1, "smth", 102}
    print(my_set)
    
    my_list = ["first", "second", "third"]
    my_frozenset = frozenset(["uno", "second", "third"])
    my_map = {1: "student", "2": "worker", (1, 2, 3): "why would I ever use this"}
