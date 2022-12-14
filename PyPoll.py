import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to the path
file_to_save = os.path.join("analysis", "election_analysis.txt")
#1. Initalize a total vote counter.
total_votes = 0
# Candidate optoins
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}
# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
# Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read the header row
    headers = next(file_reader)
# Print each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row [2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
# Save the results to our text file
with open(file_to_save, "w") as txt_file:
#Determine the percentage of votes for each candidate by looping through the counts# Iterate thorugh the candidate list
#Print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes)/float(total_votes)*100
        # Print the candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}%({votes:,})\n")
        #Print each candidate, their vote count, and percentage to the terminal
        print(candidate_results)
        #Save the candidate result to our text file
        txt_file.write(candidate_results)
#    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
# Print the candidate list
#print(candidate_options)
# print the candidate vote dictionary
#print(candidate_votes)
#Determine the winning vote count and candidate
# Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true, then set winning_count = votes and winning_percentage =
            #vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidade's name
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
# Save the winning candidate's name to the text file
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)       
#        print(row)
# 3. Print the total votes
#print(total_votes)
# #Print the file object
#     print(election_data)
# #Create a filename varaible to a direct or indirect path to the file
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# #Use the open statement to open the file as a text file
# outfile = open(file_to_save, "w")
# #Write some data to the file
# outfile.write("Hello World")
# #Close the file
# outfile.close()
# #Create a filename variable to a direct or indirect path to the file
# file_to_save - os.path.join("analysis","election_analysis.txt")
# #Using the with statement open the file as a text file
# with open(file_to_save, "w") as txt_file:
#     #Write some data into the file
#     #txt_file.write("Hello World")
#     #Write three counties to the file.
#     # txt_file.write("Arapahoe, ")
#     # txt_file.write("Denver, ")
#     # txt_file.write("Jefferson")
#     #Write three counties by line
#     # txt_file.write("Arapahoe\nDenver\nJefferson")
#     txt_file.write("Counties in the election\n----------\nArapahoe\nDenver\nJefferson")
