from django import template
from coplate.models import ClubApplication

register = template.Library()

@register.filter
def user_already_applied(user, club_name):
    return ClubApplication.objects.filter(user=user, club_name=club_name).exists()