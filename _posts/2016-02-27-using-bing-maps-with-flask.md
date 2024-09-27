---
title: "Using Bing Maps with Flask"
date: "2016-02-27"
tags: 
  - "ajax"
  - "azure"
  - "bing"
  - "flask"
  - "maps"
  - "python"
  - "segment"
  - "storage"
---

I'm working on a project that involves mapping and line segments.

It turns out that using the Mapping libraries of Bing and Google make this really easy. You create 'polylines' out of coordinates and colors.

Check out [Microsoft Maps documentation](https://msdn.microsoft.com/en-us/library/dd877180.aspx) for more info and the [dev page](https://www.microsoft.com/maps/choose-your-bing-maps-API.aspx) to sign up for a key.

In this example I'm using AJAX requests.

And this documentation is great for using [Azure Tables](http://azure.github.io/azure-storage-python/ref/azure.storage.table.tableservice.html) And the home directory for [Python Azure Table Usage](https://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-table-storage/)

I was struggling with pulling the data from a Database using flask and serving it to the client for an Ajax request. The end goal is a heat map of sorts with paths being mapped and colors being changed for certain conditions.

I'm still working out the best practices for this, but its working! So take it with a grain of salt.

The code for this project can be found here: [http://github.com/timmyreilly/BumpyRoads](https://github.com/timmyreilly/bumpyRoads/)

After a couple days of tinkering, the main pieces of code that lit this up are as follows.

Get the data from the Azure Table Storage and convert it to a list


```python
# First connect to Azure Table Service def connect\_to\_service(): table\_service = TableService(account\_name=STORAGE\_ACCOUNT\_NAME, account\_key=TABLE\_STORAGE\_KEY) print TableService return table\_service

\# Grab the data from our table def get\_table\_list(table\_service=connect\_to\_service(), max=10, table\_name='test', partitionKey='default'): x = table\_service.query\_entities(table\_name) #print(x) return x

\# return it as a list \* see below for bonus on selecting color codes def get\_json\_list(entity\_list=get\_table\_list()): ''' Takes azure table list and returns json list ''' i = 0 response = [] for r in entity\_list: c = convert\_color\_key\_to\_rgb(int(entity\_list[i].colorKey)) t = (entity\_list[i].latA, entity\_list[i].longA, entity\_list[i].latB, entity\_list[i].longB, entity\_list[i].colorKey, c[0], c[1], c[2]) response.append(t) i += 1 # print response return response
```


\* BONUS to manage color codes nicely I found this neat way of doing switch statements using dictionaries. 
```python
def convert\_color\_key\_to\_rgb(colorKey): return { 0: [100, 100, 100], 1: [240, 0, 255], 2: [0, 0, 255], 3: [0, 255, 0], 4: [255, 255, 0], 5: [255, 85, 0], 6: [255, 0, 0], }.get(colorKey, [100, 100, 100] )
```


Take that list and pass it as JSON to a template. Still not sure if this is best practice, as on the client/javascript side it picks it up as an array object. But this is the route we use in flask to send our data.


```python
@app.route('/d') def binged(): data = get\_json\_list() jdata = json.dumps(data) return render\_template( 'binged.html', data=jdata, key=token )
```


On the template side iterate through the given array object and build and push polylines. This was the toughest part for me to


```javascript
var map = null; function GetMap() { var y = JSON.parse('{{ data|safe }}'); // Initialize the map map = new Microsoft.Maps.Map(document.getElementById("mapDiv"),{ credentials:"{{ key }}", center: new Microsoft.Maps.Location(y[0][0],y[0][1]), zoom: 10 }); console.log(y); for( index = 0; index < y.length; index++ ){ lOne = new Microsoft.Maps.Location(y[index][0], y[index][1]); lTwo = new Microsoft.Maps.Location(y[index][2], y[index][3]); //console.log(lOne); var lineV = new Array(lOne, lTwo); //console.log(y[index][4]) var pLine = new Microsoft.Maps.Polyline(lineV, { strokeColor: new Microsoft.Maps.Color(y[index][5], y[index][6], y[index][7], 100), strokeThickness: 3 }); map.entities.push(pLine) } }
```


Now when I run this project locally I get something that looks like this:

\[caption id="attachment\_6711" align="aligncenter" width="723"\]![Soon they won't be random. ]({{ site.baseurl }}/assets/images/segmentsonmap.png) Soon they won't be random. \[/caption\]

If you want to give it a shot, check out the instructions/source code on [github](https://github.com/timmyreilly/bumpyRoads/)

Feel free to reach out if you have any questions or would like to work together on a project like this. \[caption id="attachment\_6751" align="aligncenter" width="1080"\]![Groovy ]({{ site.baseurl }}/assets/images/Snapchat-3202830476336172555.jpg) Groovy \[/caption\]

