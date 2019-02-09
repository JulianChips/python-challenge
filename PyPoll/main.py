import os
import csv
import sys
#Changes current working directory to file location
os.chdir(os.path.dirname(sys.argv[0]))

#csv relative path
election_csv = "../Files/PyPoll/election_data.csv"

#define variables
voting = {}
voteCounts = 0

#read csv
with open(election_csv,"r") as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ',')
    header = next(csvreader)
    
    for row in csvreader:
        voteCounts += 1
        if (voting.__contains__(row[2])):
            voting[row[2]] += 1
        else:
            voting[row[2]] = 1

#store results in variables
# candidates = voting.keys()
# percentages = [voting[candidates[i]]/voteCounts for i in candidates]
output = (f"Election Results: \n"
    f"--------------------------\n"
    f"Total Votes: {voteCounts}\n"
    f"--------------------------\n"
)
#iterate through dictionary adding onto the output the individual results of each candidate and choose the winner
winner = ""
for candidate in voting:
    output = output+ f"{candidate}: {100*voting[candidate]/voteCounts: .{6}}% ({voting[candidate]})\n"
    if(winner == ""):
        winner = candidate
    elif(voting[candidate]>voting[winner]):
        winner = candidate
#append the winner
output = output + (f"--------------------------\n"
    f"Winner: {winner}\n"
    f"--------------------------\n"
)
#write to a file and print
resultFile = "../Files/PyPoll/results.txt"
with open(resultFile,"w") as file:
    file.write(output)

print(output)


