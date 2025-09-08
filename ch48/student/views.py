from django.shortcuts import render

def setsession(request):
 request.session['fname'] = 'Sonam'
 request.session['lname'] = 'Kumari'
 return render(request, 'student/setsession.html')
 
def getsession(request):
 first_name = request.session.get('fname')
 last_name = request.session.get('lname')
 return render(request, 'student/getsession.html', {'first_name':first_name, 'last_name':last_name})

def sessionclear(request):
  request.session.flush()
  request.session.clear_expired()
  return render(request, 'student/sessionclear.html')
