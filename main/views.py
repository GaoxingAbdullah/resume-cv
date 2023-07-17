from django.shortcuts import render
from django.views import generic
from django.contrib import messages

from .models import (
    UserProfile,
    Testimonial,
    Portfolio,
    Blog,
    Certificate,
    ContactProfile
    )

from .forms import ContactForm


class IndexView(generic.TemplateView):
    def get(self, request, *args, **kwargs):

        testimonials = Testimonial.objects.filter(active=True)
        certificates = Certificate.objects.filter(active=True)
        portfolios = Portfolio.objects.filter(active=True)
        blogs = Blog.objects.filter(active=True)

        context = {
            'certificates': certificates,
            'testimonials': testimonials,
            'portfolios': portfolios,
            'blogs': blogs,
        }
        return render(request, 'main/index.html', context)
   

class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'main/contact.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank You. We will be in touch soon.')
        return super().form_valid(form)
    

class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'main/portfolio.html'
    paginate_by = 10
    context_object_name = 'portfolios'

    def get_queryset(self):
        return Portfolio.objects.filter(active=True)


class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    template_name = 'main/portfolio-detail.html'


class BlogView(generic.ListView):
    model = Blog
    template_name = 'main/blog.html'
    paginate_by = 10
    context_object_name = 'blogs'

    def get_queryset(self):
        return Blog.objects.filter(active=True)
    
    

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'main/blog-detail.html' 
    context_object_name = 'blogs'
    
