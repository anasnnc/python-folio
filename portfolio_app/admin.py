from django.contrib import admin
from .models import Profile, Skill, Service, PricingPackage, Project, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'location')
    fieldsets = (
        ('Personal Info', {
            'fields': ('name', 'title', 'email', 'phone', 'location', 'resume')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle')
        }),
        ('About Section', {
            'fields': ('about_heading', 'about_subheading', 'about_bio', 'about_image')
        }),
        ('Behind the Designs', {
            'fields': ('behind_title', 'behind_text')
        }),
        ('Social Links', {
            'fields': ('linkedin', 'behance', 'instagram', 'dribbble')
        }),
    )

    def has_add_permission(self, request):
        # Limit to 1 profile max
        if Profile.objects.exists():
            return False
        return True

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'percentage')
    list_editable = ('name', 'percentage')
    ordering = ('number',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

@admin.register(PricingPackage)
class PricingPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'billing', 'is_popular')
    list_editable = ('price', 'billing', 'is_popular')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'order', 'is_featured')
    list_editable = ('category', 'order', 'is_featured')
    list_filter = ('category', 'is_featured')
    search_fields = ('title', 'category', 'description')
    ordering = ('order',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'created_at'
    
    def has_add_permission(self, request):
        return False
        
    def has_change_permission(self, request, obj=None):
        return False
