items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# Numbered list
number = 1
for item in items:
    print(str(number) + ". " + item)
    number += 1

# Count names longer than 4 letters
long_count = 0
for item in items:
    if len(item) > 4:
        long_count += 1
print("Items with more than 4 letters:", long_count)

# Longest name, built by hand
longest = items[0]
for item in items:
    if len(item) > len(longest):
        longest = item
print("Longest item:", longest)