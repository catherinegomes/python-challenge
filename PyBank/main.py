import csv, os

file_to_load=os.path.join("Resources","budget_data.csv")
file_to_output=os.path.join("Analysis","budget_analysis.txt")

total_months=0
prev_revenue=0
net_revenue=0
month_of_change=[]
revenue_change_list=[]
greatest_inc=["",0]
greatest_dec=["",99999999999]


with open(file_to_load) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:
        total_months=total_months+1
        net_revenue=int(row["Profit/Losses"])

        revenue_change=int(row["Profit/Losses"])-prev_revenue
        prev_revenue=int(row["Profit/Losses"])
        revenue_change_list=revenue_change_list+[revenue_change]
        month_of_change=month_of_change+[row["Date"]]

# in order to capture the greatest inc/de-crease, update the variable according to the condition set forth
        if revenue_change>greatest_inc[1]:
            greatest_inc[0]=row["Date"]
            greatest_inc[1]=revenue_change

        if revenue_change<greatest_dec[1]:
            greatest_dec[0]=row["Date"]
            greatest_dec[1]=revenue_change

revenue_average=sum(revenue_change_list)/len(revenue_change_list)

output=(
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {net_revenue}\n"
    f"Average Change: {revenue_average}\n"
    f"Greatest Increase in Profits: {greatest_inc[0]} ${greatest_inc[1]}\n"
    f"Greatest Decrease in Profits: {greatest_dec[0]} ${greatest_dec[1]}\n"
)
print(output)

with open(file_to_output, "w") as text_file:
    text_file.write(output)

