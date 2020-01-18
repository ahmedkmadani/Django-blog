from django.shortcuts import render


posts = [
    {
        'author':'Ahmedk',
        'title' : 'Blog Post 1',
        'content' : 'First Post content',
        'date_posted' : 'Augest 27, 2020'
    },
       {
        'author':'Ahmedk Madani',
        'title' : 'Blog Post 2',
        'content' : 'Second Post content',
        'date_posted' : 'Augest 29, 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})
