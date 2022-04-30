# Election_Analysis
  PyPoll project using Python to submit election audit results to the election commission. This program will demonstrate usage of Python to: 
  * create scripts that read csv files
  * write and store data from files or arrays into an external file
  * perform mathematical operations
  * print outputs in two ways

## Deliverables
  The deliverables that this project will seek to bring:
  * Election results printed to terminal
  * Election results written and saved in an external file

#### [The Code](https://github.com/zhangkevq/Election_Analysis/blob/master/PyPoll_Challenge.py)
```
# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_names = []
county_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_count = 0
largest_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county not in county_names:

            # 4b: Add the existing county to the list of counties.
            county_names.append(county)

            # 4c: Begin tracking the county's vote count.
            county_votes[county] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a for loop to get the county from the county dictionary.
    for county in county_votes:

        # 6b: Retrieve the county vote count.
        votes = county_votes[county]

        # 6c: Calculate the percentage of votes for the county.
        vote_percentage = float(votes) / float(total_votes) * 100

         # 6d: Print the county results to the terminal.
        county_election_results = (
            f"{county}: {vote_percentage:.1f}% ({votes:,})\n")
        print(county_election_results)

         # 6e: Save the county votes to a text file.
        txt_file.write(county_election_results)
         # 6f: Write an if statement to determine the winning county and get its vote count.
        if (votes > largest_count) and (vote_percentage > largest_percentage):
            #If true, set winning_count = votes and winning_percentage = vote_percentage
            largest_count = votes
            largest_percentage = vote_percentage
            largest_county = county

    # 7: Print the county with the largest turnout to the terminal.
    county_results = (
        f"\n---------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"---------------------------\n"
    )
    print(county_results, end="")

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(county_results)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
```

  The code above will give us the following output in the terminal and satisfies the first deliverable: 
  ![](https://github.com/zhangkevq/Election_Analysis/blob/master/analysis/election_results_to_terminal.png)
  The terminal output shows the total votes in the election, each candidate's total votes and the percentage of the total votes they received, and the winner of the election plus winning statistics. It also shows conty information for each county and its total vote count, its percentage of total votes, county with largest number of voters. 
  
  For the second deliverable, this output is requested to be written and saved in an [external file](https://github.com/zhangkevq/Election_Analysis/blob/master/analysis/election_analysis.txt). The information saved to the text file is the same as the terminal output above. It has saved: the total votes in the election, each candidate's total votes and percentage of votes, the winner of the election plus statistics, then county results for total votes, percentage of vote split, and largest number of voters.
  
## Election Audit Summary
  Using python to perform this election audit analysis, we find that Diana DeGette is the winner with over 70% of the total votes as well as stats for each county. This script can be used to run any election anywhere because the data output depends on the csv file. The code starts with empty lists/dictionaries/etc. and fills it with whatever is in the csv file. If the csv file has county and votee in different columns, the code can be changed to get the correct column/row information:
  ```
          # Get the candidate name from each row.
        candidate_name = row[i]

        # 3: Extract the county name from each row.
        county = row[j]
        # where i and j are the new column from which candidate/county names are extracted
  ```
In this situation, Ballot ID was not used at all, however there can be a modification to the script that removes any duplicate votes by tracing the Ballot ID similar to how we added candidates and counties to an empty list:
```
 ballot_id = []
 # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county = row[1]

        id = str(row[0])
    
        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

          # Add a vote to that candidate's count
        if id not in ballot_id:
          ballot_id.append(id)
          candidate_votes[candidate_name] += 1
        elif id in ballot_id:
          candidate_votes[candidate_name] += 0
```
The code above is an example modification to segment where the votes are counted for the candidates where it checks if a ballot ID is repeated. If a ballot ID is repeated, then the vote counter does not go up. This example is not perfect, because the ballot ID in different counties could be the same and both be valid, so there would also need to be an addition to the code where it tracks which county the IDs are being taken from. This step could also be performed on the data prior to running this code, however.
