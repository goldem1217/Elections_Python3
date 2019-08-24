#import modules
import os
import pandas as pd 
import csv

#find the file & read it
vote_data = ("vote_data.csv")
vote_df = pd.read_csv(vote_data)

#establish some variables to work with
#The total number of votes cast
vote_total = (vote_df["Voter ID"].count())

#A complete list of candidates who received votes
candidates = (vote_df["Candidate"].unique())
c_list = candidates.tolist()

#Vote counts for each candidate
vote_counts = (vote_df["Candidate"].value_counts())
v_list = vote_counts.tolist()

#Each candidate's votes as a percentage of total votes
p_list = []
for x in v_list:
    p_list.append(round(int(x*100)/int(vote_total)))

#make a dictionary and convert it to a dataframe
dic = {"Candidate Name":c_list, "Percentage of Total Votes":p_list, "Number of Votes":v_list}
results_df = pd.DataFrame(dic)

#declare a winner
most_votes = (max(v_list))
for index, row in results_df.iterrows():
    if row[2] == int(most_votes):
        winner = str(row[0])

#print results in command line
print("ELECTION RESULTS:")
print("---------------------------------------------------------------------------------")
print("Total Votes: " + str(vote_total))
print("---------------------------------------------------------------------------------")
print (results_df.to_string(index=False))
print("---------------------------------------------------------------------------------")
print(str(winner) + " has won the election.")
print("---------------------------------------------------------------------------------")

#make and open a text file with the results
f = open("Report.txt","w+")
f.write("ELECTION RESULTS:\n")
f.write("---------------------------------------------------------------------------------\n")
f.write("Total Votes: " + str(vote_total)+"\n")
f.write("---------------------------------------------------------------------------------\n")
f.write(results_df.to_string(index=False)+"\n")
f.write("---------------------------------------------------------------------------------\n")
f.write(str(winner) + " has won the election.\n")
f.write("---------------------------------------------------------------------------------\n")
f.close()
os.startfile("Report.txt")