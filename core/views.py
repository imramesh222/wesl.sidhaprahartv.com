from django.shortcuts import render
from .models import (
    ContactInfo, ContactMessage, CarouselItem, AboutImage, AboutInfo,
    Fact, Feature, Service, Project, TeamMember, Testimonial, FeatureImage,
    Report, Download, Notice, Client, NewsletterSubscriber,OrganizationContent
)
from .models import Photo, Video, KeyInfo
from .forms import PhotoForm, VideoForm
from .forms import ContactForm
from django.contrib import messages
from django.shortcuts import redirect

# Home Page View
def home(request):
    context = {
        'carousel_items': CarouselItem.objects.all(),
        'about_images': AboutImage.objects.all(),
        'about_info': AboutInfo.objects.first(),
        'facts': Fact.objects.all(),
        'feature_img': FeatureImage.objects.first(),
        'features': Feature.objects.all(),
        'services': Service.objects.all(),
        'projects': Project.objects.all(),
        'team_members': TeamMember.objects.all(),
        'testimonials': Testimonial.objects.all(),
        'contact_info': ContactInfo.objects.first(),
        'clients': Client.objects.all(),
        'notices': Notice.objects.all().order_by('-published_at')[:3],  # Add this line
    }
    return render(request, 'home.html', context)



def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(status=project.status).exclude(id=project.id)[:5]
    return render(request, 'projects/detail.html', {
        'project': project,
        'related_projects': related_projects,
    })



# About Page View
def about(request):
    context = {
        'about_images': AboutImage.objects.all(),
        'about_info': AboutInfo.objects.first(),

        'organization_content': OrganizationContent.objects.first(),
    }
    return render(request, 'about.html', context)


# Static Pages
def services(request):
    context = {
        'services': Service.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }

    return render(request, 'services.html', context)

from django.shortcuts import get_object_or_404

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    related_services = Service.objects.exclude(id=service.id)[:5]
    return render(request, 'services/detail.html', {
        'service': service,
        'related_services': related_services})

def projects(request):
    ongoing_projects = Project.objects.filter(status='ongoing')
    completed_projects = Project.objects.filter(status='completed')

    context = {
        'ongoing_projects': ongoing_projects,
        'completed_projects': completed_projects,
    }
    return render(request, 'projects.html', context)

def reports(request):
    reports = Report.objects.all().order_by('-created_at')  # latest first
    context = {'reports': reports}
    return render(request, 'reports.html', context)

def downloads(request):
    downloads = Download.objects.all().order_by('-uploaded_at')
    context = {'downloads': downloads}
    return render(request, 'downloads.html', context)

def notice(request):
    notices = Notice.objects.filter(is_active=True).order_by('-published_at')
    context = {
        'notices': notices,
        'title': 'News and Notices',
        'page_header': 'News and Notices',
        'breadcrumb_title': 'News and Notices'
    }
    return render(request, 'notice.html', context)


def notice_detail(request, pk):
    notice = get_object_or_404(Notice, pk=pk, is_active=True)
    related_notices = Notice.objects.filter(is_active=True).exclude(pk=pk).order_by('-published_at')[:5]
    
    # Get the latest notices for the frontend view
    latest_notices = Notice.objects.filter(is_active=True).order_by('-published_at')[:10]
    
    context = {
        'notice': notice,  # For single notice view
        'notices': latest_notices,  # For list view fallback
        'related_notices': related_notices,
        'title': notice.title,
        'page_header': notice.title,
        'breadcrumb_title': 'Notice Details'
    }
    return render(request, 'notice.html', context)


# Contact Page View
def contact(request):
    contact_info = ContactInfo.objects.first()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            ContactMessage.objects.create(
                name=cd['name'],
                email=cd['email'],
                subject=cd['subject'],
                message=cd['message']
            )
            return render(request, 'contact.html', {
                'form': ContactForm(),
                'success': True,
                'contact_info': contact_info,
            })
    else:
        form = ContactForm()

    return render(request, 'contact.html', {
        'form': form,
        'contact_info': contact_info,
    })

def clients(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'clients.html', context)

def subscribe_newsletter(request):
    if request.method == "POST":
        email = request.POST.get('email')
        if email:
            if not NewsletterSubscriber.objects.filter(email=email).exists():
                NewsletterSubscriber.objects.create(email=email)
                messages.success(request, "Thank you for subscribing!")
            else:
                messages.info(request, "You're already subscribed.")
        else:
            messages.error(request, "Please enter a valid email.")
    return redirect(request.META.get('HTTP_REFERER', '/'))


def video(request):
    videos = Video.objects.all().order_by('-created_at')
    return render(request, 'videogallery.html', { 'videos': videos})


def photo(request):
    photos = Photo.objects.all().order_by('-created_at')
    return render(request, 'photogallery.html', {'photos': photos})



def key_info_view(request):
    # Get the KeyInfo instance (assuming you have one)
    key_info = KeyInfo.objects.first()
    
    context = {
        'key_info': key_info
    }
    return render(request, 'what_we_do.html', context)


def coverage(request):
    return render(request, 'coverage.html')