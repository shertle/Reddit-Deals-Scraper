# Original Author: Sherman Cheung

import praw
import Tkinter
import webbrowser

# TODO
# Add option for choosing how many deals to display

# Create the windows
loginwindow = Tkinter.Tk()
filterwindow = Tkinter.Toplevel()
displaywindow = Tkinter.Toplevel()

# Add window titles
loginwindow.wm_title("Login to Reddit")
filterwindow.wm_title("Choose the deals you want to display")
displaywindow.wm_title("Game Deals")

# Set the login window to the front and hide display window
loginwindow.deiconify()
filterwindow.withdraw()
displaywindow.withdraw()

# Username and Password textvariables
username = Tkinter.StringVar()
password = Tkinter.StringVar()

# Check box variables for each site to filter
amazonvar = Tkinter.IntVar()
bestbuyvar = Tkinter.IntVar()
gamersgatevar = Tkinter.IntVar()
gamestopvar = Tkinter.IntVar()
gogvar = Tkinter.IntVar()
greenmanvar = Tkinter.IntVar()
humblevar = Tkinter.IntVar()
mgsvar = Tkinter.IntVar()
neweggvar = Tkinter.IntVar()
originvar = Tkinter.IntVar()
psnvar = Tkinter.IntVar()
steamvar = Tkinter.IntVar()

# The deal sites we want to search for
search_terms = []

# Have the user login by default
skiplogin = False

# Create Praw Object for parsing reddit
r = praw.Reddit(user_agent="Game Deal Display v0.1")

def nologin():
    """Skip logging in and show filters"""
    global skiplogin
    skiplogin = True
    loginwindow.withdraw()
    filterwindow.deiconify()

def showfilters():
    """Brings up the choices of filters"""
    global skiplogin
    skiplogin = False
    loginwindow.withdraw()
    filterwindow.deiconify()

def getterms():
    """Fills the search_terms list based on which boxes were checked"""
    if int(amazonvar.get()) == 1:
        search_terms.append("[Amazon]")
    if int(bestbuyvar.get()) == 1:
        search_terms.append("[Best Buy]")
    if int(gamersgatevar.get()) == 1:
        search_terms.append("[GamersGate]")
    if int(gamestopvar.get()) == 1:
        search_terms.append("[GameStop]")
    if int(gogvar.get()) == 1:
        search_terms.append("[GOG]")
    if int(greenmanvar.get()) == 1:
        search_terms.append("[GMG]")
        search_terms.append("[Greenmangaming]")
    if int(humblevar.get()) == 1:
        search_terms.append("[HumbleBundle]")
        search_terms.append("[HumbleWeekly]")
    if int(mgsvar.get()) == 1:
        search_terms.append("[MGS]")
        search_terms.append("[MacGameStore]")
    if int(neweggvar.get()) == 1:
        search_terms.append("[Newegg]")
    if int(originvar.get()) == 1:
        search_terms.append("[Origin]")
    if int(psnvar.get()) == 1:
        search_terms.append("[PSN]")
        search_terms.append("[Playstation Store]")
    if int(steamvar.get()) == 1:
        search_terms.append("[Steam]")

def login():
    """Log the user in to Reddit"""
    # Login to reddit for voting
    r.login(str(username.get()), str(password.get()))
    showfilters()


def showdeals():
    """Display the deals selected by the user"""
    # Get the /r/GameDeals subreddit
    subreddit = r.get_subreddit('GameDeals')
    numposts = 25
    gen = subreddit.get_hot(limit=numposts)

    # Set display window to front and hide filter
    filterwindow.withdraw()
    displaywindow.deiconify()

    getterms()

    row = 0

    # Display the information in the window
    for submission in gen:
        title = submission.title

        # Check if the title contains the search term
        has_term = any(string in title for string in search_terms)
        if has_term:
            # Create the button that links to the site
            link = lambda x=submission: webbrowser.open(x.url)
            l = Tkinter.Button(
                    displaywindow, text=title, command=link,
                    wraplength=500, justify="left")
            l.grid(row=row, column=0, sticky="w")

            global skiplogin

            if not skiplogin:
                # Create the upvote button
                up = lambda y=submission: y.upvote()
                u = Tkinter.Button(displaywindow, text="Up Vote", command=up)
                u.grid(row=row, column=1)

                # Create the downvote button
                down = lambda z=submission: z.downvote()
                d = Tkinter.Button(
                    displaywindow, text="Down Vote", command=down)
                d.grid(row=row, column=2)

            row = row + 1

