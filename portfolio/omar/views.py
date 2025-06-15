from django.shortcuts import render
from .models import Home, About, Profile, Category, Skills, Portfolio, Project


def index(request):


# Home
    home = Home.objects.latest('updated')

    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)

    # Skills
    categories = Category.objects.all()

    # # Portfolio
    # portfolios = Portfolio.objects.all()

    #Projects
    project = Project.objects.latest('updated')

    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        # 'portfolios': portfolios,
        'project' : project
    }

    return render(request, 'index.html', context)