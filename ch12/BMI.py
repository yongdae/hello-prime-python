class BMI:
    def __init__(self, name, age, weight, height):
        self.__name = name
        self.__age = age
        self.__weight = weight
        self.__height = height

    def getBMI(self):
        bmi = self.__weight / self.__height * self.__height

        return round(bmi * 100) / 100

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getWeight(self):
        return self.__weight

    def getHeigth(self):
        return self.__height

    def getState(self):
        bmi = self.getBMI()
        if bmi < 18.5:
            return "저체중"
        elif bmi < 25:
            return "정상"
        elif bmi < 30:
            return "과체중"
        else:
            return "비만"
