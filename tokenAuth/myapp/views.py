from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from jose import jwt
import jwt
import datetime
from myapp.models import UserProfile
from myapp.serializers import UserSerializer
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all users
    curl -X GET http://localhost:8000/api/tasks/
    Create a new user
    curl -X POST http://localhost:8000/api/tasks/ -d "username=ratul&password=jain"
    """

    if request.method == 'GET':
        users = UserProfile.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def user_detail(request, pk):
    """
    Generates a JWT for a given user. JWT expires after 5 mins
    http://localhost:8000/api/token/3
    """
    try:
        user = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        token = jwt.encode({'username': user.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=300)}, 'secret', algorithm='HS256')
        # token = jwt.encode({'username': user.username}, 'seKre8', algorithm='HS256')
        # print token
        response_data = {}
        response_data['token'] = token
        user.token_field = token
        user.save()
        serializer = UserSerializer(user)
        # return Response(serializer.data)
        return JsonResponse(response_data)

@api_view(['GET'])
def get_payload(request, pk):
    """
    http://localhost:8000/api/payload/3
    Get token for user
    """
    try:
        user = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        token = user.token_field
        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return Response({'detail' : "The token expired. Need to generate again"},
                     status = status.HTTP_401_UNAUTHORIZED)
        response_data = {}
        response_data['token'] = "token"

        return JsonResponse(payload)
