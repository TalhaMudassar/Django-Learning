<!doctype html>
<html>
<head><meta charset="utf-8"><title>Home page</title></head>
<body>
  <h1>Home page</h1>

  <ul>
    <!-- Default str route -->
    <li><a href="{% url 'profile_default_str' 'abc' %}">Profile 'abc' (str)</a></li>

    <!-- int route -->
    <li><a href="{% url 'profile_int' 1 %}">Student 1</a></li>
    <li><a href="{% url 'profile_int' my_id=2 %}">Student 2</a></li>

    <!-- slug route -->
    <li><a href="{% url 'profile_slug' title='master-django-in-10' %}">Slug: master-django-in-10</a></li>

    <!-- two-parameter route -->
    <li><a href="{% url 'profile_two' 5 10 %}">Class 5, Student 10</a></li>
    <li><a href="{% url 'profile_two' my_class=3 my_id=2 %}">Class 3, Student 2</a></li>

    <!-- custom converter route -->
    <li><a href="{% url 'profile_year' 2003 %}">Year 2003</a></li>
  </ul>
</body>
</html>
templates/student/profile.html
<!doctype html>
<html>
<head><meta charset="utf-8"><title>Profile page</title></head>
<body>
  <h1>Profile page</h1>

  {% if id %}<h2>Student id: {{ id }}</h2>{% endif %}
  {% if class %}<h2>Class: {{ class }}</h2>{% endif %}
  {% if my_id %}<h2>my_id: {{ my_id }}</h2>{% endif %}
  {% if title %}<h2>Slug title: {{ title }}</h2>{% endif %}
  {% if year %}<h2>Year: {{ year }}</h2>{% endif %}
</body>
</html>
