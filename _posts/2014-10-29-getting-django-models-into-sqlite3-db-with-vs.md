---
title: "Getting Django Models into SQLite3 DB with VS"
date: "2014-10-29"
tags: 
  - "exe"
  - "app"
  - "book"
  - "code"
  - "django"
  - "manage-py"
  - "microsoft"
  - "migrations"
  - "models"
  - "module"
  - "named"
  - "ptvs"
  - "python"
  - "sqlite3"
  - "table"
  - "visual"
  - "vs"
---

I ran into some troubles migrating/configuring my tables for a new app in my Django project.

I've been following this [excellent tutorial](http://www.djangobook.com/en/2.0/chapter05.html "Django BOOOK!"), and ran into a bump I thought needed some clarification/update. As I'm not sure if the guide is up to date with the current version of Django.

**Things I searched:** no module named models manage.py sqlall django not creating db models are not being created in sqlite3 Django sqlite3 not creating table django No migrations to apply django sqlite3 unable to create tables manage.py shell sqlite3 python package

Do these correlate with what you're having issues with? If so this was my solution.

First Install SQLite3 and add it too your Environment Variables -> Path Install Page -- Select: Source Code -> Zip for windows machines I extracted it to C:/. Now I have SQLite.exe in my root directory. This is what the end of my Path looks like: C:\\Program Files\\Microsoft\\Web Platform Installer\\;C:\\SQLITE3.EXE\\;

Sweet, now we can use SQLite in Powershell.

**Configuration of Visual Studio:** Create a new app by right clicking on your Project file. Then "Add" -> Select "Django App" In this case my app is named book.

![DjangoApp Solution Explorer]({{ site.baseurl }}/assets/images/Untitled-picture-e1414616589757.png)

Sweet, now we have another Python app. Go into your settings file and add it to the INSTALLED\_APPS tuple. eg. 'book',

Okay, now we're configured make sure you're **SQLiteDB** is properly configured as well.

eg: 'ENGINE': 'django.db.backends.sqlite3', 'NAME': path.join(PROJECT\_ROOT, 'db.sqlite3'), 'USER': '', 'PASSWORD': '', 'HOST': '', 'PORT': '', Sweet, db all locked and loaded.

**Next we'll create a model.** Following along with the tutorial. We go into: book -> models.py and create our models. Eg: class Publisher(models.Model): name = models.CharField(max\_length=30) address = models.CharField(max\_length=50) city = models.CharField(max\_length=60) state\_province = models.CharField(max\_length=30) country = models.CharField(max\_length=50) website = models.URLField()

Sweet. Model made. Let's get it into our SQLite DB.

**Alright now in DjangoProject1Hack (Where 'ls' will show db.sqlite3 among others) We'll be doing the migration.**

1\. **Validate:** Run- C:\\Python27\\python.exe manage.py validate 2. **makemigrations** Run- C:\\Python27\\python.exe manage.py makemigrations Output: Migrations for 'book': 0001\_initial.py: - Create model Author - Create model Book - Create model Publisher - Add field publisher to book 3. **Sync (This just makes sure we add what's missing)** Run- C:\\Python27\\python.exe manage.py syncdb Output: Operations to perform: Apply all migrations: book Running migrations: Applying book.0001\_initial... OK

Sweeeeeeet!

Okay now we manage the db: Run- C:\\Python27\\python.exe manage.py shell **Sample workflow in Shell:**

\>>> from book.models import Publisher >>> p1 = Publisher(name='Apress', address='2855 Telegraph ave', city='berkely', state\_province='CA', country='USA', website= 'http://www.apress.com/') >>> p1.save() >>> p2 = Publisher(name="o'reilly", address='10 Fawcett St.', city='Cambridge', state\_province='MA', country='USA', website= 'http://www.oreilly.com/') >>> p2.save() >>> publisher\_list = Publisher.objects.all() >>> publisher\_list Publisher: Publisher object, Publisher: Publisher object

[Yeehaa](http://youtu.be/2x7bMzDPDbs "Dancing Tips"), let me know if you have any other questions!

\[caption id="attachment\_1761" align="aligncenter" width="474"\]![What is it? ]({{ site.baseurl }}/assets/images/WP_20141025_001-2-680x1024.jpg) If you can guess what pun this represents, I'll venmo you a dollar. \[/caption\]

