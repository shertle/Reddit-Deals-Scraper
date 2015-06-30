# Reddit Deals Scraper
A python script that scrapes deals from Reddit.  Specifically, scrapes deals from r/GameDeals and allows the user to filter multiple distribution sites simultanously, a function that the subreddit currently lacks.  Both the filter and the actual displaying of the deals are GUI-based.  Clicking a deal will link directly to it in the browser.  Optionally, the user may sign in so they can vote on the deals.

Utilizes Tkinter python library as well as PRAW Reddit API.

To run, use the command:
````
python dealsdisplayer.py
````

PRAW can be installed using the command:
````
pip install praw
````
