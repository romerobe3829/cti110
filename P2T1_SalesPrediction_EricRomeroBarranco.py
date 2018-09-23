# Creating a program that asks the user to enter the projected amount and display the profit from that amount
# 09/22/2018
# CTI-110 P2T1 - Sales Prediction
# Eric Romero Barranco

# Getting the projected total sales for the year.
total_sales = float(input('Enter the projected annual sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit amount in format.
print ('The profit is $', format(profit, ',.2f'))
