# Sets: no duplicates allowed
# Can not access index in set like this: my_set[0]
my_set = {1, 2, 3, 1}

# Add in set
my_set.add(54)
print(my_set)


# Remove an element from set. But will give error if element is not in the set. Use discard to overcome this
my_set.remove(1)
my_set.discard(99)
print(my_set)

# Remove random element from set
my_set.pop()
print(my_set)
