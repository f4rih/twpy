
Twpy
====

![image](https://pepy.tech/badge/twpy) ![image](https://pepy.tech/badge/twpy/week)

Twitter High level scraper for humans.

Features
--------

- NO LIMIT, NO API required
- Fast and easy to use
- Working with python 3.5+
- Integrated with pandas for data science research

Installation
------------

Manual install via git :

```bash
$ git clone https://github.com/0x0ptim0us/twpy.git
$ cd twpy
$ python setup.py install
```

Install using pip:

```bash
$ pip install twpy
# or
$ python -m pip install twpy
```

Usage
-----

Create Twpy object :

```python
from twpy import TwpyClient 

# create twpy client object
tc = TwpyClient()
```

with proxy :

```python
# or you can pass proxy
tc = TwpyClient(proxy="127.0.0.1:8080")
```

Get twpy current version :

```python
tc.__version__
# '1.2.2'
```


Get user followers:

```python
# get user followers, limited up to 50
# interval : delay between each request, default is 0 for no delay
# proxy : send traffic through proxy, default is none
followers_data = tc.get_followers(username="elonmusk", limit=50, interval=1)
```

Get user timeline:

```python
tweets = tc.get_timeline(username="elonmusk", limit=50)
```

Get user profile:

```python
user_info = tc.get_user(username="elonmusk")
```

Convert result object to other data structures :

```python
from twpy.serializers import to_pandas, to_json, to_list
# convert result to pandas data frame, json and list
# pandas
pandas_sample = to_pandas(followers_data)
# json
json_sample = to_json(followers_data)
# list
list_sample = to_list(followers_data)
```

Search example:

```python
# search user tweets until 2015
tweets = tc.search(username="elonmusk", until="2015")

# add limit and interval
tweets = tc.search(username="elonmusk", until="2015", limit=100, interval=1)

# search tweets contains `love` word
tweets = tc.search(query="love", limit=100, interval=1)

# search tweets which contains `love` word and were tweeted since 2015-01-01
tweets = tc.search(query="love", since="2015-01-01", limit=10)
```

  # Supported methods
| method | description |
|--|--|
| get_friends() | get user followings/friends |
| get_timeline()  | get user timeline/tweets |
| get_user() | get user profile info |
| search() | search tweets with query and username |

Meta
----

Fardin Allahverdinazhand -  [\@0x0ptim0us](https://twitter.com/0x0ptim0us) - <0x0ptim0us@gmail.com>  Distributed under the MIT license. see  [LICENSE.txt](https://github.com/0x0ptim0us/twpy/blob/master/LICENSE.txt)
for more information.

<https://github.com/0x0ptim0us/twpy>
