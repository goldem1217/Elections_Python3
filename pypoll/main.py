import os
import csv

#get the file
vote_data = os.path.join('vote_data.csv')

#open/read the file
with open(vote_data, mode = 'r') as csvfile:
    vote_csv = csv.reader(csvfile, delimiter=',')
    next(vote_csv)
        
  

    v_total = 0
    candidates = []
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0

    for row in vote_csv:
        v_total += 1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == candidates[0]:
            c1 +=1
        elif row[2] == candidates[1]:
            c2 +=1
        elif row[2] == candidates[2]:
            c3 +=1
        elif row[2] == candidates[3]:
            c4 +=1

    results = [c1, c2, c3, c4]
    
    percents = []
    for x in results:  
        percents.append(round(int((x*100)/v_total)))

    winner = (max(percents))
    dic = dict(zip(percents, candidates))

#print report
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(v_total))
    print("-------------------------")
    
    index = 0
    for x in candidates:
        print(str(candidates[int(index)]) + ": "+ str(percents[int(index)]) + "% ("+ str(results[int(index)]) + ")")
        index += 1
    print("-------------------------")
    print("Winner: " + dic[winner])
    print("-------------------------")

    
    f = open("Report.txt","w+")
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write("Total Votes: " + str(v_total)+"\n")
    f.write("-------------------------\n")
    index = 0
    for x in candidates:
        f.write(str(candidates[int(index)]) + ": "+ str(percents[int(index)]) + "% ("+ str(results[int(index)]) + ")\n")
        index += 1
    f.write("-------------------------\n")
    f.write("Winner: " + dic[winner]+"\n")
    f.write("-------------------------\n")
    f.close()

    os.startfile("Report.txt")

    

    
    
    



#list of candidates
#list of candidate vote totals
#calculate candidate percentages
#declare a winner
#print results
#print results in .txt file

#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
