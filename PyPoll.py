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
election_data = open(file_to_load,'r')
#with open(file_to_load) as election_data:
    #To do: perform analysis
    #print(election_data)
    #close the file
#election_data.close()

#filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

#use open() with "w" mode to write data to file
#outfile = open(file_to_save, "w")
with open(file_to_save, 'w') as txt_file:
    #write some data to file
    #outfile.write("Hello World")
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

#close the file
#outfile.close()

#To do: read and analyze the data here
#read the file object with the reader function
file_reader = csv.reader(election_data)
#print header row
headers = next(file_reader)
print(headers)
#print each row in the csv file
#for row in file_reader:
    #print(row)