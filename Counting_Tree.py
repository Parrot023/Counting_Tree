
tree = [
    ["B","G",],
    ["B","G","B","G"],
    ["B","G","B","G","B","G","B","G"]
]

goal = "B"
wished_number_of_goal = 2
count = 0
results = 0
total_pos = 8

for i in range(total_pos):

    #resets variables
    number_of_goal = 0
    temp_result = ""

    #goes through each generation
    temp_result += tree[0][(count/2)/2]
    temp_result += tree[1][count/2]
    temp_result += tree[2][count]

    #prints B's and G's from each generation
    print(temp_result)

    #Checks number of B's and G's in each posibility
    for j in range(len(temp_result)):
        if temp_result[j] == goal:
            number_of_goal += 1

    #adds 1 to number of results if the goal was reached
    if number_of_goal >= wished_number_of_goal:
        results += 1

    #adds 1 for each iteration
    count += 1


#prints nhow many times goal was reached
print(results)

#prints fraction off total posibilities
print("chance of getting " + str(wished_number_of_goal) + " " + goal + ": " + str( results) + "/" + str(total_pos))
