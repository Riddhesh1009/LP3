def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratios for each item
    for item in items:
        item['ratio'] = item['value'] / item['weight']

    # Sort items in non-increasing order of value-to-weight ratio
    items.sort(key=lambda x: x['ratio'], reverse=True)

    total_value = 0
    total_weight = 0
    knapsack = []

    for item in items:
        if total_weight + item['weight'] <= capacity:
            # Take the whole item
            knapsack.append(item)
            total_value += item['value']
            total_weight += item['weight']
        else:
            # Take a fraction of the item
            fraction = (capacity - total_weight) / item['weight']
            knapsack.append({'name': item['name'], 'weight': item['weight']*fraction, 'value': item['value']*fraction})
            total_value += item['value']*fraction
            total_weight += item['weight']*fraction
            break

    return knapsack, total_value

# Example Usage
items = [
    {'name': 'item1', 'weight': 10, 'value': 60},
    {'name': 'item2', 'weight': 20, 'value': 100},
    {'name': 'item3', 'weight': 30, 'value': 120},
 {'name': 'item3', 'weight': 30, 'value': 120},

]

capacity = 50

knapsack_items, total_value = fractional_knapsack(items, capacity)

print(f"Selected Items in Knapsack:")
for item in knapsack_items:
    print(f"Item: {item['name']}, Weight: {item['weight']}, Value: {item['value']}")

print(f"Total Value: {total_value}")
