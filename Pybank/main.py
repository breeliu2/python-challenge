import csv
import os

# path for data
csvpath = os.path.join("Resources", "budget_data.csv")
csvpath_results = open("budget_data.txt", "w")

# Variables definition
total_months = 0
total_profit_loss = 0
prev_profit_loss = 0
profit_loss_change = 0
monthly_changes = []
max_increase = 0
max_decrease = 0

#Open file
with open(csvpath, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter= ",")
    header = next(reader)
    first_row = next(reader)
    total_months = total_months + 1
    prev_profit_loss = int(first_row[1])
    total_profit_loss += prev_profit_loss
    budget_list = list(reader)

   

    for row in budget_list: 
        total_months = total_months + 1 
        total_profit_loss += int(row[1])
        profit_loss_change = int(row[1]) - prev_profit_loss
        prev_profit_loss = int(row[1]) 
        monthly_changes += [profit_loss_change]
        if profit_loss_change > max_increase: 
            max_increase = profit_loss_change
        if profit_loss_change < max_decrease:
            max_decrease = profit_loss_change
    max_increase_month = monthly_changes.index(max_increase)
    max_decrease_month = monthly_changes.index(max_decrease)

       
    
    profit_loss_average = round(sum(monthly_changes)/len(monthly_changes), 2)
        
    print(total_profit_loss)
    print(total_months)
    print(profit_loss_average)
    print(budget_list[max_increase_month -1][0], max_increase)
    print(budget_list[max_decrease_month -1][0], max_decrease)
   
    csvpath_results.write(f'Financial Analysis\n----------------\n')
    csvpath_results.write(f'Profit: ${total_profit_loss}\n')
    csvpath_results.write(f'Total Months: {total_months}\n')
    csvpath_results.write(f'Average P/L: ${profit_loss_average}\n')
    csvpath_results.write(f'Greatest Increase in Profits: ${budget_list[max_increase_month -1][0]}, {max_increase}\n')
    csvpath_results.write(f'Greatest Increase in Profits: ${budget_list[max_decrease_month -1][0]}, {max_decrease}\n')
    
