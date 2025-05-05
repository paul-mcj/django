from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def rounded_timesince(value):
    if not value:
        return ""

    now = timezone.now()

    # Make sure both datetimes are timezone-aware
    if timezone.is_naive(value):
        value = timezone.make_aware(value)

    delta = now - value
    seconds = delta.total_seconds()

    if seconds < 3600:
        minutes = int(seconds // 60)
        return f"{minutes} minute{'s' if minutes != 1 else ''} ago"
    elif seconds < 86400:
        hours = int(seconds // 3600)
        return f"{hours} hour{'s' if hours != 1 else ''} ago"
    elif seconds < 604800:
        days = int(seconds // 86400)
        return f"{days} day{'s' if days != 1 else ''} ago"
    elif seconds < 2592000:
        weeks = int(seconds // 604800)
        return f"{weeks} week{'s' if weeks != 1 else ''} ago"
    else:
        months = int(seconds // 2592000)
        return f"{months} month{'s' if months != 1 else ''} ago"
