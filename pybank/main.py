import os
import csv

#import csv file data
budget_data = os.path.join('budget_data.csv')

#open the file and read it - skip the header line
with open(budget_data, mode = 'r') as csvfile:

    budget = csv.reader(csvfile, delimiter=',')
    next(budget)

#set up some variables
    bigmoney = 0
    months = 0
    firstlist = []
    monthlist = []
    changelist = []

#make a function because why not, it's only being used once
    def changefunction(item):
        length = len(item)
        for x in range(length):
            changelist.append(int(item[x])-int(item[x-1]))
        
        changelist.pop(0)
        changelist.insert(0, 0)

        return None
        
#for loop - grab some numbers, add them up, and put them in a list
    for row in budget:

        firstlist.append(row[1])
       
        bigmoney += int(row[1])
        
        monthlist.append(row[0])
         
        months += 1
    
#apply the single-use function
    changefunction(firstlist)

#zip some lists to make a dictionary
    keys = (changelist)

    values = (monthlist)

    zipdic = dict(zip(keys, values))

#get the display going
    print("FINANCIAL ANALYSIS")

    print("-------------------------------")

    print("Total Months: " + str(months))
    
    print("Total: $" + str(bigmoney)+".00")  
    
    print("Average Change: $" + str(round(int(sum(changelist))/int(len(changelist))))+".00")

    increase = str(max(changelist))

    decrease = str(min(changelist))

    print("Greatest Increase in Profits: " + zipdic[int(increase)] + " $" + increase +".00")

    print("Greatest Decrease in Profits: " + zipdic[int(decrease)] + " $" + decrease +".00")

    f = open("Report.txt","w+")

    f.write("FINANCIAL ANALYSIS\n")

    f.write("-------------------------------\n")

    f.write("Total Months: " + str(months)+"\n")
    
    f.write("Total: $" + str(bigmoney)+".00\n")  
    
    f.write("Average Change: $" + str(round(int(sum(changelist))/int(len(changelist))))+".00\n")

    f.write("Greatest Increase in Profits: " + zipdic[int(increase)] + " $" + increase +".00\n")

    f.write("Greatest Decrease in Profits: " + zipdic[int(decrease)] + " $" + decrease +".00\n")

    f.close()

    os.startfile("Report.txt")

print("done")

#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period