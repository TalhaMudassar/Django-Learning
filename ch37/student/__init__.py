customfilter.py
from django import template  

# Step 1: Create a Library object to register filters
register = template.Library()

# Step 2: Define your filter function
def myreplace(value, args):
    """
    Custom filter to replace 'i am' with 'we are'
    value → the variable passed from template
    args → the string you want to replace
    """
    return value.replace(args, 'we are')

# Step 3: Register the filter
register.filter('iamToweare', myreplace)
