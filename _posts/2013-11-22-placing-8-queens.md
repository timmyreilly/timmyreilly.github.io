---
title: "Placing 8 Queens"
date: "2013-11-22"
---

I figure the second post I make ought to be a bit nerdy.

This is an algorithm we were working on in class yesterday, and I thought was pretty cool. It's called the Eight Queens Puzzle. The challenge is to place eight queens on a chess board without them being able to attack each other. The solution we were taught uses Backtracking, which is slowly exploding my mind. This little bit of code uses a helper recursive function and an isValid to check if a queen can be placed. The queens' locations are stored in a vector of strings where "Q......." is a queen on the first column, and the vector index is the row.

This is the recursive helper function:

<script src="http://pastebin.com/embed_js.php?i=uV1erz00"></script>

Neato!

