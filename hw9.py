#Name:
#Class: 5th Hour
#Assignment: HW9

#1. Print Hello World!

#2. Go to the link below and convert the code into pseudocode in comments, then code the flowchart completely:# #https://# dacomputerscience.org/images/content/computer_science/design_and_development/program_design/figures/ada_cs_design_flow_ifelseif.svg

#make a variable called temperature and have it equal a number
#then make if statements that use > and < to determine if its hot cold or mild outside
#have all if statements eventually lead to the print statement "Thank you"

import random

temp = random.randint(1,50)
print("it is" , temp ,"celcuis outside right now")
temp=20
if temp > 20:
    print("its hot")
elif temp == 20:
    print("its mild")
else:
    print("its cold")
print("thank you")
