# python_scraping_web
Web scraping with python3 requests and BeautifulSoup

# Installation

```
pip install -r requirements.txt
```

**requirements.txt**
```
requests==2.19.1
beautifulsoup4==4.6.3
```

**requests** module for requesting the url and fetching response and 
**bs4 (beautifulsoup4)** for making web scraping easier.

# Requesting and Souping
Once you have the requirements installed you can simply import and use. For now we will be
requesting the yelp service and playing around with our modules

**requesting_yelp.epy**
```
import requests
from bs4 import BeautifulSoup
```

You can visit [yelp](https://www.yelp.com/) and search for anything in search bar, for 
example we searched for restaurants and it returned back **Best Restaurants in San 
Francisco, CA**

Copy the url from the browser and paste it into your file

**requesting_yelp.epy**
```
url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc=San+Francisco%2C+CA&ns=1"
```

Now requests comes to work. Since we make an GET request with our browser for this url and
we get back all the html response in form of new webpage, we are gonna do the same with 
```requests.get(url)``` and store the result.

**requesting_yelp.epy**
```
response = requests.get(url)
```

Now response contains the returned result from the get request to the url. We can use 
methods on response like, you can actually print response,

```
print(response)
print(response.status_code)
```

run the file 

**cmd**
```
.../python_scraping_web> py requesting_yelp.py
<Response [200]>
200
```

**200**. The HTTP 200 OK success status response code indicates that the request has 
succeeded.

To actually print the whole html that the webpage contains we can print

```
print(response.text)
```

Earlier version of python requests used to print the html from ```response.text``` in ugly 
way but on printing it now we can get the prettified html or we can also use the bs4 module

For that we need to create a BeautifulSoup object by passing in the text returned from the
url,

```
soup = BeautifulSoup(response.text)
print(soup.prettify())

<img height="1" src="https://www.facebook.com/tr?id=102029836881428&amp;ev=PageView&amp;noscript=1" style="display:none" width="1">
   </img>
  </noscript>
  <script>
   (function() {
                var main = null;

                var main=function(){var c=Math.random()+"";var b=c*10000000000000;document.write('<iframe src="https://6372968.fls.doubleclick.net/activityi;src=6372968;type=invmedia;cat=qr3hlsqk;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;ord='+b+'?" width="1" height="1" frameborder="0" style="display:none"></iframe>')};

                if (main === null) {
                    throw 'invalid inline script, missing main declaration.';
                }
                main();
            })();
  </script>
  <noscript>
   <iframe frameborder="0" height="1" src="https://6372968.fls.doubleclick.net/activityi;src=6372968;type=invmedia;cat=qr3hlsqk;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;ord=1?" style="display:none" width="1">
   </iframe>
  </noscript>
 </body>
</html>
```

Resultant html should be something like this in both requests and BeautifulSoup case.

But BeautifulSoup gives us more advanced methods for scraping like the ```find()``` and
```findall()```

**requesting_yelp.py**
```
links = soup.findAll('a')
print(links)

...
<span class="dropdown_label">
                The Netherlands
        </span>
</a>, <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com.tr/" role="menuitem">
<span class="dropdown_label">
                Turkey
        </span>
</a>, <a class="dropdown_link js-dropdown-link" href="https://www.yelp.co.uk/" role="menuitem">
<span class="dropdown_label">
                United Kingdom
        </span>
</a>, <a class="dropdown_link js-dropdown-link" href="https://www.yelp.com/" role="menuitem">
<span class="dropdown_label">
                United States
        </span>
...
```

A lot of links exists so you terminal should be full of links and html tags

We can loop over the links variable and print the individual link

```
for link in links:
	print(link)
```

**On running**
```
...
<a href="/atlanta">Atlanta</a>
<a href="/austin">Austin</a>
<a href="/boston">Boston</a>
<a href="/chicago">Chicago</a>
<a href="/dallas">Dallas</a>
<a href="/denver">Denver</a>
<a href="/detroit">Detroit</a>
<a href="/honolulu">Honolulu</a>
<a href="/houston">Houston</a>
<a href="/la">Los Angeles</a>
<a href="/miami">Miami</a>
<a href="/minneapolis">Minneapolis</a>
<a href="/nyc">New York</a>
<a href="/philadelphia">Philadelphia</a>
<a href="/portland">Portland</a>
<a href="/sacramento">Sacramento</a>
<a href="/san-diego">San Diego</a>
<a href="/sf">San Francisco</a>
<a href="/san-jose">San Jose</a>
<a href="/seattle">Seattle</a>
<a href="/dc">Washington, DC</a>
<a href="/locations">More Cities</a>
<a href="https://yelp.com/about">About</a>
<a href="https://officialblog.yelp.com/">Blog</a>
<a href="https://www.yelp-support.com/?l=en_US">Support</a>
<a href="/static?p=tos">Terms</a>
<a href="http://www.databyacxiom.com" rel="nofollow" target="_blank">Some Data By Acxiom</a>
```

This looks a lot cleaner now.

# Requesting Pages
So far we have requesting a single url. In this section we will be formatting url
to request a different url. 

If you look at the yelp url we used before, you might find at the very bottom that 
there is [pagination](https://whatis.techtarget.com/definition/pagination) being used.

So what we can do is visit another search page say ```2``` page and we find that url 
changed a bit. 

Specifically the url had some new value at last for the ```2``` page which is

```
https://www.yelp.com/search?find_desc=Restaurants&find_loc=los+angeles&start=30
```

You guessed it right 

```
&start=30
```

is what is new in the url, if you have worked with django then you might have used 
pagination somewhere in your templates.

So that means we can actually add this value at the end of the existing url and locate
to another search result page 

Have a look at ```formatting_url.py```

```
import requests
from bs4 import BeautifulSoup

base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc={}"
city = "los angeles"
start = 30

url = base_url.format(city)

second_page = url + '&start=' + str(start)

response = requests.get(third_page)

print(f"STATUS CODE: {response.status_code} FOR {response.url}")

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.findAll('a')
```

We assign 30 value to the start and add it as ```str(start)``` at the end of the url
and name it ```second_page``` and then request that page. We get ```200``` status code

This means that by finding the patterns in url we can request more url.

So what more could be done. We can start a **loop** that would request the urls and
each time increment the start value by ```30```

```
start = 0
for i in range(40):
    url = base_url.format(city)
    url += '&start=' + str(start)
    start += 30
    if start == 270:
        break
    ...
```

Now how do I know that we have to increment by ```30``` well I checked the pattern of
urls by visiting the pages and stop at ```270``` so that we only request 10 pages.
You can use whatever value you want but it should be multiple of ```30```

# Reading Restaurant Title
Now we will be using the previous code that we wrote in ```formatting_url.py``` and 
extract the particular piece of text from the html tags that we need which is the title
of the restaurant from each search page.

Visit the [url](https://www.yelp.com/search?find_desc=Restaurants&find_loc=los+angeles&start=30) and open developers tools
and point at the block of restaurant with title, rating, review etc. and find the
li tag with class ```regular-search-result```

We will be using this class for searching the particular ```li``` tag from the response
using ```BeautifulSoup```

**reading_name.py**
```
import requests
...
info_block = soup.findAll('li', {'class': 'regular-search-result'})
print(info_block)
```

Run the file and you should the whole li tag and its inner tags printed. But we want
to extract the title of the restaurant from each li tag, for that we have to find 
the class used in the title of restaurant

The title is wrapped inside a **anchor** tag with class ```biz-name```

```
info_block = soup.findAll('a', {'class': 'biz-name'})
print(info_block)

count = 0
for info in info_block:
    print(info.text)
    count += 1

print(count)
```

On printing the ```text``` of the html tag we get the title of the restaurant, these are 
not all the title cause some block don't have ```biz-name``` class but we have what we 
need.

# Advanced Extraction
In this section we will be go a little more further and extract the name, address, 
phone-number of the restaurant.

This time we will be looking for the ```div``` tag that has class ```biz-listing-large```
that contains the restaurant details.
