## Web Scraping with Python
### Modules used in Web Scraping

When it comes to basic Web Scraping, two modules are almost always used:

- Requests -- Used to send HTTP requests.

- Beautiful Soup 4 (BS4) -- Used for extracting and parsing HTML data.

These modules aren't installed by default, so you will have to install them first.

<div class="file-name"><i class="fas fa-terminal" style="color:#738ADB;"></i>&nbsp;Terminal</div>
``` shell
pip install requests
pip install BeautifulSoup4
```
Let's create a new script file for this and begin by importing the modules scrape.py

<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;Python</div>
``` python
import requests
from bs4 import BeautifulSoup
```

### Web Scraping Steps
Web scrapping is broken down into four steps:

1. Use the Requests module to gather the data.
2. Use BS4 to parse and navigate the data.
3. ???
4. Profit.

Jokes aside, steps 3 and 4 are what you make of the data you scrape.  Our steps 3 and 4 will be to load the data into our fortune-telling app and tell a fortune to the user.
 
### Using the Request module to get HTML Data

The first thing we need to do is use requests to get the data. Let's define a url and then feed it into requests. We will save our request object to a variable named 'page'.

```python
url = 'https://joshmadison.com/2008/04/20/fortune-cookie-fortunes/'
page = requests.get(url)
```

### Parsing HTML Data with BS4
Per our previous step, 'page' now contains our request object.  There is a lot of data available in this object, but what we are interested in is the content. If you look at page.content you can see the HTML data, but the data is not easy to navigate. Let's feed it into BS4 so it can be parsed.

``` python
soup = BeautifulSoup(page.content, 'html.parser')
```

### Finding Elements within the HTML
We now have a BS4 object named 'soup' which contains our parsed HTML data. Now we need to search the data for the elements we are interested in.

```python
#Find all the UL elements
ul_elements = soup.find_all('ul')

#Finds li items
fortunes = ul_elements[1].find_all('li')
```
In the above code, we found all the data within 'ul' elements, then for ul_elements[1] we found all the 'li' elements within.

### Parsing the Data
We now have the data we want, but it contains the 'li' html tags.  We want to get rid of these, so let's iterate over the data and use get_text() to only get the text from the object.

``` python
#Removes the tags
fortunes_cleaned = []
for fortune in fortunes:
    fortunes_cleaned.append(fortune.get_text())
return fortunes_cleaned
```

We now have the fortunes stored in a cleaned up list named 'fortunes_cleaned'.  Next, we will convert our script to a function, then import that function to our fortune.py application.

## Creating our own Module
### Using our scrape.py as a module

A module allows you to logically organize your code. Grouping related code into it's own script file and then importing it into another one is a common practice with Python.  Let's have a look at how we can do that.

### Converting our code to a function

Let's take the code we have and make it into a function.  This will allow us to re-use our code by just passing in a url variable.

Below shows how the code will look.

<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;scrape.py</div>
``` shell
import requests
from bs4 import BeautifulSoup


def scrape_website(url):
    #Requests pulls html data
    page = requests.get(url)

    #BS4 parses HTML data
    soup = BeautifulSoup(page.content, 'html.parser')

    #Find all the UL elements
    ul_elements = soup.find_all('ul')

    #Finds li items
    fortunes = ul_elements[1].find_all('li')

    #Removes the tags
    fortunes_cleaned = []
    for fortune in fortunes:
        fortunes_cleaned.append(fortune.get_text())
    return fortunes_cleaned()
```

### Importing our Function

Now that our scrape function is created and housed in scrape.py, let's import it into fortune.py and pass it a URL.

<div class="file-name"><i class="fab fa-python" style="color:#738ADB;"></i>&nbsp;fortune.py</div>
``` shell
from scrape import scrape_website

url = 'https://joshmadison.com/2008/04/20/fortune-cookie-fortunes/'
fortunes = scrape_website(url)
```

And that's it!  We are now using the function we defined in scrape.py to scrape the fortunes off of the web.


## Conclusion
### We're done.. What Now?

This concludes our beginner's course on Python. I hope you found the lessons practical and helpful, but this is just the beginning of your Journey. The best learnings don't come from a book or online video but through practical experience.  Go out there and invent your own scripts to automate something to make your daily life easier. Stay thirsty my friends.