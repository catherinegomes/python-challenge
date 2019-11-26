import csv, os, pprint

file_to_load=os.path.join("Resources","election_data.csv")
file_to_output=os.path.join("Analysis","election_analysis.txt")

vote_total=0
candidate_counts={}
candidate_option=[]
winning_count=0

with open(file_to_load, "r") as election_data:
    reader = csv.DictReader(election_data,delimiter=",")
    # Headers: Voter ID,County,Candidate
    for row in reader:
#   The total number of votes cast
        vote_total= vote_total+1
        candidate = row["Candidate"]
        if candidate not in candidate_option:
            candidate_option.append(candidate)
            candidate_counts[candidate]=0
#   The total number of votes each candidate won
        candidate_counts[candidate] = candidate_counts[candidate]+1

    # ElectionResults = (
    #     f"\n\nElection Results\n"
    #     f"-----------------------\n"
    #     f"Total Votes: {vote_total}\n"
    #     f"-----------------------\n"
    # )
    # print(ElectionResults)

    # with open(file_to_output,"w") as text_file:
    #     text_file.write(ElectionResults)
# Calculate the percentages of votes by Candidate
        for candidate in candidate_counts:
            votes = candidate_counts.get(candidate)
            vote_percentage = float(votes)/float(vote_total)*100
#Detn the winner
            if votes > winning_count:
                winning_count=votes
                winning_candidate=candidate
# Format the Candidate, Percentage and Raw Votes
            voter_output = f"{candidate}: {vote_percentage:.2f}% ({votes})\n"
        #     print(voter_output)

        # text_file.write(voter_output)

        # winning_candidate_summary = (
        #     f"==========================\n"
        #     f"Winner: {winning_candidate}\n"
        #     f"==========================\n")
        # print(winning_candidate_summary)

        # text_file.write(winning_candidate_summary)
with open(file_to_output, "w") as text_file:
    output=(
    f"\n\nElection Results\n"
    f"-----------------------\n"
    f"Total Votes: {vote_total}\n"
    f"-----------------------\n"
    f"{candidate}: {vote_percentage:.2f}% ({votes})\n"
    f"==========================\n"
    f"Winner: {winning_candidate}\n"
    f"==========================\n"
    )
    print(output)
    text_file.write(output)