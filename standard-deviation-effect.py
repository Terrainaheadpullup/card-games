import random
import statistics

# List for options and empty list for data
options = [1, 0]
data = []

# loop for each probability following the format 1 in k
for k in range(2, 100):
    # loop for each person
    for j in range(1000):
        score = 0
        # loop for whether the person gets the questions correct or not
        for i in range(k * 100):
            choice = random.choice(options)
            if choice == 1:
                score += 1
        # adds the score for each person into the data list
        data.append(score)
    # calculates the standard deviation of the values in the data list
    s_dev = statistics.stdev(data)

    # Opens the file and writes each line in the format [Number of options],[Standard deviation]
    data_standard_dev = open("Standard_Deviations.txt", "a")
    data_standard_dev.write(str(k))
    data_standard_dev.write(",")
    data_standard_dev.write(str(s_dev))
    data_standard_dev.write("\n")

    # adds a 0 to the options list to increase the number of options 1 in k -> 1 in k+1
    options.append(0)