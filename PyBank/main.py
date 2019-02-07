import os
import csv
import sys
#Changes current working directory to file location
os.chdir(os.path.dirname(sys.argv[0]))

#csv relative path
budget_csv = "../Instructions/PyBank/Resources/budget_data.csv"

#checks current working directory
#print(os.getcwd())

#define variables
monthCount = 0
total = 0
previous = 0
current = 0
difference = []
greatestIncrease = ""
greatestDecrease = ""
#read csv with DictReader
with open(budget_csv, "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        current = int(row.get("Profit/Losses"))
        total += current
        if(difference):     
            if((current-previous) > max(difference)):
                greatestIncrease = str(row.get("Date"))
            if((current-previous) < min(difference)):
                greatestDecrease = str(row.get("Date"))
            if(previous != 0):
                difference.append(current-previous)
        else:
            difference.append(current)
        monthCount += 1
        previous = current
#Write the results to a file then print the file out.
finances = "../Instructions/PyBank/Resources/finances.txt"
avgchange = sum(difference)/(monthCount-1)

output = (f"Financial Analysis\n"
        f"-----------------------\n"
        f"Total Months: {monthCount}\n"
        f"Total: {total}\n"
        f"Average Change: {avgchange}\n"
        f"Greatest Increase in Profits: {greatestIncrease} {max(difference)}\n"
        f"Greatest Decrease in Profits: {greatestDecrease} {max(difference)}\n"
        )
print(output)
with open(finances ,"w+") as file:
    file.write(output)




    