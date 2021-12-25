def maximumToys(prices, k):
    # Write your code here
    prices = sorted(prices)
    print(prices)
    sum = 0
    counter = 0
    for i in range(len(prices) - 1):
        if prices[i] + sum <= k:
            sum += prices[i]
            counter += 1
    return counter

p = [1 ,2, 4,3, 5]

print(maximumToys(p, 7))
