from django.shortcuts import render
from datetime import datetime, timedelta, timezone   # for expires example

# ------------------ SET COOKIE ------------------
def setcookie(request):
    # Rendering a response from template
    response = render(request, 'student/setcookie.html')
    
    # Store cookie with key='pay_id', value='pay123456'
    # max_age=3600 → cookie will expire after 1 hour (3600 seconds)
    response.set_cookie('pay_id', 'pay123456', max_age=3600)

    # Another way: use 'expires' → expire after 2 days
    # response.set_cookie('pay_id', 'ppp123',
    #                     expires=datetime.now(timezone.utc) + timedelta(days=2))

    return response


# ------------------ GET COOKIE ------------------
def getcookie(request):
    # Method 1 (Unsafe): Direct access – will throw KeyError if cookie does not exist
    # pay_id = request.COOKIES['pay_id']

    # Method 2 (Safe): Using .get() → returns None (or default) if cookie is missing
    pay_id = request.COOKIES.get('pay_id')  # returns value or None

    # Passing cookie value to template
    response = render(request, 'student/getcookie.html', {'pay_id': pay_id})
    return response


# ------------------ DELETE COOKIE ------------------
def delcookie(request):
    response = render(request, 'student/delcookie.html')
    # Delete cookie 'pay_id' from browser
    response.delete_cookie('pay_id')
    return response


# ------------------ SET SIGNED COOKIE ------------------
def setsignedcookie(request):
    response = render(request, 'student/setsignedcookie.html')
    # set_signed_cookie adds a "signature" for security
    # salt='tk' → adds extra layer so value can’t be tampered with
    response.set_signed_cookie('token', 'tk12345', salt='tk')
    return response


# ------------------ GET SIGNED COOKIE ------------------
def getsignedcookie(request):
    # get_signed_cookie verifies signature
    # If tampered → raises BadSignature error
    # default="guesttoken123" → returned if cookie missing
    token = request.get_signed_cookie('token',
                                      default="guesttoken123",
                                      salt='tk')
    return render(request, 'student/getsignedcookie.html', {'token': token})
