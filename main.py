# Main script to be run
import os
import csv

total_votes=0
vote_percentage=[]
cand_votes={}
cand_options=[]
cand_name=[]
cand_results=[]
votes=[]
win_percent=0
winning_count=0
cand_win=""

csvpath = os.path.join('Resources', 'election_data.csv')
file_output=os.path.join('Analysis', 'election_data.txt')

with open(csvpath) as csvfile:
    
# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

# Read the header row first (skip this step if there is now header)
    election_data_header = next(csvreader)
#Count Total Number of Votes
    
    for row in csvreader:
    # Add to the total vote count
        total_votes+=1

        cand_name= row[2]

        if cand_name not in cand_options:
            cand_options.append(cand_name)

            cand_votes[cand_name]=0

        cand_votes[cand_name]+=1

    for cand_name in cand_votes:
        
        votes = cand_votes.get(cand_name)
        
        vote_percentage = round(float(votes) / float(total_votes) * 100 , 2)
        
        cand_results += [(
            f"{cand_name}: {vote_percentage}% ({votes})")]
        
        if (votes > winning_count) and (vote_percentage > win_percent):
            winning_count = votes
            cand_win = cand_name
            win_percent = vote_percentage




#Analysis of Election Results Summary
analysis=(
f"Election Results\n"
f"____________________________\n"
f"Total Votes:{total_votes}\n"
f"{cand_results}\n"
f"____________________________\n"
f"Winner:{cand_win}\n")

#Print the Analysis
print(analysis)
#Export to Text File
with open(file_output, "w") as txt_file:
    txt_file.write(analysis) 