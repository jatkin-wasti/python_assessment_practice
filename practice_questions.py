# Declare a list with numbers 1 to 5 and add 6 at the end of the list
# num_list = [1, 2, 3, 4, 5]
# print(num_list)
# # appending 6 to the end of the list
# num_list.append(6)
# print(num_list)

# Create a tuple with numbers 1 to 5 and add 2.5
# num_tuple = (1, 2, 3, 4, 5)
# print(num_tuple)
# tuples are immutable so we can't add to it without converting it to a list and back again

# Creating a dictionary and changing a value
# num_dict = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
# print(num_dict)
# num_dict["four"] = "four"
# print(num_dict)

# Create a set and output values from it until you output 3
rand_set = {1, 2, 3, 4, 5}
for num in rand_set:
    print(num)
    if num == 3:
        break

