# Python Band Name Generator 🎸🎶
***Day(1/100) - Project 1 for my #100daysofcode with Python 🐍 challenge***

### <ins>Description:</ins>

This is a band name generator made with Python. 
The program asks the user to enter a city they grew
up in as well as the name of a pet that either they, 
a friend or family member owned. 

The program retruns the two words that were input by
the user using f-strings. 
To make it appear as if the computer is thinking, 
the time module was used to add a few seconds of 
waiting time before the name is generated. 

If the user is happy with the name the program will exit. 
If the user is not happy with the name, the program reads in 
random_words.txt and stores each word in a list. Using the
random package the program then generates two integers and 
concatenates these using f-strings. The random integers are
generated between zero and the length of the list minus 1 to 
avoid any index errors as Python is zero indexed. 

The program will continue to do this until the user is happy
with the generated name. 

#### <ins>What I learnt from this project:</ins>
- Reading in txt files 📃
- using the random package to generate random integers 🔢
- using the time package for the time.sleep() method ⏰

