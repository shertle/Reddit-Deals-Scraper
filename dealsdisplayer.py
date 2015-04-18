import praw
import Tkinter
import webbrowser

# Create the windows
loginwindow = Tkinter.Tk()
displaywindow = Tkinter.Tk()

# Add window titles
loginwindow.wm_title("Login to Reddit")
displaywindow.wm_title("Game Deals")

# Set the login window to the front and hide display window
loginwindow.deiconify()
displaywindow.withdraw()

#Username and Password textvariables
username = Tkinter.StringVar()
password = Tkinter.StringVar()

def begin():
    # Create Praw Object for parsing reddit
    r = praw.Reddit(user_agent="Game Deal Display v0.1")

    # Get the /r/GameDeals subreddit
    subreddit = r.get_subreddit('GameDeals')
    numposts = 25
    gen = subreddit.get_hot(limit=numposts)

    # Login to reddit for voting
    r.login(str(username.get()), str(password.get()))

    # Set display window to front and hide login
    loginwindow.withdraw()
    displaywindow.deiconify()

    # The deal sites we want to search for
    search_terms = ["[Steam]", "[Humble Bundle]", "[Humble Store]",
                    "[GMG]", "[GreenManGaming]", "[GamersGate]", "[Amazon]"]

    row = 0

    # Display the information in the window
    for submission in gen:
        title = submission.title

        # Check if the title contains the search term
        has_term = any(string in title for string in search_terms)
        if has_term:
            submission.upvote()
            # Create the button that links to the site
            link = lambda x=submission: webbrowser.open(x.url)
            l = Tkinter.Button(displaywindow, text=title, command=link,
                               wraplength=500, justify="left")
            l.grid(row=row, column=0, sticky="w")

            # Create the upvote button
            up = lambda y=submission: y.upvote()
            u = Tkinter.Button(displaywindow, text="Up Vote", command=up)
            u.grid(row=row, column=1)

            # Create the downvote button
            down = lambda z=submission: z.downvote()
            d = Tkinter.Button(displaywindow, text="Down Vote", command=down)
            d.grid(row=row, column=2)

            row = row + 1

# Create the labels for the username and password
user_label = Tkinter.Label(loginwindow, text = "Username")
user_label.grid(row=0, column=0)
pass_label = Tkinter.Label(loginwindow, text = "Password")
pass_label.grid(row=1, column=0)

# Create the text boxes for the user to enter info
user_entry = Tkinter.Entry(loginwindow, textvariable = username)
user_entry.grid(row=0, column=1 )
pass_entry = Tkinter.Entry(loginwindow, textvariable = password, show="*")
pass_entry.grid(row=1, column=1 )


# Create the button to allow the user to login
login_button = Tkinter.Button(loginwindow, text="Login", command=begin)
login_button.grid(row=2, column=0)

Tkinter.mainloop()
