from msilib.schema import Property
class Car:
    def __init__(self, engine_power=None, brand=None, max_speed=None, price=0, owner_name="Unknown"):
        self.__engine_power = engine_power
        self.__brand = brand
        self.__max_speed = max_speed
        self.__price = price
        self.__owner_name = owner_name

    @property
    def engine_power(self):
        return self.__engine_power

    @engine_power.setter
    def engine_power(self, engine_power):
        if engine_power >= 0:
            self.__engine_power = engine_power
        else:
            raise ValueError("Engine power must be a non-negative integer.")

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, max_speed):
        if max_speed >= 0:
            self.__max_speed = max_speed
        else:
            raise ValueError("Max speed must be a non-negative integer.")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price >= 0:
            self.__price = price
        else:
            raise ValueError("Price must be a non-negative integer.")

    @property
    def owner_name(self):
        return self.__owner_name

    @owner_name.setter
    def owner_name(self, owner_name):
        self.__owner_name = owner_name

    def __str__(self):
        return f"Car: {self.__brand}, Power: {self.__engine_power} HP, Max Speed: {self.__max_speed} km/h, Price: {self.__price}, Owner: {self.__owner_name}"

    def __repr__(self):
        return f"Car({self.__engine_power}, '{self.__brand}', {self.__max_speed}, {self.__price}, '{self.__owner_name}')"

    def __del__(self):
        print(f"Car object {self.__brand} destroyed.")

def main():
    car1 = Car(300, "BMW", 290, 50000, "Nazar")
    car2 = Car(350, "Ferrari", 320, 150000, "Vlad")
    car3 = Car()

    print(car1)
    print(car2)
    print(car3)

    print(f"Brand: {car1.brand}, Engine Power: {car1.engine_power} HP, Max Speed: {car1.max_speed} km/h, Price: {car1.price}, Owner: {car1.owner_name}")
    print(f"Brand: {car2.brand}, Engine Power: {car2.engine_power} HP, Max Speed: {car2.max_speed} km/h, Price: {car2.price}, Owner: {car2.owner_name}")
    print(f"Brand: {car3.brand}, Engine Power: {car3.engine_power} HP, Max Speed: {car3.max_speed} km/h, Price: {car3.price}, Owner: {car3.owner_name}")
    print(f"Max speed of {car1.brand}: {car1.max_speed} km/h")
    print(f"Max speed of {car2.brand}: {car2.max_speed} km/h")

main()