# Create the labels for the username and password
user_label = Tkinter.Label(loginwindow, text="Username")
user_label.grid(row=0, column=0)
pass_label = Tkinter.Label(loginwindow, text="Password")
pass_label.grid(row=1, column=0)

# Create the text boxes for the user to enter info
user_entry = Tkinter.Entry(loginwindow, textvariable=username)
user_entry.grid(row=0, column=1)
pass_entry = Tkinter.Entry(loginwindow, textvariable=password, show="*")
pass_entry.grid(row=1, column=1)

# Create the button to allow the user to login
login_button = Tkinter.Button(loginwindow, text="Login", command=login)
login_button.grid(row=2, column=0)

# Create the button to skip user login
skip_button = Tkinter.Button(
    loginwindow, text="Continue without Login", command=nologin)
skip_button.grid(row=2, column=1)

# Create the go button
go_button = Tkinter.Button(filterwindow, text="Go!", command=showdeals)
go_button.grid(row=6, column=0, sticky="w")

# Create the filter checkboxes
amazon_box = Tkinter.Checkbutton(
    filterwindow, text="Amazon", justify="left", variable=amazonvar,
         width=50)
amazon_box.grid(row=0, column=0, sticky="w")

bestbuy_box = Tkinter.Checkbutton(
    filterwindow, text="Best Buy", justify="left", variable=bestbuyvar,
         width=50)
bestbuy_box.grid(row=1, column=0, sticky="w")

gamersgate_box = Tkinter.Checkbutton(
    filterwindow, text="GamersGate", variable=gamersgatevar,
       justify="left", width=50)
gamersgate_box.grid(row=2, column=0, sticky="w")

gamestop_box = Tkinter.Checkbutton(
    filterwindow, text="GameStop", variable=gamestopvar,
       justify="left", width=50)
gamestop_box.grid(row=3, column=0, sticky="w")

gog_box = Tkinter.Checkbutton(
    filterwindow, text="GOG", justify="left", variable=gogvar,
       width=50)
gog_box.grid(row=4, column=0, sticky="w")

greenman_box = Tkinter.Checkbutton(
    filterwindow, text="GreenManGaming", justify="left", variable=greenmanvar,
         width=50)
greenman_box.grid(row=5, column=0, sticky="w")

humble_box = Tkinter.Checkbutton(
    filterwindow, text="Humble Bundle", variable=humblevar,
       justify="left", width=50)
humble_box.grid(row=0, column=1, sticky="w")

mgs_box = Tkinter.Checkbutton(
    filterwindow, text="Mac Game Store", variable=mgsvar,
       justify="left", width=50)
mgs_box.grid(row=1, column=1, sticky="w")

newegg_box = Tkinter.Checkbutton(
    filterwindow, text="Newegg", variable=neweggvar,
    justify="left", width=50)
newegg_box.grid(row=2, column=1, sticky="w")

origin_box = Tkinter.Checkbutton(
    filterwindow, text="Origin", variable=originvar,
    justify="left", width=50)
origin_box.grid(row=3, column=1, sticky="w")

psn_box = Tkinter.Checkbutton(
    filterwindow, text="PSN", variable=psnvar,
    justify="left", width=50)
psn_box.grid(row=4, column=1, sticky="w")

steam_box = Tkinter.Checkbutton(
    filterwindow, text="Steam", justify="left", variable=steamvar,
       width=50)
steam_box.grid(row=5, column=1, sticky="w")

# Main loop initiates GUI display
Tkinter.mainloop()
