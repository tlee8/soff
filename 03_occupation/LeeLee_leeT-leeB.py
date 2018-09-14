# Team LeeLee - Thomas Lee and Brian Lee
# SoftDev1 pd6
# K06 --  StI/O: DIvine Your Destiny!
# 2018-09-13

import random

d = {}

def read_jobs():
    """
    Return a dictionary containing data on jobs in the US.
    """
    with open("occupations.csv") as csv:
        lines = csv.readlines()
        for line in lines[1:-1]: # Only read lines containing job data
            job_data = parse_csv_line(line)
            job_name = job_data[0]
            job_percentage = float(job_data[1])
            d[job_name] = job_percentage
    return d

def parse_csv_line(line):
    """
    Given a string representing a line in csv, returns a list containing the line's values.
    """
    list = []
    prev_comma_idx = -1
    outside_quotes = True
    for i in range(len(line)):
        char = line[i]
        if char == "\"":
            # Update whether we are inside quotes or not
            outside_quotes = not outside_quotes
        elif char == "\n" or (char == "," and outside_quotes):
            value = line[prev_comma_idx + 1 : i]
            value = value.replace("\"", "") # Remove quotes
            list.append(value)
            prev_comma_idx = i
    return list

def weighted_random():
    """
    Given a list of a dictionary containing keys and its weights,
    return a random key from the dict where the results are weighted by the weights given.
    """

    # Create seperate lists of of the dictionary's keys and values
    k = list(d.keys())
    v = list(d.values())
    v = [i * 10 for i in v]  # Multiply the percentages by 10 to get rid of decimals
    r = random.randint(1,998) # The total sum of percentages is 99.8
    b = 0

    for c in range (len(d)):
        b += v[c] # Increase the bound by the next percentage
        if r <= b:
            return k[c] # If the random number is within a specific range, it will return a specific job

# def test_weighted_random_job():
#    job_dict = read_jobs()
#    for i in range(100):
#        random_job = weighted_random(job_dict)
#        print(random_job)
#
# test_weighted_random_job()

print(read_jobs())
print("-" * 80)
print("Your random occupation is: " + weighted_random())
