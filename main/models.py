from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils.text import slugify


class Skill(models.Model):
    class Meta:
        verbose_name = 'Skills'
        verbose_name_plural = 'Skills'

    name = models.CharField(max_length=30, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='skills/')
    key_skill = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    class Meta:
        verbose_name = 'User Profiles'
        verbose_name_plural = 'User Profiles'

    user = models.OneToOneField(User, on_delete=models.CASCADE )
    avatar = models.ImageField(blank=True, null=True, upload_to='profile/')
    title = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    cv = models.FileField(blank=True, null=True, upload_to='cv/')
    

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    

class Testimonial(models.Model):
    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        ordering = ['name']

    name = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='testimonials/')
    title = models.CharField(max_length=30, blank=True, null=True)
    quote = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Media(models.Model):
    class Meta:
        verbose_name = 'Media Files'
        verbose_name_plural = 'Media'
        ordering = ['name']

    name = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='media/')
    url = models.URLField(blank=True, null=True)
    is_image = models.BooleanField(default=True)

    
    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        super(Media, self).save(*args, **kwargs)

    
    def __str__(self):
        return self.name
    

class Portfolio(models.Model):
    class Meta:
        verbose_name = 'Portfolio Profiles'
        verbose_name_plural = 'Portfolios'
        ordering = ['name']

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='portfolio/')
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Portfolio, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    # def get_absolute_url(self):
    #     return f"/portfolio/{self.slug}"
    

class Blog(models.Model):
    class Meta:
        verbose_name = 'Blog Profiles'
        verbose_name_plural = 'Blogs'
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='blog/')
    slug = models.SlugField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/blog/{self.slug}"
    

class Certificate(models.Model):
    class Meta:
        verbose_name = 'Certificates'
        verbose_name_plural = 'Certificates'

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='certificates/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ContactProfile(models.Model):
    class Meta:
        verbose_name = 'Contact Profile'
        verbose_name_plural = 'Contact Profiles'
        ordering = ['timestamp']

    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200,verbose_name='Name', null=True)
    email = models.EmailField(verbose_name='Email', null=True)
    message = models.TextField(verbose_name='Message', null=True)

    def __str__(self):
        return self.name