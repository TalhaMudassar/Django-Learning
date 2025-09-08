from django import template
register = template.Library()

#without decorator
def myreplace(value,args):
    return value.replace(args,'we are')

register.filter('iamToweare',myreplace)

#with decorator
@register.filer(name='iamToweare')
def myreplace(value,args):
    return value.replace(args,'we are')
