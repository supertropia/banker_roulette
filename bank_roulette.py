import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

number_random = random.randint(0,4)

print(number_random)
print(f" the bill will pay for : {friends[number_random]}")
print ("elements in the list : " + str(len(friends)))
