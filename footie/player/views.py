from django.shortcuts import render
from .models import Player
from common.util import response
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')  # Only needed if you're using CSRF protection
class PlayerView(View):
    # def post(self, request):
    #     # Handle POST request
    #     data = request.POST  # If form data is sent
    #     # or
    #     data = request.body  # If JSON data is sent
    #     # Process the data and save to the database
    #     # Example:
    #     YourModel.objects.create(**data)
    #     return JsonResponse({'message': 'Data saved successfully'}, status=201)
    
    # def put(self, request):
    #     # Handle PUT request
    #     data = request.body  # JSON data
    #     # Process the data and update the database
    #     # Example:
    #     YourModel.objects.filter(id=data['id']).update(**data)
    #     return JsonResponse({'message': 'Data updated successfully'})

    def get(self, request):
        players = Player.objects.all()
        return response(list(players), 200)
