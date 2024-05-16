from rest_framework.response import Response
from rest_framework.decorators import api_view
from auth.jwt import validate_jwt
from player.models import Player
import bcrypt
from datetime import datetime, timedelta
import jwt

@api_view(['POST'])
def login(request):
    player = Player.objects.filter(email = request.data["email"]).first()
    if not player:
        return Response({"message": 'Could not verify User does not exist !!'}, status=401)

    if bcrypt.hashpw(request.data["password"], player.password):
        token = jwt.encode({ 'user_id': player.id, 'exp' : datetime.utcnow() + timedelta(minutes = 30)}, "secret")
        return Response({"data": token},status=201)
    
    return Response({"message":  "Could not verify Wrong Password !!"}, status=403)

@api_view(['POST'])
def register(request):
    player = Player.objects.filter(email = request.data["email"]).first()
    if not player:
        hashed = bcrypt.hashpw(request.data["password"], bcrypt.gensalt(2))
        user = Player(email = request.data["email"], password = hashed)
        user.save()
        return Response({"message":  "Successfully sign up"}, status=201)
    else:
        return Response({"message":  "User already exist"}, status=400)