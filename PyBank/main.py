print("Financial Analysis")
print("-----------------------")
 
from datetime import date
from operator import index
import os
import csv
csvpath=os.path.join('budget_data.csv')
with open(csvpath,encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")

with open('budget_data.csv', newline="") as f:
    reader= csv.reader(f)
    data = list(reader)
   
reader = csv.reader(open("budget_data.csv"))
lines = len(list(reader))-1
print(f"Total Months: {lines}")
 
sum = 0
for index, row in enumerate(data):
    if index != 0:
        current = (row[1])
        sum += int(current)
 
 
print(f"Total: {sum}")
 
index = 0
totalchange = 0
for index, row in enumerate(data):
    if(index > 1):
        prevRow = data[index-1]
        x1 = prevRow[1]
        x2 = row[1]
        change = int(x2) - int(x1)
        totalchange = totalchange + change
 
avg_change = totalchange/lines
 
print(f"Average Change: {avg_change}")
 
index = 0
greatest_increase = 0
greatest_increase_index = 0
for index, row in enumerate(data):
    if index != 0:
        current_value = row[1]
        current_value_int = int(current_value)
        if current_value_int > greatest_increase:
            greatest_increase = current_value_int
            greatest_increase_index = index
 
greatest_increase_line_data = data[greatest_increase_index]
greatest_increase_value = greatest_increase_line_data[1]
greatest_increase_date = greatest_increase_line_data[0]
print(greatest_increase_value, greatest_increase_date)
print(f"Greatest Increase In Profits: ")
