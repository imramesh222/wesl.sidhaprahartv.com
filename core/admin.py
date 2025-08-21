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

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'short_description')
    list_filter = ('status',)
    search_fields = ('title', 'short_description', 'description')
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'short_description', 'description')
        }),
        ('Media', {
            'fields': ('image', 'attachment'),
        }),
        ('Status', {
            'fields': ('status',),
        }),
    )
@admin.register(models.TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'phone')
    search_fields = ('name', 'position', 'email')
    list_filter = ('position',)
    fieldsets = (
        (None, {
            'fields': ('name', 'position', 'description', 'photo')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'facebook', 'twitter', 'instagram'),
            'classes': ('collapse',)
        }),
    )
admin.site.register(models.Testimonial)
admin.site.register(models.Report)
admin.site.register(models.Download)
admin.site.register(models.Notice)
admin.site.register(models.Client)
admin.site.register(models.NewsletterSubscriber)
admin.site.register(models.OrganizationDetail)

