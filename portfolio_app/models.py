from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, default="Anas NC")
    title = models.CharField(max_length=100, default="Graphic Designer")
    
    # Hero Section
    hero_title = models.CharField(max_length=200, default="Hey, I'm Anas NC, a Graphic Designer.")
    hero_subtitle = models.TextField(default="Great design should feel invisible. From logo to campaigns, I build brands that connect and convert.")
    
    # About Section
    about_heading = models.CharField(max_length=200, default="Designer. Strategist. Creative partner.")
    about_subheading = models.CharField(max_length=200, default="Blending clarity and creativity to build brands with purpose.")
    about_bio = models.TextField(default="I'm Anas NC, a freelance brand designer with years of experience helping startups, creators, and growing businesses build identities that feel like them. Blending strategy and style, I'm here to guide you through a fun, collaborative design process.")
    about_image = models.ImageField(upload_to="profile/", blank=True, null=True)
    
    # Behind the Designs Section
    behind_title = models.CharField(max_length=200, default="Shaping Experiences That Make Life Simpler")
    behind_text = models.TextField(default="I'm a product designer focused on building clean, intuitive interfaces that solve real-world problems.")
    
    # Contact & Socials
    email = models.EmailField(default="hello@anasnc.com")
    phone = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, default="India")
    resume = models.FileField(upload_to="resume/", blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    behance = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    dribbble = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100)
    number = models.CharField(max_length=10, help_text="e.g., +01, +02")
    description = models.TextField(blank=True, null=True)
    percentage = models.IntegerField(default=90, help_text="Progress bar percentage")
    
    def __str__(self):
        return f"{self.number} - {self.name}"

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, blank=True, null=True, help_text="Icon class name or SVG identifier")
    
    def __str__(self):
        return self.title

class PricingPackage(models.Model):
    name = models.CharField(max_length=100) # Starter, Pro plan, Enterprise plan
    price = models.CharField(max_length=50) # e.g. "$1990"
    billing = models.CharField(max_length=50, default="month") # e.g. "month"
    features_text = models.TextField(help_text="Enter one feature per line")
    is_popular = models.BooleanField(default=False)
    cta_text = models.CharField(max_length=50, default="Get in touch")
    
    @property
    def features_list(self):
        return [f.strip() for f in self.features_text.split('\n') if f.strip()]
        
    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200) # Orange Blox, Nova Scene
    category = models.CharField(max_length=100) # Brand Identity Design, Packaging Design
    description = models.TextField()
    image = models.ImageField(upload_to="projects/")
    url = models.URLField(blank=True, null=True, help_text="External link to project page")
    is_featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0, help_text="Lower values come first")
    
    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} - {self.email}"
