import os
import csv

budget_csv = "../Instructions/PyBank/Resources/budget_data.csv"
print(os.getcwd())
#read csv
with open(budget_csv, "r") as csvfile:
    csvreader = csv.DictReader(csvfile)
    print(csvreader)
    monthCount = 0
    sum = 0
    for row in csvreader:
        monthCount += 1




    # temp = None




    # run = "y"
    # while run == "y":
    #     temp = next(csvreader)
    #     if temp == None:
    #         break
    #     else:
    #         sum += int(temp[1])
    #         monthCount += 1
            

    