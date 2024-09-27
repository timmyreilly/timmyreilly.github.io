---
title: "Cool Things about JavaScript"
date: "2015-07-25"
---

JavaScript is cool. I don't know why, but that's what I hear. So I decided to dedicate a quiet week to learning all about JavaScript from this book [Eloquent JavaScript](http://eloquentjavascript.net/). The author is great and the explanations/examples are clear and interesting.

I'm almost halfway through the book and these are just a few of the cool things I've learned:

**Lexical Scoping**

Lexical Scoping is not just fun to think about it can be very powerful. What is going to happen when the scope of a function is determined by the function that calls it?

You can get functions to do all sorts of crazy stuff this way.

Here are a couple different ways to get it into your head:

From _Eloquent JavaScript:_  "...each local scope can also see all the local scopes that contain it. The set of variables visible inside a function is determined by the place of that funciton in the program text. All variables from blocks around a functions definition are visible -- meaning both those in function bodies that enclose it and those at the top level of the program. This approach to variable visibility is called _lexical scoping._" - Marijn Haverbeke

[Helpful StackOverflow](http://stackoverflow.com/questions/1047454/what-is-lexical-scope)

[Helpful Blog](http://pierrespring.com/2010/05/11/function-scope-and-lexical-scoping/)

"The scope of an _inner function_ contains the scope of a parent function."

My example: Each local scope, can see the variables of the containing scope. Each new set of braces does NOT create a brand new environment. It's like the octopus holds another octopus.


```javascript
var octopus1 = function(){ var smallArms = 5; var octopus2 = function(){ var largeArms = 8; console.log(largeArms > smallArms); } }

octopus1(); --> True
```


It's like each new function is a new Octopus, and one of the octopus tentacles is on the octopus that called it.

It seems like kind of a backward metaphor. Like the thing that harkens for information ends up being help by the provider.

So the biggest octopus will be found at the most inner scope. Holding a chain of sequentially smaller octopuses.

Other things that I found cool...

**NaN and Undefined (Null?)**

Very much a pitfall to be aware of, on second thought this isn't really cool, but just good to know.

Here's a helpful blog that helped me wrap my brain around the [reasoning and differences](http://www.mapbender.org/JavaScript_pitfalls:_null%2C_false%2C_undefined%2C_NaN)

He references this source for his blog: [which I've found helpful](http://www.hunlock.com/blogs/Essential_Javascript_--_A_Javascript_Tutorial) .

NaN: Not a number, bad arithmetic

Undefined: variable doesn't have a value

Null: Not a value, will return empty object.

**Infinity and -Infinity**

As my little cousin would say, "You're it times infinity!"

**For loops like C++**


```JavaScript
for(var i == 0; i < 10; i++){ console.log("ahh yeah"); }
```


C++ was my first language so these for loops remind me of my first CS class, even though that's where I got my first C on an exam, it was the first time I felt the power of computing.

**Strings can be wrapped 'with single quotes' or "double quotes"**

'That\\'s nice' "How convenient!"

**Ternary Operator** 
```JavaScript
console.log(true ? 1 : 2) // --> 1

console.log(false ? 1 : 2) // --> 2
```


This is cool. I've never used a ternary operator. I could see this saving lots of lines for if statements.

**Variables as Tentacles**

'rather than boxes. They do not contain values; they only grasp them … when you need to remember something, you grow a tentacle to hold on to it or you reattach one of your existing tentacles to it.' - Marijn Haverbeke

Like lexical scoping, this is a cool metaphor for looking at your programs and functions. Gosh octopi are [cool](http://media.giphy.com/media/NbeduiwpZhTNu/giphy.gif) and [smart](https://en.wikipedia.org/wiki/Octopus)!

**do loops**

Do this… Then loop if the condition is met. When you just need to get something done. DO it!

Finally:

**Optional Arguments are handled nicely.**


```JavaScript
function power(base, exponent){ if (exponent == undefined) exponent = 2; var result = 1; for(var count = 0; count < exponent; count++) result \*= base; return result; }

console.log(power(4)); // --> 16 console.log(power(4, 3)); // --> 64
```


Ahh that's sooo sweet.

Looking forward to continued JavaScript development and I hope this list has whet your appetite for more JavaScript to come.

Happy Friday, Tim

\[video width="528" height="384" mp4="http://timmyreilly.azurewebsites.net/wp-content/uploads/2015/07/24mdoubledraw.mp4"\]\[/video\]

If that doesn't load, here another photo that I enjoy: \[caption id="attachment\_5251" align="aligncenter" width="3552"\]![Pickup truck full of kegs]({{ site.baseurl }}/assets/images/WP_20150702_15_36_27_Pro.jpg) This pickup truck looks like Seattle\[/caption\]

