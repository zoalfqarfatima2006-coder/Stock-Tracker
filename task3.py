# 1. Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 170,
    "MSFT": 320
}

total_investment = 0
portfolio = []

print("=== Simple Stock Tracker ===")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        try:
            qty = int(input("Enter quantity: "))
            value = stock_prices[stock] * qty
            total_investment += value

            portfolio.append((stock, qty, value))

            print(f"{stock}: {qty} shares = {value}$")
        except:
            print("Invalid quantity!")
    else:
        print("Stock not found!")

# 2. Show final result
print("\n=== Portfolio Summary ===")
for item in portfolio:
    print(f"{item[0]} | Qty: {item[1]} | Value: {item[2]}$")

print("\nTotal Investment:", total_investment, "$")

# 3. Optional file saving
save = input("\nDo you want to save result? (yes/no): ").lower()

if save == "yes":
    choice = input("Save as txt or csv? ").lower()

    if choice == "txt":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio Summary\n\n")
            for item in portfolio:
                file.write(f"{item[0]} | Qty: {item[1]} | Value: {item[2]}$\n")
            file.write(f"\nTotal Investment: {total_investment}$")
        print("Saved as portfolio.txt")

    elif choice == "csv":
        with open("portfolio.csv", "w") as file:
            file.write("Stock,Quantity,Value\n")
            for item in portfolio:
                file.write(f"{item[0]},{item[1]},{item[2]}\n")
            file.write(f"\nTOTAL,,{total_investment}")
        print("Saved as portfolio.csv")

    else:
        print("Invalid choice!")