import csv
import os
print(os.getcwd())

candidates = []
vote_count = 0
candidate_votes = {}
filename = open("Resources/election_data.csv", 'r')
csvreader = csv.reader(filename, delimiter = '\t')
next(csvreader)
for row in csvreader:
    if len(row) != 0:
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] not in candidate_votes.keys():
            candidate_votes[row[2]] = 1
        elif row[2] in candidate_votes.keys():
            candidate_votes[row[2]] += 1
    vote_count += 1 #369711 votes cast
print("Election Results")
print('-' * 20)
print("Total votes: " + str(vote_count))
print('-' * 20)
vote_pct = 0
for i in candidates:
    print(str(i)+":", str(round((candidate_votes[i]/vote_count)*100,3))+"%"+" "+"("+str(candidate_votes[i])+")")
    if (candidate_votes[i]/vote_count)*100 > vote_pct:
        vote_pct = (candidate_votes[i]/vote_count)*100
        winner = i
print('-' * 20)
print("Winner:", winner)
print('-' * 20)

with open("election_results.txt", "w") as f: 
    f.write("Election Results\n")
    f.write('-' * 20 + "\n")
    f.write("Total votes: " + str(vote_count) + "\n")
    f.write('-' * 20 + "\n")
    for i in candidates: 
        f.write(str(i)+": " + str(round((candidate_votes[i]/vote_count)*100,3)) + "%" + " (" + str(candidate_votes[i]) + ")\n")
    f.write('-' * 20 + "\n")
    f.write("Winner: " + winner + "\n")
    f.write('-' * 20 + "\n")
filename.close()



