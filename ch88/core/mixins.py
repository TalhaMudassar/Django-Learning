from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.shortcuts import redirect

erro_403_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>403 Forbidden</title>
    <style>
        /* General Styles */
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f3f4f6;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background-color: #ffffff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
            text-align: center;
            padding: 30px;
            max-width: 400px;
            width: 100%;
        }

        h1 {
            font-size: 32px;
            color: #e3342f;
            margin-bottom: 20px;
        }

        p {
            font-size: 16px;
            color: #4a4a4a;
            margin-bottom: 20px;
        }

        a {
            display: inline-block;
            padding: 12px 24px;
            background-color: #3490dc;
            color: #ffffff;
            font-weight: bold;
            text-decoration: none;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            transition: background-color 0.3s, box-shadow 0.3s;
        }

        a:hover {
            background-color: #2779bd;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>403 - Access Forbidden</h1>
        <p>Sorry, you are not authorized to access this page.</p>
        <a href="/">Return to Home</a>
    </div>
</body>
</html>

"""

class IsCustomerMixin(UserPassesTestMixin):
  def test_func(self):
    return self.request.user.is_authenticated and hasattr(self.request.user, 'is_customer') and self.request.user.is_customer
  
  def handle_no_permission(self):
    if self.request.user.is_authenticated:
      return HttpResponseForbidden(erro_403_html)
    return redirect('login')

class IsSellerMixin(UserPassesTestMixin):
  def test_func(self):
    return self.request.user.is_authenticated and hasattr(self.request.user, 'is_seller') and self.request.user.is_seller
  
  def handle_no_permission(self):
    if self.request.user.is_authenticated:
      return HttpResponseForbidden(erro_403_html)
    return redirect('login')
  