import os
# pyrefly: ignore [missing-import]
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
django.setup()

from portfolio_app.models import Profile, Skill, Service, PricingPackage, Project

def seed_database():
    print("Starting database seeding...")
    
    # 1. Profile
    Profile.objects.all().delete()
    profile = Profile.objects.create(
        name="Anas NC",
        title="Graphic Designer",
        hero_title="Hey, I'm Anas NC, a Graphic Designer.",
        hero_subtitle="Great design should feel invisible. From logo to campaigns, I build brands that connect and convert.",
        about_heading="Designer. Strategist. Creative partner.",
        about_subheading="Blending clarity and creativity to build brands with purpose.",
        about_bio="I'm Anas NC, a freelance brand designer with years of experience helping startups, creators, and growing businesses build identities that feel like them. Blending strategy and style, I'm here to guide you through a fun, collaborative design process.",
        about_image="profile/profile.png",
        behind_title="Shaping Experiences That Make Life Simpler",
        behind_text="I'm a graphic designer focused on building clean, intuitive visual systems and products that solve real-world problems.",
        email="hello@anasnc.com",
        phone="+91 98765 43210",
        location="India",
        linkedin="https://linkedin.com",
        behance="https://behance.net",
        instagram="https://instagram.com"
    )
    print("Created Profile.")

    # 2. Skills
    Skill.objects.all().delete()
    skills = [
        {"name": "Brand Strategy", "number": "+01", "percentage": 95},
        {"name": "Brand Identity Design", "number": "+02", "percentage": 90},
        {"name": "Packaging Design", "number": "+03", "percentage": 85},
        {"name": "Creative Direction", "number": "+04", "percentage": 80},
    ]
    for s in skills:
        Skill.objects.create(**s)
    print("Created Skills.")

    # 3. Services
    Service.objects.all().delete()
    services = [
        {
            "title": "Brand Strategy",
            "description": "Identifying your target audience, developing unique market positioning, and establishing a cohesive brand voice.",
            "icon": "fas fa-drafting-compass"
        },
        {
            "title": "Brand Identity Design",
            "description": "Crafting memorable logos, custom typography, color systems, and comprehensive style guides.",
            "icon": "fas fa-bezier-curve"
        },
        {
            "title": "Packaging Design",
            "description": "Designing premium packaging containers, custom labels, and structural concepts for physical goods.",
            "icon": "fas fa-box-open"
        },
        {
            "title": "Creative Direction",
            "description": "Directing visual aesthetics for advertising, photography shoots, and multichannel digital design projects.",
            "icon": "fas fa-photo-film"
        }
    ]
    for sv in services:
        Service.objects.create(**sv)
    print("Created Services.")

    # 4. Pricing Packages
    PricingPackage.objects.all().delete()
    packages = [
        {
            "name": "Starter",
            "price": "$1990",
            "billing": "project",
            "features_text": "Logo design\nTypography selection\nBasic brand guide\n3 Revision cycles",
            "is_popular": False,
            "cta_text": "Get in touch"
        },
        {
            "name": "Pro plan",
            "price": "$2990",
            "billing": "project",
            "features_text": "Full visual identity\nBrand strategy\nDetailed brandbook\nSocial media templates\nUnlimited Revision cycles",
            "is_popular": True,
            "cta_text": "Get in touch"
        },
        {
            "name": "Enterprise plan",
            "price": "$4990",
            "billing": "project",
            "features_text": "Full visual identity\nBrand strategy\nCustom packaging design\nLogo animation & training\n1 Year post-launch support",
            "is_popular": False,
            "cta_text": "Get in touch"
        }
    ]
    for pkg in packages:
        PricingPackage.objects.create(**pkg)
    print("Created Pricing Packages.")

    # 5. Projects
    Project.objects.all().delete()
    projects = [
        {
            "title": "Orange Blox",
            "category": "Brand Design",
            "description": "Orange Blox is a vibrant lifestyle apparel brand that brings playfulness and geometry together. In this project, we designed the brand identity, logo, typography guidelines, and apparel packaging concepts.",
            "image": "projects/orange_blox.png",
            "url": "https://behance.net",
            "order": 1
        },
        {
            "title": "Nova Scene",
            "category": "Packaging Design",
            "description": "Nova Scene is a high-end luxury fragrance company. We crafted a premium packaging experience, from custom bottle labels to textured presentation boxes with hot foil stamps.",
            "image": "projects/nova_scene.png",
            "url": "https://behance.net",
            "order": 2
        },
        {
            "title": "Arched Pink",
            "category": "Cosmetics Branding",
            "description": "Arched Pink is a minimalist organic cosmetics brand focused on skin health. We developed the clean, arched label aesthetic and premium soft-touch glass printing layouts.",
            "image": "projects/arched_pink.png",
            "url": "https://behance.net",
            "order": 3
        },
        {
            "title": "Liquid",
            "category": "Experimental Art",
            "description": "Liquid is a creative exhibition showcasing metallic sculpture concepts. We conceptualized the visual branding, post-modern poster layouts, and social campaigns.",
            "image": "projects/liquid.png",
            "url": "https://behance.net",
            "order": 4
        }
    ]
    for prj in projects:
        Project.objects.create(**prj)
    print("Created Projects.")
    
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()
