#!/usr/bin/env python3
# Magic 8 Ball IRC bot
# Created by Lance Brignoni
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import random ####Imports the random code that allows for the user to see the random outcomes
import time #### Imports the allocation for time between prompts
responses = ["Not so sure", "42", "Most likely", "Absolutely not", "Outlook is good", "I see good things happening", "Never",
"Negative", "Could be", "Unclear, ask again", "Yes", "No", "Possible, but not probable"] #### List of all possible responses

## Following function asks user question, then returns random results from responses

#### When the program is run, the code asks the user what the question will be
def answerQuery():
    question = input("Ask and you shall receive: ") #### The first prompt, asks the user for a question
    print("Let me dig deep into the waters of life, and find your answer")
    time.sleep(2) #### Lets time pass between prompts to allow for more mystifying tension
    print("Hmmm")
    time.sleep(2)
    print(random.choice(responses)) #### Prints the random response out of the list
    print("\n")
answerQuery() 

## Following asks user if they would like to play again, and loops until user is finished

#### Allows the user to play the game again without having to run the program again
secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: "))
while secondQuestion == str("Y"):
    answerQuery()
    secondQuestion = (input("Would you like to ask the Wise One another question? Y/N: ")) #### If 'N' is typed, the game is over
else:
    print(input("Press any key to exit")) #### The keybind for exiting the game