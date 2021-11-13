from django import template

register = template.Library()

def range_filter(value):
    return value[0:500] + "........"

def range_filter_card(value):
    return value[0:100] + "."

register.filter('range_filter',range_filter)
register.filter('card_filter',range_filter_card)
