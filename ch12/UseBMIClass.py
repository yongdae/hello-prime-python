from BMI import BMI


def main():
    bmi = BMI("Yongdae", 39, 89, 185)
    print(bmi.getName(), "의 BMI는", bmi.getBMI(), bmi.getState())

    bmi = BMI("황지수", 43, 51, 162)
    print(bmi.getName(), "의 BMI는", bmi.getBMI(), bmi.getState())

main()