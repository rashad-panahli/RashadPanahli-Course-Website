from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, FormView, CreateView
from .models import Post, Contact, ContactForm
from django.contrib import messages
from marketing.forms import SignupForm
from django import forms


def home (request):
    return render(request, 'blog/index.html')
        
def about (request):
    return render (request, 'blog/about.html' )

def teachers (request):
    return render (request, 'blog/teacher.html' )

def courses (request):
    return render (request, 'blog/courses.html' )

def abroad (request):
    return render (request, 'blog/abroad.html' )

def contact (request):
    if request.method  ==  'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            contactdata=Contact()
            contactdata.name = form.cleaned_data ['name']
            contactdata.email = form.cleaned_data ['email']
            contactdata.subject = form.cleaned_data ['subject']
            contactdata.message = form.cleaned_data ['message']
            contactdata.save()


        messages.success(request, "Sizin məktub müvəffəqiyətlə göndərildi")
        return HttpResponseRedirect('/contact/')
    else:
        form = ContactForm()   

    return render (request, 'blog/contact.html', {'form': form})   

def blog (request):
    return render (request, 'blog/blog.html')        

class BlogView(ListView):
    model = Post
    template_name =  'blog/blog.html'
    context_object_name = "blog_posts"
    ordering = ['-post_date_posted']

class BlogDetailView(DetailView):
    model = Post



class FooterView(CreateView):
    template_name = 'blog/footer.html'
    form_class = SignupForm
    success_url = '/'
    