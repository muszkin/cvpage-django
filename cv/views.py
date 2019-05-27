from django.utils.translation import activate
from django.shortcuts import render

from .models import Shool, Skill, Testimonial, Work
# Create your views here.


def index(request):
    shools = Shool.objects.all()
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.all()
    works = Work.objects.all()
    for work in works:
        work.duties = work.duties.all(work)

    activate("pl")
    return render(request, 'index.html', {
        "shools": shools,
        "skills": skills,
        "testimonials": testimonials,
        "works": works
    })
