---
layout: page
title: Blog Posts by Tag
desc: "A list of blog posts organized by tags"
permalink: /tag/
---

Click on a tag to see a relevant list of posts.

<ul class="tags">
  {% for tag in site.tags %}
    {% assign t = tag | first %}
    <li><a href="/tag/#{{ t | downcase | replace: " ", "-" }}">{{ t | downcase }}</a></li>
  {% endfor %}
</ul>

---

{% for tag in site.tags %}
  {% assign t = tag | first %}
  {% assign posts = tag | last %}

  <h4>
    <a name="{{ t | downcase | replace: " ", "-" }}"></a>
    <a class="internal" href="/tag/#{{ t | downcase | replace: " ", "-" }}">{{ t | downcase }}</a>
  </h4>
  
  <ul>
    {% for post in posts %}
      {% if post.tags contains t %}
      <li>
        <a href="{{ post.url | prepend: site.baseurl }}" target="_blank">{{ post.title }}</a>
        <span class="date">{{ post.date | date: "%B %-d, %Y" }}</span>
      </li>
      {% endif %}
    {% endfor %}
  </ul>

---

{% endfor %}
