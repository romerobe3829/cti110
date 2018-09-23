#This program asks the user to input the number of males and females, calculates and displays the percentages of each gender.
#09/22/2018
#CTI-110 P2HW2 - Male Female Percentage
#Eric Romero Barranco
#
#Pseudocode:
#Input the number of Males in the class
#Input the number of Females in the class
#Calculate the Total amount of students in the class by adding both gender inputs
#Calculate the Males Percentage by dividing the males by total students
#Calculate the Females Percentage by dividing the females by total students
#Display the percentage of Males in class
#Display the percentage of Females in class
#
Males = float(input('Enter the number of Male students in the class: '))
Females = float(input('Enter the number of Female students in the class: '))
Total_Students = Males + Females
Males_Percentage = (Males / Total_Students)
Females_Percentage = (Females / Total_Students)
print ('The percentage of Males in the class is:', format(Males_Percentage, '.0%'))
print ('The percentage of Females in the class is:', format(Females_Percentage, '.0%'))
