import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Profile, Skill, Service, PricingPackage, Project, ContactMessage

def home_view(request):
    # Fetch first profile or create a default in-memory fallback
    profile = Profile.objects.first()
    if not profile:
        profile = Profile(
            name="Anas NC",
            title="Graphic Designer",
            hero_title="Hey, I'm a Creative Graphic Designer",
            hero_subtitle="Great design should feel invisible. From logo to campaigns, I build brands that connect and convert.",
            about_heading="Designer. Strategist. Creative partner.",
            about_subheading="Blending clarity and creativity to build brands with purpose.",
            about_bio="I'm Anas NC, a freelance brand designer with years of experience helping startups, creators, and growing businesses build identities that feel like them. Blending strategy and style, I'm here to guide you through a fun, collaborative design process.",
            email="hello@anasnc.com",
            location="India"
        )
    
    skills = Skill.objects.all().order_by('number')
    services = Service.objects.all()
    pricing_packages = PricingPackage.objects.all()
    projects = Project.objects.all().order_by('order')
    
    context = {
        'profile': profile,
        'skills': skills,
        'services': services,
        'pricing_packages': pricing_packages,
        'projects': projects,
    }
    return render(request, 'portfolio_app/home.html', context)

@require_POST
def contact_submit_view(request):
    # Support AJAX (JSON) and standard form POST
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.content_type == 'application/json'
    
    if request.content_type == 'application/json':
        try:
            data = json.loads(request.body)
            name = data.get('name', '')
            email = data.get('email', '')
            subject = data.get('subject', '')
            message = data.get('message', '')
        except Exception:
            return JsonResponse({'status': 'error', 'message': 'Invalid data format'}, status=400)
    else:
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        
    if not name or not email or not message:
        if is_ajax:
            return JsonResponse({'status': 'error', 'message': 'Name, email, and message are required'}, status=400)
        messages.error(request, 'Name, email, and message are required.')
        return redirect('home')
        
    # Save the contact message
    ContactMessage.objects.create(
        name=name,
        email=email,
        subject=subject,
        message=message
    )
    
    if is_ajax:
        return JsonResponse({'status': 'success', 'message': 'Your message has been sent successfully!'})
        
    messages.success(request, 'Your message has been sent successfully!')
    return redirect('home')
