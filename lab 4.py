# Fractional Knapsack Problem

def max_profit(capacity, weights, profits, objects):
    # Calculating profit to weight ratio
    p_to_w = [p/w for (p, w) in zip(profits, weights)]

    # Making a single item tuple
    items = [(w, p, p_w, o)
             for (w, p, p_w, o) in zip(weights, profits, p_to_w, objects)]

    # Sorting items based on the profit to weight ration in descending order
    items = sorted(items, key=lambda x: x[2], reverse=True)

    cur_capacity = 0
    max_profit = 0

    # Adding items as long as they don't exceed the capacity
    for item in items:
        if cur_capacity+item[0] < capacity:
            cur_capacity += item[0]
            max_profit += item[1]
        else:
            remaing = capacity - cur_capacity
            cur_capacity += remaing
            fraction = remaing/item[0]
            max_profit += (fraction*item[1])
            break

    return max_profit


# Driver Code
if __name__ == "__main__":
    # Taking inputs
    capacity = int(input("Enter Capacity of Knapsack: "))
    weights = list(map(int, input("Enter Weights: ").split(" ")))
    profits = list(map(int, input("Enter Profits: ").split(" ")))
    objects = input("Enter Object Names: ").split(" ")

    print("\nMax profit is", max_profit(capacity, weights, profits, objects))
