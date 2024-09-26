---
layout: default
title: Check
---

<h1>Welcome to My Jekyll Blog</h1>

<p>Here are the latest posts:</p>

<ul>
  {% for post in paginator.posts %}
    <li>
      <a href="{{ post.url | prepend: site.baseurl }}">
        {{ post.title }}
      </a>
      <span>Published on {{ post.date | date: "%B %d, %Y" }}</span>
    </li>
  {% endfor %}
</ul>

<div class="pagination">
  {% if paginator.previous_page %}
    <a href="{{ paginator.previous_page_path | prepend: site.baseurl }}">&larr; Previous</a>
  {% endif %}
  {% if paginator.next_page %}
    <a href="{{ paginator.next_page_path | prepend: site.baseurl }}">Next &rarr;</a>
  {% endif %}
</div>
