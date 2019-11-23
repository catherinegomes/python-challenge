import csv, os

file_to_load=os.path.join("Resources","election_data.csv")
#file_to_output=os.path.join("Analysis","election_analysis.txt")

vote_total=0
candidate_counts={}

with open(file_to_load, "r") as election_data:
    reader = csv.DictReader(election_data,delimiter=",")
    # Voter ID,County,Candidate
    for row in reader:
        candidate = row["Candidate"]
        if candidate not in candidate_counts.keys():
            candidate_counts[candidate] = 1
        else:
            candidate_counts[candidate] += 1

print(candidate_counts)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# final_votes=sum(list(total_votes[:]))

# output=(
#     f"\nElection Results\n"
#     f"-------------------------\n"
#     f"Total Votes: {to_votes}\n"
#     f"Candidate 1: {perc_cand1}\n"
#     f"Candidate 2: {perc_cand2}\n"
#     f"Candidate 3: {perc_cand3}\n"
#     f"Candidate 4: {perc_cand4}\n"
#     f"-------------------------\n"
#     f"Winner: {}\n"
#     f"-------------------------\n"    
# )
# print(output)

# with open(file_to_output, "w") as text_file:
#     text_file.write(output)