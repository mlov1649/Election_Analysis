# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Declare Candidate Options List, candidate votes dictionary
candidate_options = []

candidate_votes = {}

candidate_shares = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0



# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for ballot in file_reader:
        # Add to the total vote count.
        total_votes += 1
        
        # Print the candidate name from each row.
        candidate_name = ballot[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates. 
            candidate_options.append(candidate_name)
            #Begin Tracking cthat candidate's vote.
            candidate_votes[candidate_name]=0
       
        # Add count to candidate
        candidate_votes[candidate_name] += 1
        
        
#calculate totals

for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # Calculate the percentage of votes and record it to dictionary.
    
    vote_percentage = (float(votes)/ float(total_votes)) * 100
    candidate_shares[candidate_name] = vote_percentage



    #  To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.

    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
         # If true then set winning_count = votes and winning_percent = vote_percentage.
         winning_count = votes
         winning_percentage = vote_percentage
         # And, set the winning_candidate equal to the candidate's name.
         winning_candidate = candidate_name
    

    
    
    
        
#Print the results
print (f"There was a total of {total_votes} votes.")
print (candidate_options)
print (candidate_votes)
for candidate in candidate_shares:
    print(f"{candidate} received {candidate_shares[candidate]:.1f}% of the vote.")
print(f"The winner of the election is {winning_candidate} with {candidate_shares[winning_candidate]:.0f}% of the votes.")    
