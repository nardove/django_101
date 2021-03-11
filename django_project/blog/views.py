from django.shortcuts import render

posts = [
    {
        'author': 'Ricardo Sanchez',
        'title': 'Dummy blog post',
        'content': 'First post content',
        'date_posted': 'March 10, 2021'
    },
    {
        'author': 'Thomas Sanchez',
        'title': 'Second dummy blog post',
        'content': 'Second post content',
        'date_posted': 'June 01, 2014'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})