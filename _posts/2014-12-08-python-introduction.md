---
title: "Python Introduction!"
date: "2014-12-08"
---

Thank you for attending the brief introduction to Python!

Here are notes and resources to help you continue learning!

[Click here if you still need to get setup!](https://openhatch.org/wiki/PyCon_intro_tutorial_prep#Goal_.231:_set_up_Python "Python Setup")

\[sourcecode language="python"\]\[/sourcecode\]

**From Yesterday:**

**Let's Start Using Python**

This is what we walked through using our REPL (Read, Evaluate, Print, Loop) Any text that looks like...

`this`

or

\[sourcecode language="python"\] if this in this\_list: print this \[/sourcecode\]

can be entered into your REPL (when the terminal has the '>>>' next to the cursor)

**Calculator + - \* /** `2 + 2 2 / 2`

**Floats v. Ints** `1/2` Huh?

Use Floats to get decimals! `1.0/2`

**Assigning and Adding variables** `x = 6` `x + 6` **Print statements** `name = "Tim" print "hello world" print "Your name" print "Hello " + name`

**Concatenation: Type Error Example: Let's read through this error!** `x = 6 name = "Tim" print name + x` Errors will happen, but they can be understood! **Functions: Useful bits of work**

`name = "Tim" len("Hello") -> 1 Argument len(name)`

`name * 10`

_ANY QUESTIONS? Let me know in the comments below!_ How did I know about len? `help(len)`

**COMPARISON**

`1 == 1`

True ->

Boolean

`True == True False == False 1 == False 0 == False`

Truthiness!

Python strives to be readable. 'in' keyword:

`"H" in "Hello"  "z" not in "Hello"`

**MAKING CHOICES** Multi Line statements \[sourcecode language="python"\] if "found" in "Newfoundland" print "Yes" \[/sourcecode\] The stuff indented will be executed. Indentation matters the most to your brain 4 spaces is the standard, but a tab will work as well. Consistency is what matters the most.

**Making choices with if** Condition check What is the current state of something? What condition is met? What state is it in? \[sourcecode language="python"\] Tim = 22 Alfred = 2

if Tim > Alfred: print "Tim is older" else: print "alfred is older" \[/sourcecode\] _Remember your colons ':'_

What if they're the same age? \[sourcecode language="python"\] Tim = 22 Alfred = 22

if Tim > Alfred: print "tim is older" elif Tim == Alfred: print "Same age!" else: print "Alfred is older" \[/sourcecode\] You can pile on these elif statements to build larger conditional checks. Else is the catch all. If none of our 'if' or 'elif' conditions are met else will be executed. Else is not required.

Remember you only get one thing so if multiple conditions are met the first one in the conditional will be executed. You only get one thing!

**LISTS**

New Object Type: A collection of objects! Just as strings were a collection of characters. Lists can be collections of any object!

`my_list = ["a", "b", "c"] my_list my_list[0] my_list[1]  my_list[-1]`

Last element, Always

What does -2 give us?

`my_list[3]`

We know how to read a traceback!

`my_list.append("d")`

New syntax! append is a function that takes "d" as an argument

`my_list.SomeFunction()  len(my_list)`

Two different types of function calls!

Replace something in list -> Mutable Mutable == Can be changed Immutable == Cannot be changed `my_list[0] = "z"`

To find something: `my_list.index("c")`

Check for containment: Does our list contain z? `"z" in my_list "a" in my_list` **Slice Lists** `my_list[0:2] my_list[:3] my_list[2:] my_list[:]  my_string = "Hello world" my_string[:6]` Very similar syntax to manipulating strings `your_list = ["hello", 1, True, -0.5]  names = ["Alfred", "Melinda", "Kramer", "Tobias", "Edmundo"] names.sort() "Alfred" in names  numbers = [3, -5, .6, 1700] max(numbers) min(numbers)`

_To see what objects are available to our REPL_ `dir()`

What do we have going on here with different types of functions?

len() is a thing you do to objects .sort() is something that lists can do to themselves

Lists can be used to read lines out of files, build list from data, and give our data organizational structure to make manipulate and changing data much easier.

LOOPS! Looping over lists

\[sourcecode language="python"\] for name in names: print name \[/sourcecode\] This is a for loop for variable name in list name name is our variable name. It could be anything. Another Example:

\[sourcecode language="python"\] for x in names: print x \[/sourcecode\]

Very machine like, think manufacturing.

\[sourcecode language="python"\] for name in names: print "Hello" + name \[/sourcecode\] THE POWER! Get ready to geek out about programming.

\[sourcecode language="python"\] name = "Zelda" for x in name: print x \[/sourcecode\] Looping over strings v. lists

Solidify: \[sourcecode language="python"\] names

for x in names: if x\[0\] in "AEIOU": print x + " starts with a vowel"

your\_name = "Tim"

if name in names: if name\[0\] in "AEIOU" print name + " start with a vowel" else: print name + " starts with a consonant" \[/sourcecode\]

This is the most conceptually difficult thing

Another Example: Build a list

\[sourcecode language="python"\] vowel\_names = \[\] len(vowel\_names)

for name in names: if name \[0\] in "AEIOU" vowel\_names.append(name)

\[/sourcecode\]

What should vowel\_names contain?

\[sourcecode language="python"\] vowel\_names \[/sourcecode\]

**Build a sentence** \[sourcecode language="python"\] sentence = "" for name in names: sentence = sentence + name \[/sourcecode\] Another Example \[sourcecode language="python"\] sentence = "Four score and seven years ago" sentence\_no\_vowels = "" for letter in sentence: if letter not in "AEIOUaeiou": sentence\_no\_vowels = sentence\_no\_vowels + letter sentence\_no\_vowels \[/sourcecode\] REAL WORK IN FILES!

Copy and paste this into a file and save it as python file using the extension: '.py' \[sourcecode language="python"\] sentence = "Four score and seven years ago" sentence\_no\_vowels = "" for letter in sentence: if letter not in "AEIOUaeiou": sentence\_no\_vowels = sentence\_no\_vowels + letter sentence\_no\_vowels \[/sourcecode\] For example I named my file 'same\_thing.py' and saved it to my desktop.

Then exit out of the REPL by pressing ctrl+c or ctrl+x. Navigate to the directory containing the file. [Use Goal #3 to learn how to navigate your terminal.](https://openhatch.org/wiki/PyCon_intro_tutorial_prep#Goal_.231:_set_up_Python "Look at Goal #3! ") Run the file using the command you used to start the Python REPL. Possibly: `python same_thing.py` or `C:\Python27\python.exe same_thing.py`

This is what running a this python file looks like for me: `C:\Users\tireilly\Desktop> C:\Python27\python.exe same_thing.py`

And there you go! You've created and run your first Python program.

Now if we have time let's work on some more advanced python!

This is just the beginning! You can change and manipulate this file to do all sorts of wild stuff. This is a very barebones python file. But exemplifies the simplicity and readability of Python. If you're ready to continue learning check out the resources below!

**Next Steps** **Fundamentals Practice:** [Python the Hard Way](http://learnpythonthehardway.org/) [Codeacademy](http://www.codecademy.com/learn "Codeacademy")

**Website Frameworks:** [Django:](http://www.djangobook.com/en/2.0/index.html "So Good") This tutorial is awesome! [Flask:](http://flask.pocoo.org/ "Flask is Fun") Microframework!

**Others:** [iPython Notebook](http://ipython.org/ "Check out Docs and Videos") (Great for Math teachers!) [Pygame](http://www.pygame.org/news.html "Check out the tutorials! ") is great for learning how to make video games!

I think we also talked about website hosting: [This is a great place to get started.](http://blogs.msdn.com/b/msgulfcommunity/archive/2013/04/08/build-your-own-web-site-using-azure-for-free-in-5-minutes.aspx) You can choose WordPress or Django instead.

\[caption id="attachment\_2601" align="aligncenter" width="474"\]![Thank you Workshop Weekend for an awesome workspace! ]({{ site.baseurl }}/assets/images/IMG_1603-e1418082177902-1024x564.jpg) Thank you Workshop Weekend for an awesome workspace! \[/caption\]

