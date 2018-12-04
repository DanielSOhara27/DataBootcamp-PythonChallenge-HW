# Adding Dependendancies
import os
import csv

# Setting up filepath using os library
filePath = os.path.join("Resources", "budget_data.csv")

# Setting Global variables used through-out the script,
# PS. we only need one Integer and the rest are Floats
totalMonths = 0
totalChangeProfit = 0.0
netProfit = 0.0
avgProfitChange = 0.0
maxProfitIncrease = ['N/A', -1]
maxProfitDecrease = ['N/A', 1]
previousPeriodMoney = 0.0


# Function that will keep track of the total change in Profit
# this will later be used to calculate the average. This will
# also help identify the max +/- change if Profit
def calcChangeProfit(currPeriod):

    # Declaring global variables locally to save the results
    global totalChangeProfit
    global maxProfitIncrease
    global maxProfitDecrease
    global netProfit
    global previousPeriodMoney

    # Step 0: setting up local variables
    currPeriodMoney = float(currPeriod[1])

    # Step 1: updating netProfit
    netProfit += currPeriodMoney


    # Step 2: Getting change in profit
    auxChange = currPeriodMoney - previousPeriodMoney


    # Step 3: Updating totalChangeProfit variable
    if totalMonths != 0:
        totalChangeProfit += auxChange


    # Step 4: Updating Max Profit Gain/Loss variables
    if (currPeriodMoney < 0) & (maxProfitDecrease[1] > auxChange):
        maxProfitDecrease[0] = currPeriod[0]
        maxProfitDecrease[1] = auxChange

    elif (currPeriodMoney > 0) & (maxProfitIncrease[1] < auxChange):
        maxProfitIncrease[0] = currPeriod[0]
        maxProfitIncrease[1] = auxChange

    # Step 5 updating previous period money as a variable
    previousPeriodMoney = currPeriodMoney


# --------- THIS IS THE END OF THE calChangeProfit FUNCTION --------

# ----- THIS IS THE START OF THE PYTHON SCRIPT EXECUTABLE SECTION -----

# Opening budget_data.csv file and reading it
with open(filePath, newline="") as budgetData:

    # Reading contents of file
    csvBudget = csv.reader(budgetData, delimiter=",")

    # Skipping over headers
    next(csvBudget)

    # Iterating over each row once and performing all operations
    for budgetRow in csvBudget:
        calcChangeProfit(budgetRow)
        totalMonths +=1


    # Once we are done iterating over all the file we prepare the
    outputList = list()
    outputList.append("Financial Analysis")
    outputList.append('-'*30)
    outputList.append(f"Total Months: {totalMonths}")
    outputList.append(f"Total: ${netProfit}")
    outputList.append(f"Average Change: ${(totalChangeProfit/(totalMonths-1))}")
    outputList.append(f"Greatest Increase in Profits: {maxProfitIncrease[0]} (${maxProfitIncrease[1]})")
    outputList.append(f"Greatest Decrease in Profits: {maxProfitDecrease[0]} (${maxProfitDecrease[1]})")

    # Printing results to terminal
    for x in outputList:
        print(x)


with open("Output_budget_data.txt", "w+") as outputFile:
    outputFile.writelines("%s\n" %line for line in outputList)
