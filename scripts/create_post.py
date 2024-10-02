import sys
import os
from datetime import datetime

# Function to create a Jekyll post
def create_jekyll_post(title, tags):
    # Ensure the _posts directory exists
    posts_dir = '_posts'
    if not os.path.exists(posts_dir):
        os.makedirs(posts_dir)

    # Get current date and time
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")

    # Convert the title to a valid filename format (lowercase, hyphen-separated)
    filename_title = title.strip().lower().replace(' ', '-')
    filename = f"{date_str}-{filename_title}.md"

    # Define the path for the new post
    file_path = os.path.join(posts_dir, filename)

    # Prepare the markdown content with front matter
    content = f"""---
layout: post
title: "{title}"
date: {time_str}
categories: blog
tags: [{tags}]
---

# {title}

Write your content here...
"""

    # Write the content to the markdown file
    with open(file_path, 'w') as f:
        f.write(content)

    print(f"New post created: {file_path}")

# Main function to handle input arguments
def main():
    if len(sys.argv) < 3:
        print("Usage: python create_post.py 'Post Title' 'tag1, tag2, tag3'")
        return

    # Get the title and tags from command-line arguments
    title = sys.argv[1]
    tags = sys.argv[2]

    # Create the post
    create_jekyll_post(title, tags)

if __name__ == '__main__':
    main()
