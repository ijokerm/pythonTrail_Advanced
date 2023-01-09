"""
演示面向对象的多态特性以及抽象类（接口）的使用
"""
# 演示多态的特性
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("汪汪汪")

class Cat(Animal):
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):
    animal.speak()
# 演示多态，使用2个子类对象来调用函数
dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)

# 演示抽象类
class AC:
    def cold_wind(self):
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass
    def swing_lr(self):
        """左右摆风"""
        pass

class Midea_AC(AC):
    def cold_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")

    def swing_lr(self):
        print("美的空调左右摆风")


class GREE_AC(AC):
    def cold_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_lr(self):
        print("格力空调左右摆风")

def make_cool(ac:AC):
    ac.cold_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()
make_cool(midea_ac)
make_cool(gree_ac)