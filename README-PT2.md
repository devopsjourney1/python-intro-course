## Creating a Python Application from Scratch

### Creating the Script

We will start by creating a script named fortune.py and importing the 'random' library.

### Importing and Exploring Libraries
<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;fortune.py</div>
```python
import random
```
This will allow us to make use of the Python Standard Library "random", which will allow us to randomly pick an item from a list.  We will be importing additional libraries throughout this course as we get into loading files, logging errors, and web scraping.

If you want to learn more about a library you can check out the Python documentation or by using the help() or dir() functions.
```python
#shows you help information for the module.
help(random)
```

```python
#shows you all the available functions within the library.
dir(random)
```


### Choosing a Random Item from a List

With the dir() function we have found a good candidate for how to pick a random item for a list.  We will use random.choice.

``` python
fortunes = ['A beautiful, smart, and loving person will be coming into your life.',
'A dubious friend may be an enemy in camouflage.',
'A faithful friend is a strong defense.']
random.choice(fortunes)
```
The above code defines a list of three fortunes, then randomly chooses between them.

If you want to print the output to the user, you will have to wrap the random.choice() function into a print statement as per below

``` python
print(random.choice(fortunes))
```
## Receiving User Input, Flow Control, and Functions in Python

### How to use input()

The input() function allows you to take standard input from the user.

The below code will display "Do you want to play again?" to the user and then wait for the user to give input.  It will then assign that user input to the variable 'playagain'
``` python
playagain = input("Do you want to play again?")
```

### The If statement

The if statement checks if a condition is True, if it is, it will do what's in the code block below, if it is NOT True then it will perform the code underneath 'else'.

```python
import sys

playagain = input("Do you want to play again?")

if playagain == 'y':
    print("User chose to play again.")
else:
    print("User chose to exit, exiting application now.")
    logging.info("Exiting")
    sys.exit()
```

### Functions

Functions are reusable blocks of code that run when they are called.  In our app we are going to define a function "TellFortune()" that randomly selects a fortune when called

``` python
def TellFortune():
    fortune= random.choice(fortunes)
    print(fortune)
```

Now whenever we want our application to tell a fortune, we just call the TellFortune() function.

### While Loops

While loops will continue to loop as long as the condition is true.  Since we want our application to run indefinitely, we are creating an infinite while loop.

``` python
while(True):
    TellFortune()
    playagain = input("Do you want to play again?(y/n): ")

    if playagain == 'y':
        print("User chose to play again.")
    else:
        print("User chose to exit, exiting application now.")
        logging.info("Exiting")
        sys.exit()
```

## Opening files in Python
### Reading in Data from Files

Reading data from files in a common task in Python.

``` python
filename = 'fortunes.dat'
with open(filename, 'r') as f:
    fortunes = f.readlines()
```
To break this down:
First, we assign a variable to the filename. 
After that, we use open(filename, 'r').  the 'r' is specifying that we are opening the file in read-only mode. If we wanted to write to the file we would set it to 'w' for write or 'a' to append.
After the file is opened, we read in the data using readlines() and assign it to the variable fortunes.

## Logging with Python

Logging is one of the easiest things to implement in a python application and it makes debugging your code so much easier.

To enable logging, simply import the logging library and then start using the logging commands. Below is the logging configuration I use for most of my Python applications.
``` python
import logging

logging.basicConfig(
    format="{asctime} {levelname:<8} {message}",
    style="{",
    level=logging.WARNING,
    stream=sys.stdout,
)
```

To log a message, use one of the logging messages below
```python
import logging

logging.critical('This is a critical level msg!')
logging.error('This is a error level msg!')
logging.warning('This is a warning level msg!')
logging.info('This is a info level msg!')
logging.debug('This is a debug level msg!')
```

By default, only warning errors and above will be displayed, but the threshold can be changed in logging.basicConfig().

Below is a table of the logging message levels.

|Level|Numeric Value |
| ------------- | ------------- |
| CRITICAL | 50  |
| ERROR  | 40  |
| WARNING | 30
| INFO | 20
| DEBUG |10


## Continue to Part Part3
### Part 3 - Web-Scrapping with Python
[In Part 3 of this course, we will go over how to implement web-scrapping.](/lessons/7/python-course-part-3)