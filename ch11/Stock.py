class Stock:

    def __init__(self, name, symbol, previousPrice, currentPrice):
        self.name = name
        self.symbol = symbol
        self.previousPrice = previousPrice
        self.currentPrice = currentPrice

    def getName(self):
        return self.name

    def getSymbol(self):
        return self.symbol

    def getPreviousPrice(self):
        return self.previousPrice

    def getCurrentPrice(self):
        return self.currentPrice

    def setPreviousPrice(self, previousPrice):
        self.previousPrice = previousPrice

    def setCurrentPrice(self, currentPrice):
        self.currentPrice = currentPrice

    def getChangePercent(self):
        return format((self.currentPrice - self.previousPrice) * 100 / self.previousPrice, "5.2f") + "%"


def main():
    stock = Stock("Intel Corperation", "INTC", 20500, 20350)

    print("가격 변동률은", stock.getChangePercent(), "입니다.")

main()
