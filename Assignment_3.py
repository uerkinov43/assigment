def replace_value(values, index, new_value):
    values[index] = new_value
    return None
def find_first(values, target):
    for i in range(len(values)):
       if values[i] == target:
        return i
    return -1
def sumarize(values):
   start= (min(values),max(values),sum(values))
   return start
number_of_days=int(input("Enter the number of days: "))
original=[]
for i in range(number_of_days):
   Sleep_time=int(input("Enter the sleep in hours: "))
   original.append(Sleep_time)
updated=original[:]
index=int(input("Enter the index to change: "))
new_time=int(input("Enter the new sleep time:"))
replace_value(updated,index,new_time)
target=int(input("Enter the sleep time for search: "))
first_index = find_first(updated, target)
count=updated.count(target)
start=sumarize(updated)
minimum,maximum,total=start
sorted_list=sorted(updated)
print(f"Original:{original}")
print(f"Updated:{updated}")
print(f"Sorted:{sorted_list}")
print(f"The shortest sleep:{minimum} hours")
print(f"The longest sleep:{maximum} hours")
print(f"Total sleep time: {total} hours")

if first_index == -1:
    print("Target not found")
else:
    print(f"First index of target: {first_index}")

print(f"Matching value {count}")
