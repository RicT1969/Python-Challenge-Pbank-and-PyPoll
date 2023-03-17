# import Modules

import os
import csv

# Specify the csv.file path

budget_csv = os.path.join("Resources", "budget_data.csv")

#set variables (counters to 0) and list
row_count = 0
net_profit = 0
total_change = 0
val_change = 0
prev_profit = None
average_change = 0
cur_profit = 0
max_increase = 0
max_decrease = 0
max_increase_month = ""
max_decrease_month = ""

# Reading using CSV module
with open(budget_csv) as csvfile:

    # CSV reader specifies delimiter and variable that holds content
    csvreader = csv.reader(csvfile, delimiter=',')
  
    #Exclude header from the count of entries.#This means that we will need to add 1 to the count, 
    #as the first row will be counted as 0. This is necessary, as later calculations will need to have the header excluded.
    
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    
       
    for row in csvreader:
        
        #Count number of records. Note - we have excluded the headers, so the count will begin at 0 for the first line. 
        #i.e. 'n' records returns a count of 'n-1'. To get correct count add 1.

        net_profit

        row_count = row_count+1

        #Calulate total profit using the net_profit variable as the counter
        month, net_profit = row[0], int(row[1])
        
        net_profit += int(row[1])

        #calculate the monthly change from the previous row(if it exists) 

               
        cur_profit =  int(row[1])
        if prev_profit is not None:
            val_change = cur_profit - prev_profit
            total_change += val_change

        #print(val_change)
        

        
        if val_change > max_increase:
            max_increase = val_change
            max_increase_month = month
        elif val_change < max_decrease:
            max_decrease = val_change 
            max_decrease_month = month
        prev_profit = cur_profit

average_change = total_change / (row_count -1)
average_change = "{:.2f}".format(average_change)
#print('total change: ', total_change)

#checks for results
#print("Total Months: ", row_count)
#print('Net Profit/Losses: $', net_profit)
#print('average change / month $', average_change)
#print('Greatest Increase in Profits ',max_increase_month,  max_increase)
#print('Greatest Increase in Profits ', max_decrease_month, max_decrease)


#Final Print_out to terminal

print("Financial Analysis")

print("------------------------------------------")

print('Total Months: ', row_count)
print('Total Profit: $', net_profit)
print('Average Change: $', average_change)
print('Greatest Increase in Profits: ', max_increase_month, '($', max_increase,')')
print('Greatest Decrease in Profits: ', max_decrease_month, '($', max_decrease,')')

#Write results to text file
    
with open('Fnancial_Analysis.txt', 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("------------------------------------------\n")
    txtfile.write(f'Total Months: {row_count}\n')
    txtfile.write(f'Total Profit ${net_profit}\n')
    txtfile.write(f'Average Change: ${average_change}\n')
    txtfile.write(f'Greatest Increase in Profits: {max_increase_month} (${max_increase})\n')
    txtfile.write(f'Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n')   
