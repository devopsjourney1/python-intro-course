## Getting Started with Python
### Installing Python

Installing Python is simple. Go to [Python.org](https://www.python.org/downloads/) and download the latest version.  Any version above 3+ will work for this course.

If you are using linux, Install python using the command
<div class="file-name"><i class="fas fa-terminal" style="color:#738ADB;"></i>&nbsp;Terminal</div>
```shell
apt-get install python
```

### Python IDLE
Python IDLE (Integrated Development and Learning Environment) is the Python shell.  You can load any Python module or run any Python code while in IDLE. It's great for experimenting and testing your code while you build a script.

Enter the Python IDLE shell by simply calling the Python executable:
<div class="file-name"><i class="fas fa-terminal" style="color:#738ADB;"></i>&nbsp;Terminal</div>
```shell
python
```
You will know you are in the Python shell when you see the three greater-than signs '>>>'.

Once you are in the Python shell try running some python code.  Here are some examples:
<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;Python IDLE</div>
``` python
print("Hellow world!")

1+1

2 * 2
```

Those are all simple one-liners.  Let's move on to a code block.  
<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;Python IDLE</div>
```python
for n in range(100):
    print(n)
```

The above 'for loop' will print out the numbers 0-99. What's important to understand here is the indentation.  With other programming languages, good indentation is a best practice, but with Python, it is required.

### Python Indentation - Tabs or spaces?
Python indentation can use tabs or spaces. Four spaces are equivalent to one tab.  It doesn't matter which one you use, but you must be consistent. Your code will error out if you try to use both tabs and spaces in the same code block.


## Python Package Management
### What is PIP?

Pip is the package manager that comes with python.  There are thousands of python packages that you can download and make use of in your own code.

### Installing Python Packages with Pip

To install a package using pip run the command 'pip install <packagename>'.  The below code installs the pandas module which is a popular package used in Data Science and Machine learning.
<div class="file-name"><i class="fas fa-terminal" style="color:#738ADB;"></i>&nbsp;Terminal</div>
``` shell
pip install pandas
```

## Which Code Editor is best for Python?

### VSCode Editor
When it comes to code editors there are a lot of options, but in my opinion, VSCode is the best one to start out with.  It has a very simple GUI and is very extensible.  According to statistics provided by Github over 60% of developers use VSCode as their preferred code editor in 2020.

VSCode is completely open-source and free to download [https://code.visualstudio.com/](https://code.visualstudio.com/)

### VSCode Recommended Extensions for Python
I recommend using the VSCode extensions following:

- Python
- Material Icon Theme

## Creating and Running Python Scripts

### Creating a Python Script
Python scripts end with the .py extension.  Create a new file called 

<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;myscript.py</div>
```python
print("Hello world")
```

### Running a Python Script
To run a Python script, type python then the script name. Example below.

<div class="file-name"><i class="fas fa-terminal" style="color:#738ADB;"></i>&nbsp;Terminal</div>
```shell
python myscript.py
```

## Variables and the Four Major Python Data Types
### Variables
Before we get into the data types it's good to understand what a variable is. Variables are just containers for storing data values. Here's an example. 
<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;Python IDLE</div>
``` shell
a = 'hello world'
b = 1337
```
In the above example, the variable 'a' contains the string 'hello world' and variable 'b' contains the 'Int' of 1337.

### Strings
In Python, a string is a sequence of characters encapsulated in quotations.  Either " " or ' ' can be used.
### Integeres
Integers are numbers that are not encapsulated in quotations.
### Lists
Lists are an ordered sequence of data.  They contain 'items' which can be any of the other data types.  Lists are contained within square brackets [] and each item is separated by a comma.  An example of a list containing both strings and numbers is below.
<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;Python IDLE</div>
```python
["item1", "item2", 536, 30, "my third string"]
```
### Dictionaries
Dictionaries contain data in key/value pairs, contained within squiggly brackets.
<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;Python IDLE</div>
``` python
{'key1': 'value1', 'key2':'value2'}
```
To reference a value in a dictionary, put the dictionary name followed by the key name.
<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;Python IDLE</div>
```python
mydict['key1']
```
## Continue to Part 2
### Part 2 - Creating a Fortune Telling App
[In Part 2 of this course](/lessons/6/python-course-part-2), we will go over how to create a real-world application. This is a practical real-world example and it's the best way to learn the core skills of Python. [Go to Part 2 now.](/lessons/6/python-course-part-2)