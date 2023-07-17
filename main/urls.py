from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio/<int:slug>/', views.PortfolioDetailView.as_view(), name='portfolio-detail'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('blog/blog-detail/<int:slug>/', views.BlogDetailView.as_view(), name='blog-detail'),
    
]
