
#Import libraries
import random
import sys
import logging
from scrape import scrape_website

logging.basicConfig(
    format="{asctime} {levelname:<8} {message}",
    style="{",
    level=logging.WARNING,
    stream=sys.stdout,
)

logging.info("Starting fortune app")

#Create a list of fortunes
#filename = 'fortunes.dat'
#with open(filename, 'r') as f:
#    fortunes = f.readlines()
url = 'https://joshmadison.com/2008/04/20/fortune-cookie-fortunes/'
fortunes = scrape_website(url)



#Randomly pick a fortune from the list
def TellFortune():
    fortune = random.choice(fortunes)
    print('*' * 20 + "\nYour fortune is...\n" + fortune + '\n' + '*' * 20)


#Tell first fortune

#Ask the user if they want to play again
while(True):
    TellFortune()
    playagain = input("Do you want to play again?(y/n): ")

    if playagain == 'y':
        print("User chose to play again.")
    else:
        print("User chose to exit, exiting application now.")
        logging.info("Exiting")
        sys.exit()