from todo.models import Task
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import User
from rest_framework import permissions, viewsets, filters
from .serializers import TaskSerializer, UserSerializer
from rest_framework.exceptions import NotAuthenticated


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskAuthViewSet(viewsets.ModelViewSet):
    search_fields = ['title']
    filter_backends = (filters.SearchFilter,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise NotAuthenticated(detail='Sorry.You are not authenticated.')

        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


