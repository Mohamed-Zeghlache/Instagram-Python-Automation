# Instagram-Python-Automation
in this repository we will see how to Automate posting on Instagram using python and Selenium.

![Instagram-Python-Automation](https://cdn-images-1.medium.com/max/800/1*Mo6sMJc0jGzgIuek7Loqkw.png)

we are gonna dive right into it, but before we get started... if you have Two_factor Authentication turned on in your Instagram account; you need to turn it off for this script to work.

first of all, we are gonna need to import the following packages

``` 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import autoit
import pyperclip
import schedule
from datetime import date
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
```

we will be using selenium and the chrome web Driver to scrape and get through the web pages. and the scheduler to schedule our postings.

if you have not used the chrome web Driver before it will be installed for the first time, but then it will not be installed each time it's executed … it will get the setup from the cache.
we will provide the caption of our posts, and also the path to the images that we will be posting.
in this script, I will be getting the images from a folder and posting them, and then deleting that image from the folder so it will not be used again. but you can just transfer that image to another folder if you don't want to delete it.

``` 
def job():
    filename = next((os.path.join(path, f) for f in os.listdir(path)      if os.path.isfile(os.path.join(path, f))), "default value here")
    post(filename)
```

we will build another function called post which will be using the webdriver and selenium to do the posting on instagram. (of course; after we provide the username and the password of the account that we will be publishing on)
we will install the ChromeWebDriver and define a mobile emulator to work on.


After that, we will just use selenium to go through the web pages and add our information until we end up posting the the selected image.

then, we will use an appschedueler to scheduel our postings for every 5 houres for example.
When you excute this script, it will get an image and post it every fiive hours.
