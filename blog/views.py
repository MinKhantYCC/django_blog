from datetime import date

from django.shortcuts import render

# Create your views here.
all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountain.jpg",
        "author": "Min Khant",
        "date": date(2024, 12, 25),
        "title": "Mountain Hiking",
        "excerpt": "There is nothing like the views you get when hiking in the mountains!",
        "content": "There is nothing like the views you can get when hiking in the mountains! Let's go hiking."
    },
    {
        "slug": "Living-in-the-dark",
        "image": "dark.jpg",
        "author": "Min Khant",
        "date": date(2025, 1, 1),
        "title": "Living in the dark",
        "excerpt": "Sometimes, we need to live in the dark to know the value of light.",
        "content": "Sometimes, we need to live in the dark to know the value of light. Isn't it?"
    },
    {
        "slug": "Monkey-Coder",
        "image": "mky-coder.png",
        "author": "Min Khant",
        "date": date(2025, 1, 5),
        "title": "Code like monkey",
        "excerpt": "You know, Monkey can do coding.",
        "content": "Yeah. Monkey can code. Monkey is me."
    }
]

def get_date(post):
    return post["date"]

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })