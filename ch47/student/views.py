from django.shortcuts import render
from datetime import datetime, timedelta, timezone

def setsession(request):
    # Store values in the session (just like key-value pairs in a dictionary)
    request.session['fname'] = 'talha'
    request.session['lname'] = 'mudassar'
    # Now session contains something like: {'fname': 'talha', 'lname': 'mudassar'}

    # Control how long the session should last:
    
    # Option 1 → Uncomment this to make the session expire after 10 seconds
    # request.session.set_expiry(10)  
    
    # Option 2 → If expiry = 0, the session will expire when the browser is closed
    request.session.set_expiry(0)

    # Render response and save session data
    return render(request, 'student/setsession.html')
 
def getsession(request):
    # first_name = request.session['fname'] # method 1 to get the session
    first_name = request.session.get('fname') # second method to get the session its also work 
    last_name = request.session.get('lname')
    #  first_name = request.session.get('fname', 'Guest') # here we use for default value if fname are empty it shows default value 
    return render(request, 'student/getsession.html',{'first_name':first_name,'last_name':last_name})

def delsession(request):
    if 'fname' in request.session:  # use  if condition beucause if session not exist it shows error 
        del request.session['fname']
        del request.session['lname']
    return render(request, 'student/delsession.html')

def flushsession(request):
    request.session.flush() #We use this when we want to ensure that the previous session data cannot be accessed by the user
    # use case : we use this when user logout or other like if user logout so we use this to flush all their session data 
    return render(request, 'student/flushsession.html')

def sessionmethodsinview(request):
    # Access all the keys stored in the current session
    key = request.session.keys()  
    print(key)  
    # Example Output: dict_keys(['fname', 'lname'])  
    # We use this when we only want the keys (like dictionary keys).

    # Access both keys and values stored in the session
    items = request.session.items()  
    print(items)  
    # Example Output: dict_items([('fname', 'talha'), ('lname', 'mudassar')])  
    # We use this when we need both keys and values together.

    # setdefault() → If 'age' exists, return its value. If not, set it to 31.
    age = request.session.setdefault('age', 31)  
    print(age)  
    # Example: If session has {'age': 25}, it will print 25.  
    # If 'age' is not in session, it will create {'age': 31} and print 31.

    # Returns the default age (in seconds) for session cookies from settings.py (SESSION_COOKIE_AGE).
    session_cookies_age = request.session.get_session_cookie_age()  
    print("session cookie age", session_cookies_age)  
    # Useful for checking how long session cookies last (default = 1209600 seconds = 2 weeks).

    # Returns how many seconds until the session expires.
    expire_age = request.session.get_expiry_age()  
    print("Expire age", expire_age)  
    # Helpful if you want to know remaining time before session deletion.

    # Returns the exact date & time when the session will expire.
    expiry_date = request.session.get_expiry_date()  
    print("Expire date", expiry_date)  
    # Good for logging or reminding users when their session will end.

    # Returns True if the session will expire when the browser is closed.
    expire_at_browser_close = request.session.get_expire_at_browser_close()  
    print("Expire at browser", expire_at_browser_close)  
    # Useful when SESSION_EXPIRE_AT_BROWSER_CLOSE = True in settings.py.

    # Sending data to template for display
    return render(request, 'student/sessionmethodsinview.html', {
        'key': key,
        'items': items,
        'age': age,
        'session_cookies_age': session_cookies_age,
        'expire_age': expire_age,
        'expiry_date': expiry_date,
        'expire_at_browser_close': expire_at_browser_close,
    })



def sessionclear(request):
    request.session.clear_expired() # If we want to remove the expired data, we use clear_expired."
    return render(request, 'student/sessionclear.html')

def sessionmethodsintemplate(request):
    keys= request.session.keys()
    items = request.session.items()
    
    return render(request, 'student/sessionmethodsintemplate.html',{'keys':keys,'items':items})


# here some method to check either user browser can support  set or get cookies or not 
def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'student/settestcookie.html')

def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request, 'student/checktestcookie.html')

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'student/deltestcookie.html')
