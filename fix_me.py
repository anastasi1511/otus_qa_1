def calculate_average(numbs):
    total = sum(numbs)
    count = len(numbs)
    return total / count


numbs = [10, 15, 20]
result = calculate_average(numbs)
print("The average is:", result)
