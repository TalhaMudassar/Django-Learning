from django.shortcuts import render
from student.forms import Registration, login

# Registration view
def registration(req):
    # Default
    # fm = Registration()

    # Change field order
    fm = Registration(field_order=['email', 'city'])
    
    return render(req, 'student/registration.html', {'form': fm})


# Login view
def loginpage(req):
    # Different ways of customizing forms:

    # 1. auto_id=True  → default id="id_fieldname"
    # lp = login(auto_id=True)

    # 2. auto_id='id_%s' → id="id_email", id="id_passward"
    # lp = login(auto_id='id_%s')

    # 3. auto_id='talha_%s' → id="talha_email", id="talha_passward"
    # lp = login(auto_id='talha_%s')

    # 4. auto_id=False → No <label for=""> attribute connected to input
    # lp = login(auto_id=False)

    # 5. label_suffix='A' → Adds "A" after every label (e.g. "EmailA")
    # lp = login(label_suffix='A')

    # 6. label_suffix=' ' → Removes colon (default `:`), just space
    lp = login(label_suffix=' ')

    # 7. initial values → Pre-fill the form fields
    # lp = login(initial={'email': 'sonam@example.com', 'passward': '1234'})

    return render(req, 'student/login.html', {'loginform': lp})
