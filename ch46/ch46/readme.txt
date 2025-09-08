response.set_cookie(
    key,                  # (Required) The name of the cookie (e.g., "username", "session_id").
    value='',              # (Optional) The value you want to store. Default is an empty string.
    
    max_age=None,          # (Optional) Cookie lifetime in seconds.
                           # Example: max_age=60*60*24*2  → cookie will last for 2 days.
    
    expires=None,          # (Optional) Expiration date/time for the cookie.
                           # Example: expires=datetime.utcnow() + timedelta(days=2)
                           # If both max_age and expires are given, max_age has priority.
    
    path='/',              # (Optional) URL path for which the cookie is valid.
                           # Default '/' means cookie is available for the entire site.
                           # Example: path='/home' → only accessible under /home URLs.
    
    domain=None,           # (Optional) Domain for which the cookie is valid.
                           # Example: domain="geekyshows.com" → works for that domain.
    
    secure=False,          # (Optional) If True → cookie only sent via HTTPS (secure connection).
                           # Prevents leakage over HTTP.
    
    httponly=False,        # (Optional) If True → cookie is **not accessible via JavaScript**.
                           # Helps protect against XSS (cross-site scripting) attacks.
    
    samesite=None          # (Optional) Restricts cross-site cookie sending.
                           # Options:
                           #   'Lax'   → cookies sent only for safe cross-site requests (default in Django 3.1+).
                           #   'Strict'→ cookies sent only from the same site (more secure).
                           #   'None'  → cookies sent in all requests, but must be Secure=True.
)
