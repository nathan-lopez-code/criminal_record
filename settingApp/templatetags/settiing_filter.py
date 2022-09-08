from django import template

register = template.Library()


@register.filter
def get_last_crime(o):
    crime = o.crime_set.all()[:1][0]
    return 'condamné le {} pour {}'.format(crime.dateCondamnation, crime.descriptionCrime)


@register.filter
def comp(liste):
    return len(liste)