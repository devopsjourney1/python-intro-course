

## Getting Started with Python
### Installing Python

Installing pythong is simple. Go to [Python.org](https://www.python.org/downloads/) and download the latest version.  Any version above 3+ will work for this course.

If you are using linux, Install python using the command
```shell
apt-get install python
```

### Python IDLE - Integrated Development and Learning Environment

Python IDLE is a python shell.  You can load any Python moduel or run any Python code while in this shell. It is great for expirmenting and testing your code while you build a script.

Enter Python IDLE shell by simply calling the Python executable:
```shell
python
```
You will know you are in the Python shell when you see the three greater then signs '>>>'.

Once you are in the Python shell try running some python code.  Here's some examples:
``` python
print("Hellow world!")

1+1

2 * 2
```

Those are all simple one liners.  Let's move on to a code block.  

```
for n in range(100):
    print(n)
```

The above 'for loop' will print out the numbers 0-99. What's important to understand here is the indentation.  With other programming languages good indentation is a best practice, but with python it is required.

### Python Indentation - Tabs or spaces?
Python indentation can use tabs or spaces. Four spaces is the equalivalent to one tab.  It doesn't matter which one you use, but you must be consistent. Your code will error out if you try to use both tabs and spaces in the same code block.


## Installing Python Packages with Pip

Pip is the package manager that comes with python.  There are thousands of python packages that you can download and make use of in your own code.

To install a package using pip run the command 'pip install <packagename>'.  The blow code installs the pandas module which is a popular package used in Data Science and Machine learning.

``` shell
pip install pandas
```

## Which Code Editor is best for Python?

When it comes to code editors there are a lot of options, but in my opinion VSCode is the best one to start out with.  It has a very simple GUI and is very extensible.  Accroding to statistics provided by github over 60% of developers use VS Code as their preferred code editor in 2020.

VS Code is completely open source and free to download https://code.visualstudio.com/

### VS Code Recommended Extensions for Python
I recommond using the VSCode extensions following:

Python
Material Icon Theme

## Creating and Running Python Scripts

### Creating a Python Script
Python scripts end with the .py extension.  Create a new file called 

<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;myscript.py</div>
```python
print("Hello world")
```

### Running a Python Script
Run the script py running

<div class="file-name"><i class="fas fa-terminal" style="color:#738ADB;"></i>&nbsp;Terminal</div>
```shell
python myscript.py
```

## Variables and the Four Major Python Data Types
### Variables
Before we get into the data types it's good to understand what a variable is. Variables are just containers for storing data values. Here's an example. 

``` shell
a = 'hello world'
b = 1337
```
In the above example, the variable a contains the string 'hello world' and variable b contains the 'Int' of 1337.

### Strings
In Python, a string is a sequence of characters encapsulated in quotations.  Either " " or ' ' can be used.
### Integeres
Integeres are numbers that are not encapsualted in quotations.
### Lists
Lists are an ordered sequence of data.  They contain 'items' which can be any of the other data types.  Lists are contained within square brackets [] and each item is seperated by a comma.  An example of a list containing both strings and numbers is below
```python
["item1", "item2", 536, 30, "my third string"]
```
### Dictionaries
Dictionaries contain data in key/value pairs, contained within squiggly brackets.

``` python
{'key1': 'value1', 'key2':'value2'}
```
To reference a value in a dictionary, put the dictionary name followed by the keyname

```python
mydict['key1']
```

## Creating a Python Application from Scratch

### Creating the Script

We will start by creating a script named fortune.py and importing the 'random' library.

### Importing and Exploring Libraries
<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;fortune.py</div>
```python
import random
```
This will allow us to make use of the Python Standard Library "random", which will allow us to randomly pick an item from the list.  We will be importing additional libaries throughout this course as we get into loading files, logging errors and webscraping.

If you want to learn more about a library you can check out the Python documentation or by using the help() or dir() functions.
```python
help(random)
```
help() shows you help information for the module.

```python
dir(random)
```
dir() shows you all the avaialable functions within the library.

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
## Recieving User Input, Flow Control and Functions in Python

### How to use input()

The input() function allows you to take in user input to the user.

The below code will display "Do you want to play again?" to the user and then wait for the user to give input.  It will then assign that user input to the variable 'playagain'
``` python
playagain = input("Do you want to play again?")
```

### The If statement

The if statement checks if a contidion is True, if it is, it will do what's in the code block below, if it is NOT True then it will perform the code underneath 'else'.

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

Functions are re-usable blocks of code that run when they are called.  In our app we are going to define a function "TellFortune()" that randomly selects a fortune when called

``` python
def TellFortune():
    fortune= random.choice(fortunes)
    print(fortune)
```

Now whenever we want our application to tell a fortune, we just call the TellFortune() function.

### While Loops

While loops will continue to loop as long as the condition is true.  Since we want our application to run indefintly, we are creating an infinite while loop.

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
First we assign a variable the filename. 
After that we use the open(filename, 'r').  the 'r' is specifying that we are opening the file in read-only mode. If we wanted to write to the file we would set it to 'w' for write or 'a' to append.
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

By default, only warning errors and above will be displayed, but the threshold can be changed in the logging.basicConfig.

Below is a table of the logging message levels.

|Level|Numeric Value |
| ------------- | ------------- |
| CRITICAL | 50  |
| ERROR  | 40  |
| WARNING | 30
| INFO | 20
| DEBUG |10














