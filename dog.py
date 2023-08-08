class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def get_info(self):
        print(f"Coat Color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def play_fetch(self):
        print(f"{self.name} is playing fetch!")

    def bark(self):
        print(f"{self.name} is barking loudly!")


class Bulldog(Dog):
    def guard_house(self):
        print(f"{self.name} is guarding the house.")

    def snore(self):
        print(f"{self.name} is snoring loudly.")


def main():
    dog1 = JackRussellTerrier("Jack", 3, "White")
    dog2 = Bulldog("Buddy", 5, "Brown")

    dog1.description()
    dog1.get_info()
    dog1.play_fetch()
    dog1.bark()

    print()

    dog2.description()
    dog2.get_info()
    dog2.guard_house()
    dog2.snore()


if __name__ == "__main__":
    main()
