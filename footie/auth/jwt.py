import jwt
from django.http import JsonResponse
from django.conf import settings

def validate_jwt(view_func):
    def wrapper(request, *args, **kwargs):
        # Get the Authorization header from the request
        auth_header = request.headers.get('Authorization')
        
        # Check if the Authorization header exists and has the expected format
        if not auth_header or 'Bearer ' not in auth_header:
            return JsonResponse({'error': 'Authorization header missing or invalid'}, status=401)
        
        # Extract the token from the Authorization header
        token = auth_header.split(' ')[1]
       
        try:
            # Validate the JWT token
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            # You can now access the payload, such as payload['username'], payload['user_id'], etc.
            # You can also perform additional checks here if needed
            
            # Call the view function with the validated token
            return view_func(request, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            # Handle expired token
            return JsonResponse({'error': 'Token has expired'}, status=401)
        except jwt.InvalidTokenError:
            # Handle invalid token
            return JsonResponse({'error': 'Invalid token'}, status=401)
    
    return wrapper