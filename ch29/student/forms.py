from django import forms
from django.core.validators import MinLengthValidator, RegexValidator

GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')]

INTERESTS_CHOICES = [
    ('tech', 'Technology'),
    ('art', 'Art'),
    ('sports', 'Sports')]

# Field Type Examples

# class DemoForm(forms.Form):
#     # Basic Fields
#     name = forms.CharField()
#     email = forms.EmailField()
#     pin_code = forms.IntegerField()

#     # Additional Field Types
#     age = forms.FloatField()
#     date_of_birth = forms.DateField()
#     appointment_time = forms.TimeField()
#     appointment_datetime = forms.DateTimeField()
#     is_subscribed = forms.BooleanField()
#     agree_terms = forms.NullBooleanField()

#     # Choice Fields
#     gender = forms.ChoiceField(choices=GENDER_CHOICES)
#     interests = forms.MultipleChoiceField(choices=INTERESTS_CHOICES)

#     # File and URL Fields
#     profile_image = forms.ImageField()
#     resume = forms.FileField()
#     website = forms.URLField()

#     # Other Specialized Fields
#     phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
#     password = forms.CharField(widget=forms.PasswordInput())
#     slug = forms.SlugField()
#     ip_address = forms.GenericIPAddressField()
#     rating = forms.DecimalField()




# Field Arguments Example

# class DemoForm(forms.Form):
#     # Basic Fields
#     name = forms.CharField(
#         label="Full Name",              # Sets label displayed next to the field
#         max_length=100,                 # Limits input length to 100 characters
#         # Sets the suffix after the label (default is ':')
#         label_suffix=":",
#         initial="Enter your full name",   # Sets an initial placeholder value
#         help_text="Enter your legal name here",  # Provides guidance for the user
#         # Validates that input has at least 3 characters
#         validators=[MinLengthValidator(3)]
#     )
#     email = forms.EmailField(
#         label="Email Address",        # Sets a user-friendly label for this email field
#         # Disables field input (useful for readonly fields)
#         disabled=True,
#     )
#     pin_code = forms.IntegerField(
#         label="Pin Code",            # Sets the field label
#         min_value=100000,            # Ensures minimum value is 100000
#         max_value=999999,             # Ensures maximum value is 999999
#         error_messages={                  # Custom error messages
#             'min_value': 'Pin code must be at least 6 digits.',
#             'max_value': 'Pin code can be at most 6 digits.'
#         }
#     )

#     # Additional Field Types
#     age = forms.FloatField(
#         label="Age",                 # Sets the label for the age field
#         min_value=0                  # Ensures a non-negative age
#     )
#     date_of_birth = forms.DateField(
#         label="Date of Birth",       # Sets label for date field
#         required=False,               # Field is optional
#         help_text="Enter your birth date in YYYY-MM-DD format"  # Guidance text
#     )
#     appointment_time = forms.TimeField(
#         label="Appointment Time",    # Sets label for time field
#         required=False               # Field is optional
#     )
#     appointment_datetime = forms.DateTimeField(
#         label="Appointment Date & Time",  # Sets label for datetime field
#         required=False               # Field is optional
#     )
#     is_subscribed = forms.BooleanField(
#         label="Subscribe to Newsletter",  # Sets label for boolean field
#         required=False               # Field is optional
#     )
#     agree_terms = forms.NullBooleanField(
#         label="Do you agree with terms?"  # Sets label for a three-state boolean field
#     )

#     # Choice Fields
#     gender = forms.ChoiceField(
#         label="Gender",              # Sets label for gender field
#         choices=GENDER_CHOICES
#     )
#     interests = forms.MultipleChoiceField(
#         label="Interests",           # Sets label for multiple-choice field
#         choices=INTERESTS_CHOICES,
#         required=False               # Field is optional
#     )

#     # File and URL Fields
#     profile_image = forms.ImageField(
#         label="Profile Image",       # Sets label for image upload
#         required=False               # Field is optional
#     )
#     resume = forms.FileField(
#         label="Upload Resume",       # Sets label for file upload
#         required=False               # Field is optional
#     )
#     website = forms.URLField(
#         label="Personal Website",    # Sets label for URL field
#         required=False               # Field is optional
#     )

#     # Other Specialized Fields
#     phone_number = forms.RegexField(
#         label="Phone Number",        # Sets label for phone number field
#         regex=r'^\+?1?\d{9,15}$',    # Regex pattern ensures valid phone format
#         error_messages={             # Custom error message if regex fails
#             'invalid': 'Enter a valid phone number, e.g., +123456789.'
#         }
#     )
#     password = forms.CharField(
#         label="Password",            # Sets label for password field
#         max_length=50,               # Limits input to 50 characters
#         widget=forms.PasswordInput(),  # Masks input for password security
#         # Minimum length validation for password
#         validators=[MinLengthValidator(8)],
#         # Custom error
#         error_messages={
#             'min_length': 'Password must be at least 8 characters long.'}
#     )
#     slug = forms.SlugField(
#         label="Slug",                # Sets label for slug field
#         max_length=50                # Limits slug input to 50 characters
#     )
#     ip_address = forms.GenericIPAddressField(
#         label="IP Address",          # Sets label for IP address field
#         protocol='both',             # Allows both IPv4 and IPv6 addresses
#         unpack_ipv4=False,           # Maintains IPv4 addresses in standard form
#         localize=True,              # Formats the IP address according to locale
#     )
#     rating = forms.DecimalField(
#         label="Rating",              # Sets label for decimal field
#         max_digits=3,                # Allows up to 3 total digits, e.g., 9.5
#         decimal_places=1,            # Specifies 1 decimal place for rating
#         min_value=0,                 # Sets minimum allowed value
#         max_value=10,                # Sets maximum allowed value
#         initial=5.0,                 # Sets an initial rating value
#         help_text="Provide a rating between 0 and 10",
#         localize=True        # Localizes the number format based on user locale
#     )

