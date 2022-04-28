#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

#dependencies
#import datetime
import csv
import os

#use now() to get present time
#now = datetime.datetime.now()
#print("the time right now is ", now)

#CSV
file_to_load = os.path.join('Resources','election_results.csv')
    #open election results and read the file
#election_data = open(file_to_load,'r')
#with open(file_to_load) as election_data:
    #To do: perform analysis
    #print(election_data)
    #close the file
#election_data.close()

#filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

total_votes = 0 #initialize total vote counter
candidate_options = [] #declare empty list
candidate_votes = {} #declare empty dictionary

#use open() with "w" mode to write data to file
#outfile = open(file_to_save, "w")
#with open(file_to_save, 'w') as txt_file:
    #write some data to file
    #outfile.write("Hello World")
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#close the file
#outfile.close()

#To do: read and analyze the data here
#read the file object with the reader function
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read header row
    headers = next(file_reader)
    #print each row in the csv file
    for row in file_reader:
        total_votes += 1 #Add to the total vote count
        candidate_name = row[2] #print candidate name from each row
        #append candidate name to candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0 #set candidate vote count to 0
        candidate_votes[candidate_name] += 1 #add 1 for each time the file is run
#print(total_votes)
#print(candidate_votes)

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Determine the percentage of votes for each candidate by looping through the counts
#iterate through the candidate list
for candidate_name in candidate_votes:
    votes = candidate_votes[candidate_name] #retrieve vote count of a candidate
    vote_percentage = float(votes) / float(total_votes) * 100 #calculate percentage of votes
    #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.") #print candidate name and percentage of votes, modified to 1 decimal spot
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") #print each candidate's name, vote count, and percentage of votes
    #to do: print each candidate's name, vote count, and percentage of votes
    #determine winner and count
    #determine if votes is greater than winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true, set winning_count = votes and winning_percent = vote percent
        winning_count = votes
        winning_percentage = vote_percentage
            #set winning candidate equal to candidate's name
        winning_candidate = candidate_name
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------\n"
    )
print(winning_candidate_summary)