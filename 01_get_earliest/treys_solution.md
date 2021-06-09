This exercise can be solved in a number of ways. The first thing we need to do is somehow separate out the MM/DD/YYYY components of the strings. We could:

Slice the string to grab each part
Split the string on the "/" character
Use a regular expression to grab each part
Once we've separated out the month, day, and year we need some way to compare these parts to determine which date string is the earliest one. We could:

Create a series of if-elif-else statements to compare the years, then the months, then the days in order
Rearrange each MM/DD/YYYY-formatted string into YYYYMMDD and compare them
Create (YYYY, MM, DD) tuples from each of the strings and compare them
Let's take a look at some actual solutions.

Here's an answer that uses a series of if-elif-else statements and string slicing:
```
def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    if date1[6:] < date2[6:]:
        return date1
    elif date1[6:] > date2[6:]:
        return date2
    elif date1[:2] < date2[:2]:
        return date1
    elif date1[:2] > date2[:2]:
        return date2
    elif date1[3:5] < date2[3:5]:
        return date1
    elif date1[3:5] > date2[3:5]:
        return date2
    else:
        return date1
```
Notice that this isn't easy to understand. There's a couple reasons for this:

`date1[3:5]`, `date[:2]`, and `date[6:]` aren't very descriptive... they don't really tell you what's being compared
the logic itself is complex... see whether year1 is less, then see whether year2 is less, then see whether month1 is less, then see whether month2 is less, etc.
Let's work on the first problem first by making variable names to describe what we're comparing:

def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    month1 = date1[:2]
    day1 = date1[3:5]
    year1 = date1[6:]
    month2 = date2[:2]
    day2 = date2[3:5]
    year2 = date2[6:]
    if year1 < year2:
        return date1
    elif year1 > year2:
        return date2
    elif month1 < month2:
        return date1
    elif month1 > month2:
        return date2
    elif day1 < day2:
        return date1
    elif day1 > day2:
        return date2
    else:
        return date1
This makes things a little more descriptive, but we still have a complex series of if-elif-else statements. We could join together YYYYMMDD strings to compare to fix that:

def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    month1 = date1[:2]
    day1 = date1[3:5]
    year1 = date1[6:]
    month2 = date2[:2]
    day2 = date2[3:5]
    year2 = date2[6:]
    ymd1 = year1 + month1 + day1
    ymd2 = year2 + month2 + day2
    if ymd1 < ymd2:
        return date1
    else:
        return date2
All that slicing is a little ugly. Let's try option 2 and split these strings on "/":

def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    date1_split = date1.split('/')
    date2_split = date2.split('/')
    month1 = date1_split[0]
    day1 = date1_split[1]
    year1 = date1_split[2]
    month2 = date2_split[0]
    day2 = date2_split[1]
    year2 = date2_split[2]
    ymd1 = year1 + month1 + day1
    ymd2 = year2 + month2 + day2
    if ymd1 < ymd2:
        return date1
    else:
        return date2
Those indexes should be a red flag. Whenever you see manual indexes accesses like date1_string[0] and date1_string[2], you should think of tuple unpacking.

We could use tuple unpacking to make those date variables more easily:

def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    month1, day1, year1 = date1.split('/')
    month2, day2, year2 = date2.split('/')
    ymd1 = year1 + month1 + day1
    ymd2 = year2 + month2 + day2
    if ymd1 < ymd2:
        return date1
    else:
        return date2
That looks much nicer than what we had before. Tuple unpacking really is an amazing feature in Python.

At this point we might consider using tuples to compare year, month, and day instead of using strings. It's a little odd to concatenate strings if we don't care about the string we're making, we just care about the comparison.

def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    m1, d1, y1 = date1.split('/')
    m2, d2, y2 = date2.split('/')
    if (y1, m1, d1) < (y2, m2, d2):
        return date1
    else:
        return date2
Notice I've also shortened things further here by using y1/m1/d1 variable names instead of the more verbose (but more distracting in my opinion) year1/month1/day1.

This solution is my preferred one. Let's talk about a couple more though.

Here's a solution that uses an inline "if" statement:

def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    (m1, d1, y1) = date1.split('/')
    (m2, d2, y2) = date2.split('/')
    return date1 if (y1, m1, d1) < (y2, m2, d2) else date2
Python's inline "if" statements are the same as ternary statements in other languages. So "X if Y else Z" in Python is the same as "Y ? X : Z" in C/Java/Ruby/JavaScript.

I think this inline "if" solution isn't a bad one. I'm often torn on whether to use inline "if" statements versus non-inline "if" statements. This is definitely one of the more sensible cases for using one.

Here's a solution that uses a regular expression:

def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    DATE_RE = re.compile(r'^(\d{2})/(\d{2})/(\d{4})$')
    (m1, d1, y1) = DATE_RE.search(date1).groups()
    (m2, d2, y2) = DATE_RE.search(date2).groups()
    return date1 if (y1, m1, d1) < (y2, m2, d2) else date2
Notice that this answer is a little picker about our inputs. This will fail if the given strings don't consist of two digits, two digits, and four digits with slashes in between them.

Alright let's look at one last solution before we move onto the bonus. This one doesn't actually pass our tests but it's a good one to know about:

def get_earliest(string1, string2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    date1 = datetime.strptime(string1, "%m/%d/%Y")
    date2 = datetime.strptime(string2, "%m/%d/%Y")
    if date1 < date2:
        return string1
    else:
        return string2
This solution that relies on Python's built-in datetime module which can parse our strings into datetime objects for us. This won't meet our needs though because we wanted to allow invalid date strings (like 02/29/2006) and the datetime module requires the date strings to be valid.

Now let's talk about the bonus. If you didn't attempt the bonus for this problem, you may want to stop reading at this point.

Bonus
The bonus required us to allow our get_earliest function to accept any number of dates, provided as positional arguments. We need to split and rearrange each date string to find out which one is the earliest. Fortunately, Python's built-in min function can help us do exactly that. The key is that we need to provide a key keyword argument (that sentence sure had a lot of "key" in it!).

def get_earliest(*dates):
    """Return earliest of given MM/DD/YYYY-formatted date strings."""
    def date_key(date):
        (m, d, y) = date.split('/')
        return (y, m, d)
    return min(dates, key=date_key)
Our key function tells the min function what criteria we'd like to use for determining whether one date string is less than (earlier than) another one. The key function will be called with each date string and the returned date string will be the one with the resulting key tuple which is smallest. If you're not familiar with that * operator, the min built-in, or the optional key argument you can provide to min, you might want to look these things up to use in the future!

To quickly review...

In the the non-bonus, this is the solution that both works and is fairly easy to read:

def get_earliest(date1, date2):
    """Return earliest of two MM/DD/YYYY-formatted date strings."""
    m1, d1, y1 = date1.split('/')
    m2, d2, y2 = date2.split('/')
    if (y1, m1, d1) < (y2, m2, d2):
        return date1
    else:
        return date2
The biggest takeaways I'd like to make sure you get out of this email are:

tuple unpacking (aka multiple assignment) is very powerful
the ability to compare tuples is powerful