from django.contrib import admin

from .models import (
    Skill, 
    UserProfile, 
    Testimonial, 
    Media,
    Portfolio,
    Blog,
    Certificate,
    ContactProfile
    )


admin.site.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title', 'bio']
    search_fields = ('user', 'name', 'title')


admin.site.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score')


admin.site.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'quote', 'image', 'active')


admin.site.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


admin.site.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url', 'description')


admin.site.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url', 'description')
    readonly_fields = ('slug',)


admin.site.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'url', 'description')


admin.site.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'message')







