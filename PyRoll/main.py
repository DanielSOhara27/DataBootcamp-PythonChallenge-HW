# Adding Dependendancies
import os
import csv
import pandas as pd

# Setting up filepath using os library
filePath = os.path.join("Resources", "election_data.csv")
df = pd.read_csv(filePath, encoding="ISO-8859-1")
df2 = df['Candidate'].value_counts()

print(f"Election Results\n{'-'*30}\nTotal Votes: {df['Candidate'].count()}\n{'-'*30}\n")
print(df2)
# All unique candidates are


# Setting Global variables used through-out the script,
# PS. we only need one Integer and the rest are Floats
#counter = 0


# Opening election_data.csv file and reading it
#with open(filePath, newline="") as electionData:

    # Reading contents of file
    #csvElection = csv.reader(electionData, delimiter=",")

    # Skipping over headers
    #next(csvElection)

    # Iterating over each row once and doing all the work
    #for electionRow in csvElection:
    #    counter +=1

    #print(f"There are {counter} rows of data + 1 more for headers")