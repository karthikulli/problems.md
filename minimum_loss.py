def minimize_loss(prices):
    min_loss = float('inf')
    buy_year = sell_year = -1
    indexed_prices = []
    for year, price in enumerate(prices):
        price=price
        year=year
        indexed_prices.append((price,year))

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            loss = prices[i] - prices[j]
            if loss > 0 and loss < min_loss:
                min_loss = loss
                buy_year = i + 1
                sell_year = j + 1

    if min_loss == float('inf'):
        return "No loss possible"
    return {
        "buy_year": buy_year,
        "sell_year": sell_year,
        "min_loss": min_loss
    }

prices = [20, 15, 7, 2, 13]
print(minimize_loss(prices))
