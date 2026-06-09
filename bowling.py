
#File:bowling.py
#Description:Calculates a bowler's average and handicap after three games.
#Assignment number:4
#
#Name: Clifford Djan
#STUDENT ID: 2425400968
#Email: 2425400968@live.gctu.edu.gh

#Grader: Augustus Buckman
#Slip days used this assignment: 0
#
#On my honor,Clifford Djan, this programming assignment is my own work
# and i have not provided this code to any other student

import math
name = input("Enter your name: ")
print()

game1 = int(input("Enter Game1: "))
game2 = int(input("Enter game2: "))
game3 = int(input("Enter game3: "))

average = (game1 +  game2 + game3) // 3

handicap = math.floor((200-average) * 80) // 100

print()
print(name + "'s average is: " + str(average))
print(name + "'s handicap is: " + str(handicap))

