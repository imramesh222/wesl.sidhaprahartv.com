from django.contrib import admin
from django.urls import path, include
from . import models

# Register your models here.
admin.site.register(models.ContactInfo)
admin.site.register(models.ContactMessage)
admin.site.register(models.CarouselItem)
admin.site.register(models.AboutImage)
admin.site.register(models.AboutInfo)
admin.site.register(models.Fact)
admin.site.register(models.FeatureImage)
admin.site.register(models.Feature)
admin.site.register(models.Service)
admin.site.register(models.Project)
admin.site.register(models.TeamMember)
admin.site.register(models.Testimonial)
admin.site.register(models.Report)
admin.site.register(models.Download)
admin.site.register(models.Notice)
admin.site.register(models.Client)
admin.site.register(models.NewsletterSubscriber)
admin.site.register(models.OrganizationDetail)

