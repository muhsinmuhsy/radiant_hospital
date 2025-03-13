from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import *

@receiver(post_migrate)
def create_dummy_data(sender, **kwargs):
    # Create dummy data for HomeAboutHero
    if HomeAboutHero.objects.count() == 0:
        HomeAboutHero.objects.create(
            title="This is the title for HomeAboutHero",
            description="This is the description for HomeAboutHero.",
            mini_text = "none",
            feature_one_name = "none",
            feature_one_description = "none",
            feature_two_name = "none",
            feature_two_description = "none",
        )
        
    # Create dummy data for HomeServiceHeader
    if HomeServiceHeader.objects.count() == 0:
        HomeServiceHeader.objects.create(
            title="This is the title for HomeServiceHeader",
            description="This is the description for HomeServiceHeader."
        )
        
    # Create dummy data for HomeConsultantHeader
    if HomeConsultantHeader.objects.count() == 0:
        HomeConsultantHeader.objects.create(
            title="This is the title for HomeConsultantHeader",
            description="This is the description for HomeConsultantHeader."
        )

    # Create dummy data for HomeSpecialitiesHeader
    if HomeSpecialitiesHeader.objects.count() == 0:
        HomeSpecialitiesHeader.objects.create(
            title="This is the title for HomeSpecialitiesHeader",
            description="This is the description for HomeSpecialitiesHeader."
        )

    # Create dummy data for SpecialitiesHero
    if SpecialitiesHero.objects.count() == 0:
        SpecialitiesHero.objects.create(
            simple_title="Simple Title",
            title="Specialities Hero Title",
            description="This is the description for SpecialitiesHero.",
            specialties_count="100+",
            surgeries_count="500+",
            years_exp_count="10+",
            image_badge_one="Top Rated",
            image_badge_two="Best in Class"
        )

    # Create dummy data for SpecialitiesMainHeader
    if SpecialitiesMainHeader.objects.count() == 0:
        SpecialitiesMainHeader.objects.create(
            title="Specialities Main Header",
            description="This is the description for SpecialitiesMainHeader."
        )

    # Create dummy data for ConsultantsMainHeader
    if ConsultantsMainHeader.objects.count() == 0:
        ConsultantsMainHeader.objects.create(
            title="Consultants Main Header",
            description="This is the description for ConsultantsMainHeader.",
            mini_description="A brief mini description."
        )

    # Create dummy data for ContactHero
    if ContactHero.objects.count() == 0:
        ContactHero.objects.create(
            title_one="Contact Us Today!",
            title_two="We Are Here To Help",
            description="This is the description for ContactHero."
        )

    # Create dummy data for QuickInfo
    if QuickInfo.objects.count() == 0:
        QuickInfo.objects.create(
            contact="+1 234 567 890",
            hours="Mon-Fri: 9 AM - 5 PM",
            location="123 Main Street, City, Country"
        )

    # Create dummy data for Mission
    if Mission.objects.count() == 0:
        Mission.objects.create(
            title="Our Mission",
            description="This is the description for Mission.",
            list=["Integrity", "Innovation", "Excellence"]
        )

    # Create dummy data for Vision
    if Vision.objects.count() == 0:
        Vision.objects.create(
            title="Our Vision",
            description="This is the description for Vision.",
            list=["Customer Satisfaction", "Global Reach", "Sustainability"]
        )

    # Create dummy data for ServiceHero
    if ServiceHero.objects.count() == 0:
        ServiceHero.objects.create(
            title="Service Hero Title",
            description="This is the description for ServiceHero."
        )

    # Create dummy data for CTAButton
    if CTAButton.objects.count() == 0:
        CTAButton.objects.create(
            single_title="Join Us Today",
            title="Take Action Now",
            description="This is the description for CTAButton."
        )
        
    if AboutHero.objects.count() == 0:
        AboutHero.objects.create(
            title="AboutHero Title",
            description="This is the description for AboutHero."
        )
        
    # Create dummy data for GetInTouch
    if GetInTouch.objects.count() == 0:
        GetInTouch.objects.create(
            location="123 Corporate Blvd, Suite 500, Business City",
            phone="+1 987 654 3210",
            email="contact@company.com",
            working_hours="Monday - Friday: 9 AM - 6 PM"
        )
