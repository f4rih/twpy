Twpy
========

Twitter High level scraper for humans.


Features
--------
- NO LIMIT, NO API required
- Fast and easy to use
- Working with python 3.6+
- Integrated with pandas for data science research


Installation
--------
Manual install via git :

.. code-block:: bash

    $ git clone https://github.com/0x0ptim0us/twpy.git
    $ cd twpy
    $ python setup.py install


Install using pip:

.. code-block:: bash

    $ pip3 install twpy
    # or
    $ python -m pip install twpy


Usage
--------

Guidance of using Twpy :

.. code-block:: python

    from twpy import TwpyClient
    from twpy.serializers import to_pandas, to_json, to_list

    # create twpy client object
    tc = TwpyClient()

    # get user followers, limited up to 50
    # proxy support available:
    #       example : proxy="127.0.0.1:8080"
    # interval: sleep between each request
    #       example : interval=0 (no sleep)
    followers_data = tc.get_followers(username="elonmusk", limit=50)

    # convert result to pandas data frame, json and list
    # pandas
    pandas_sample = to_pandas(followers_data)
    # json
    json_sample = to_json(followers_data)
    # list
    list_sample = to_list(followers_data)



.. csv-table:: Supported methods
    :header: "method", "description"
    :widths: 20, 40

    "get_followers()", "get user followers"
    "get_friends()", "get user followings/friends"
    "get_timeline()", "get user timeline/tweets"
    "get_user()", "get user profile info"


Meta
----
Fardin Allahverdinazhand - `@0x0ptim0us <https://twitter.com/0x0ptim0us>`_  - 0x0ptim0us@gmail.com
Distributed under the MIT license. see `LICENSE.txt <https://github.com/0x0ptim0us/twpy/blob/master/LICENSE.txt>`_ for more information.

https://github.com/0x0ptim0us/twpy