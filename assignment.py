def classify(value):
    if value < 498:
        return "Below range"
    elif 498 <= value <= 502:
        return "In range"
    else:
        return "Above range"
def calculate_average(total,count):  
    return total/count
rice=int(input("Enter the number of rice bags: "))
total_weight=0
below_count=0
in_count=0
above_count=0
for i in range(rice):
    bag_weights=int(input("Enter the rice bag weight:"))
    total_weight += bag_weights
    print(classify(bag_weights))
    if classify(bag_weights) == "Below range":
        below_count +=1
    elif classify(bag_weights) == "In range":
        in_count +=1
    else:
        above_count +=1
average_weight=calculate_average(total_weight,rice)
print(f"Total weight: {total_weight} g")
print(f"Average weight: {average_weight} g")
print(f"Below range: {below_count}")
print(f"In range: {in_count}")
print(f"Above range: {above_count}")