# 创建类
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting.")
    def roll_over(self):
        print(self.name.title() + " rolled over")
# 根据类创建实例，并访问属性
my_dog = Dog('willie', 6)
print("Mu dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.sit()
my_dog.roll_over()

class Car():
    # 在inti内指定默认值
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("This car has "+str(self.odometer_reading)+" miles on it")
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")
    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_car = Car('Benz', 'E300',2022)
print(my_car.get_descriptive_name())
# 修改属性的值
my_car.odometer_reading = 10
my_car.read_odometer()
# 类的方法对属性值作用顺序是（先修改，在读取）
my_car.update_odometer(26)
my_car.read_odometer()

my_car.update_odometer(11)
my_car.read_odometer()

my_car.update_odometer(33)
my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()

# 实例中的属性上升到类
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge"
        print(message)

# 继承
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make,model,year)
        self.battery = Battery()

# 子类与父类关联
my_nio = ElectricCar('nio', 'f4', 2019)
print(my_nio.get_descriptive_name())
my_nio.battery.describe_battery()
my_nio.battery.get_range()