# Widget Example
class DemoForm(forms.Form):
    # Text Input Widgets
    name = forms.CharField(
        # Basic text input widget
        widget=forms.TextInput(
            attrs={'placeholder': 'Type here...', 'class': 'mycss'}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'placeholder': 'Enter password'})  # Password widget
    )
    key = forms.CharField(
        # Hidden input widget for storing non-visible data
        widget=forms.HiddenInput()
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'name@example.com'})  # Email widget
    )
    URL = forms.URLField(
        widget=forms.URLInput(
            attrs={'placeholder': 'https://example.com'})  # URL widget
    )
    pin_code = forms.IntegerField(
        # Number input with min/max attributes
        widget=forms.NumberInput(attrs={'min': '0', 'max': '100'})
    )
    DOB = forms.DateField(
        # Date widget with placeholder
        widget=forms.DateInput(
            attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'})
    )
    meeting_time = forms.TimeField(
        # Time widget with placeholder
        widget=forms.TimeInput(
            attrs={'type': 'time', 'placeholder': 'HH:MM:SS'})
    )
    datetime_field = forms.DateTimeField(
        # DateTime input field for both date and time
        label="DateTime Field",
        widget=forms.DateTimeInput(
            # DateTime widget
            attrs={'type': 'datetime-local', 'placeholder': 'YYYY-MM-DD HH:MM:SS'})
    )

    # Textarea Widget
    post_content = forms.CharField(
        widget=forms.Textarea(
            # Textarea widget
            attrs={'placeholder': 'Enter multiple lines of text...'})
    )

    # Checkbox Widgets
    boolean_field = forms.BooleanField(
        label="Boolean Field",                        # Checkbox for true/false input
        widget=forms.CheckboxInput()                  # Checkbox widget
    )
    null_boolean_field = forms.NullBooleanField(
        # Allows for three states: True, False, or Unknown
        label="Null Boolean Field",
        # Dropdown with Yes, No, Unknown options
        widget=forms.NullBooleanSelect()
    )

    # Select Widgets
    choice_field = forms.ChoiceField(
        label="Choice Field",                         # Single choice from dropdown
        choices=GENDER_CHOICES,
        widget=forms.Select()                         # Standard dropdown selection widget
    )
    multiple_choice_field = forms.MultipleChoiceField(
        # Allows selection of multiple options
        label="Multiple Choice Field",
        choices=INTERESTS_CHOICES,
        widget=forms.SelectMultiple()                 # Multi-select dropdown widget
    )
    radio_choice_field = forms.ChoiceField(
        label="Radio Choice Field",                   # Single choice with radio buttons
        choices=GENDER_CHOICES,
        widget=forms.RadioSelect()                    # Radio button widget
    )

    # File Upload Widgets
    file_field = forms.FileField(
        label="File Field",                           # File upload input
        widget=forms.FileInput()                      # Basic file upload widget
    )
    image_field = forms.ImageField(
        label="Image Field",                          # Image file upload input
        # File upload with option to clear existing file
        widget=forms.ClearableFileInput()
    )

    # Other Specialized Widgets
    slug_field = forms.SlugField(
        # Slug (URL-friendly) input field
        label="Slug Field",
        # Text input with slug format suggestion
        widget=forms.TextInput(attrs={'placeholder': 'my-slug'})
    )
    ip_address_field = forms.GenericIPAddressField(
        label="IP Address Field",                     # Input for IPv4 or IPv6 addresses
        # Text input with IP format suggestion
        widget=forms.TextInput(attrs={'placeholder': '127.0.0.1'})
    )
    time_duration_field = forms.DurationField(
        label="Duration Field",                       # Input for time duration
        # Text input with duration placeholder
        widget=forms.TextInput(attrs={'placeholder': 'hh:mm:ss'})
    )
    decimal_field = forms.DecimalField(
        label="Decimal Field",                        # Decimal number input
        max_digits=5,                                 # Maximum number of total digits
        decimal_places=2,                             # Number of digits after the decimal
        # Number input with step size for increments
        widget=forms.NumberInput(attrs={'step': '0.1'})
    )

    # MultiWidgets
    split_date_time = forms.SplitDateTimeField(
        # Date and time input split into separate fields
        label="Split Date and Time Field",
        # Widget that provides two fields for date and time
        widget=forms.SplitDateTimeWidget()
    )
    split_hidden_date_time = forms.SplitDateTimeField(
        # Hidden version of SplitDateTimeField
        label="Hidden DateTime Field",
        widget=forms.SplitHiddenDateTimeWidget()      # Hidden widget for split datetime
    )
