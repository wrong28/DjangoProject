from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):

	'''This cuts all the values of "arg" from the string'''

	return value.replace(arg,'My')

#register.filter('cut',cut)

