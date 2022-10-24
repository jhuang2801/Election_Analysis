import csv
import os
# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to the path
file_to_save = os.path.join("analysis", "election_analysis_txt")
# Open the election results and read the file
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
# Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)
# Print each row in the CSV file
#    for row in file_reader:
#        print(row)

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