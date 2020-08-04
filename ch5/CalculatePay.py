# 사용자 입력을 받는다.

name = input("사원 이름을 입력하세요: ")

hours = eval(input("주당 근무시간을 입력하세요: "))
payRate = eval(input("시간당 급여를 입력하세요: "))
withTaxRate = eval(input("원천징수세율을 입력하세요: "))
restTaxRate = eval(input("주민세율을 입력하세요: "))

grossPay = hours * payRate
withTax = grossPay * withTaxRate / 100
restTax = grossPay * restTaxRate / 100
totalDeduction = withTax + restTax
netPay = grossPay - totalDeduction

# 결과를 출력한다.

out = "\n\n사원 이름: " + name + "\n\n"
out += "주당 근무시간: " + str(hours) + "시간 \n"
out += "시간당 급여: " + str(payRate) + "원 \n"
out += "총 급여: " + str(grossPay) + "원 \n"
out += "공제: \n"

out += " 원천징수세: (" + str(withTaxRate) + "%): " + str(withTax) + "원\n"
out += " 주민세: (" + str(restTaxRate) + "%): " + str(restTax) + "원\n"
out += " 총 공제: " + str(totalDeduction) + "원\n"
out += "공제 후 급여: " + str(int(netPay)) + "원\n"

print(out)