import csv, os, pprint

file_to_load=os.path.join("Resources","election_data.csv")

vote_total=0
candidate_counts={}

with open(file_to_load, "r") as election_data:
    reader = csv.DictReader(election_data,delimiter=",")
    # Headers: Voter ID,County,Candidate
    for row in reader:
        candidate = row["Candidate"]
        if candidate not in candidate_counts.keys():
            candidate_counts[candidate] = 1
        else:
            candidate_counts[candidate] += 1
#   The total number of votes each candidate won
pprint.pprint(candidate_counts)

#   The total number of votes cast
vote_total = sum(candidate_counts.values())
print(vote_total)

#   A complete list of candidates who received votes
conv_candidate_counts = list(candidate_counts)
pprint.pprint(conv_candidate_counts)

#   The percentage of votes each candidate won
Khan_percent = (candidate_counts['Khan']/vote_total)*100
Correy_percent = (candidate_counts['Correy']/vote_total)*100
Li_percent = (candidate_counts['Li']/vote_total)*100
OTooley_percent = (candidate_counts["O'Tooley"]/vote_total)*100
# def percent():
#     print("Khan: "+str(Khan_percent)+" "+str(candidate_counts['Khan']))
#     print("Correy: "+str(Correy_percent)+" "+str(candidate_counts['Correy']))
#     print("Li: "+str(Li_percent)+" "+str(candidate_counts['Li']))
#     print("O'Tooley: "+str(OTooley_percent)+" "+str(candidate_counts["O'Tooley"]))
# print(percent())
    
#   The winner of the election based on popular vote.  
if Khan_percent > (Correy_percent and Li_percent and OTooley_percent):
    print("Khan")
elif Correy_percent > (Khan_percent and Li_percent and OTooley_percent):
    print("Correy")
elif Li_percent > (Khan_percent and Correy_percent and OTooley_percent):
    print("Li")
else:
    print("O'Tooley")

output=(
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {vote_total}\n"
    f"Khan: "+str(Khan_percent)+" "+str(candidate_counts['Khan'])+" \n"
    f"Correy: "+str(Correy_percent)+" "+str(candidate_counts['Correy'])+" \n"
    f"Li: "+str(Li_percent)+" "+str(candidate_counts['Li'])+" \n"
    f"O'Tooley: "+str(OTooley_percent)+" "+str(candidate_counts["O'Tooley"])+" \n"
    f"-------------------------\n"
    f"Winner: Khan\n"
    f"-------------------------\n"    
)
print(output)

file_to_output=os.path.join("Analysis","election_analysis.txt")
with open(file_to_output, "w") as text_file:
    text_file.write(output)