#PyPoll

# import Modules
import os
import csv

#declare variables
total_votes = 0
candidates = {}


#Specify file_path to read in the csv.file 
election_csv = os.path.join("resources", "election_data.csv")

# Read in csv. file using CSV module
with open(election_csv) as csvfile:

# CSV reader with delimiter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')

    #Check path works and read work
    #print(csvreader)

    #exclude header from the count of entries.
    #add 1 to the count of votes, as the first row will be counted as 0. 
    #later calculations will need to have the header excluded.
    csv_header = next(csvreader)
    #print(csv_header)

    for row in csvreader:

        #count numnber of votes, which equals nunber of rows.
        #each row representing a voter id with only one vote). 
        #add 1 to account for the first row = 0.
        total_votes = total_votes+1

               
       #set variable to point to row 2 for name of candidates
        candidate = row[2]
       
        if candidate in candidates:
            candidates[candidate] += 1

        #or increment vote for candidates already present in list
        else:
            candidates[candidate] = 1

    #check contents of candidates
    #print(candidates)

        report =[
            'Election Results',
            '--------------------',
            f'Total Votes: {total_votes}',
            '--------------------',
        ]
#Dcalculate the percentage of votes each candidate received
for candidate, vote_count in candidates.items():
    percentage = round(vote_count / total_votes*100,3)
    candidates[candidate] = {'votes': vote_count, 'percentage':percentage}
    report.append(f'{candidate}: {percentage}% ({vote_count})')

  
winner = max(candidates, key=lambda x: candidates[x]['votes'])

report += [
    '--------------------',
    f'winner: {winner}',
    '--------------------'
]

for elect in report:
    print(elect)


#print(winner)

print('Election Results')
print("------------------------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------------------------")
for candidate, data in candidates.items():
    print(f'{candidates}: {data["percentage"]:.3f}% ({data["votes"]})')
print("------------------------------------------")
print(f'winner: {winner}')

#with open('Election_Analysis.txt', 'w') as txtfile:
#Final Print_out to terminal


#Print total number of votes cast:
#print(f'Total Votes: {total_votes}')
#for candidate in candidate_votes:
    #print(candidate)

#for cvandidate in candidate_votes:
    #percentage = candidate_votes[candidate]/total_votes*100
    #print(f'{candidate}:{percentage:.3f}% ({candidate_votes[candidate]})')
#print list of candidastes who received votes
#print()
#check outputs
#print(winner)
#print(candidate_votes)
#print(candidate_name)
#for candidate in candidates:
    #percentage = candidates[candidate] / total_votes * 100

#update winner if current candidate has > votes
#if candidates[candidate] > winner['votes']:
    #winner['name'] = candidate
    #winner['votes'] = candidates[candidate]





#create and output string to make it more convenient to create text file and termial print out.
#output = ''
#output += 'Election Results\n'
#output += '-----------------------------------------\n'
#output += f'Total Votes: {total_votes}\n'
#output += f'----------------------------------------\n'
#output += f'{candidate}: {percentage:.3f}% ({candidates[candidate]})\n'
#output += f'----------------------------------------\n'
#output += f"winner:{winner['name']}\n"
#output += f'----------------------------------------\n'

#print(output)

#with open('election_results.txt', 'w') as summary_file:
    #summary_file.write(output)

    #election_results= os.path.join(os.getcwd(), 'election_analysis.text')
