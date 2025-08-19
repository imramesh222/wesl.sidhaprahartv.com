from django.db import models
from ckeditor.fields import RichTextField


class CarouselItem(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    button_text = models.CharField(max_length=50, blank=True)
    button_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class AboutImage(models.Model):
    image = models.ImageField(upload_to='about/')

    def __str__(self):
        return f"About Image {self.id}"

class AboutInfo(models.Model):
    heading = models.CharField(max_length=200)
    description = models.TextField()
    features = models.JSONField(default=list, blank=True, null=True)

    def _str_(self):
        return self.heading


class Fact(models.Model):
    icon_class = models.CharField(max_length=100)
    number = models.PositiveIntegerField()
    label = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.label} ({self.number})"

class FeatureImage(models.Model):
    image = models.ImageField(upload_to='features/')

    def __str__(self):
        return f"Feature Image {self.id}"

class Feature(models.Model):
    icon_class = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

from django.utils.text import slugify

class Service(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    slug = models.SlugField(null=True, blank=True, unique=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Project(models.Model):
    STATUS_CHOICES = (
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    )

    title = models.CharField(max_length=200)
    short_description = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')

    def _str_(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)




class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team/')
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} - {self.position}"

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='testimonials/')
    text = models.TextField()

    def __str__(self):
        return f"{self.client_name} ({self.profession})"

class ContactInfo(models.Model):
    phone_number = models.CharField(max_length=30)
    email = models.EmailField()
    office_address = models.TextField()
    map_link = models.URLField()
    map_iframe_src = models.TextField()

    def __str__(self):
        return f"Contact Info ({self.email})"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class Download(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='downloads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Report(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='reports/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    attachment = models.FileField(upload_to='notices/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='clients/')
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class OrganizationDetail(models.Model):
    site_title = models.CharField(max_length=200, default='Hydro Organization')
    logo = models.ImageField(blank=True, null=True, upload_to="logo" )
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    whatsapp_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    weekday_hours = models.CharField(max_length=100)
    saturday_hours = models.CharField(max_length=100)
    sunday_hours = models.CharField(max_length=100)

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.site_title


class Photo(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Video(models.Model):
    title = models.CharField(max_length=200)
    youtube_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def embed_url(self):
        # Convert YouTube URL to embed format
        import re
        match = re.search(r"v=([^&]+)", self.youtube_url)
        return f"https://www.youtube.com/embed/{match.group(1)}" if match else self.youtube_url

        


class KeyInfo(models.Model):
    key_strategy = RichTextField(blank=True)
    key_achievement = RichTextField(blank=True)

    def __str__(self):
        return "Key Info"
    

class OrganizationContent(models.Model):
    mission = RichTextField(verbose_name="Mission Description")
    vision = RichTextField(verbose_name="Vision Description")
    goal = RichTextField(verbose_name="Goal Description")
    objective = RichTextField(verbose_name="Organizational Objective Description")
    value = RichTextField(verbose_name="Organizational Value Description")
    geo_area = RichTextField(verbose_name="Geographical Area Description")
    theme_area = RichTextField(verbose_name="Thematic Area Description")

    def __str__(self):
        return "Organizational Content"    