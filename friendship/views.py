from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from .models import Friendship
from .serializers import UserListSerializer

User = get_user_model()


class UserListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        q = request.query_param.get('q')
        if q:
            users = User.objects.filter(username__icontains=q)
        else:
            users = User.objects.all()
        users = User.objects.filter(is_superuser=False, is_staff=False, is_active=True)
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class RquestView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        Friendship.objects.create(requets_from=request.user, requets_to=user)

        return Response({'detail': 'Request sent'}, status=status.HTTP_201_CREATED)
    

class RequestListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        friendship = Friendship.objects.filter(requets_to=request.user, is_accepted=False)
        users = [fr.requets_from for fr in friendship]
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class AcceptView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user_id = request.data.get('user')

        try:
            user = User.objects.get(pk=user_id)
            friendship = Friendship.objects.get(requets_from=user, requets_to=request.user, is_accepted=False)
        except (User.DoesNotExist, Friendship.DoesNotExist):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        friendship.is_accepted = True
        friendship.save()

        return Response({'detail': 'Connected'})
    

class FriendListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        friendship = Friendship.objects.filter(
            Q(request_from=request.user) | Q(request_to=request.user),
            is_accepted=True,
        )
        users = [fr.requets_from for fr in friendship]
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)
    
