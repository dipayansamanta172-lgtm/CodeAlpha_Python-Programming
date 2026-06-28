
stockPrice = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGLE": 150,
    "AMZN": 170,
    "MSFT": 320
}
totalMoney = 0
print("== Stock Portfolio Tracker ==")
print("Available Stocks: AAPL  TSLA  GOOGLE  AMZN  MSFT")

howMany = int(input("\nHow many different stocks do you want to enter? "))

for i in range(howMany):

    print("\nStock", i + 1)

    stockName = input("Enter Stock Name: ").upper()

    if stockName in stockPrice:

        quantity = int(input("Enter Quantity: "))

        amount = stockPrice[stockName] * quantity

        print("Price of One Share:", stockPrice[stockName])
        print("Total Value:", amount)

        totalMoney = totalMoney + amount

    else:
        print("Stock not found.")

print("\n==============================")
print("Total Investment Value =", totalMoney)

choice = input("\nDo you want to save the result? (yes/no): ")

if choice.lower() == "yes":

    file = open("portfolio.txt", "w")

    file.write("Stock Portfolio Report\n")
    file.write("Total Investment Value = " + str(totalMoney))

    file.close()

    print("Report saved in portfolio.txt")

else:
    print("Report not saved.")