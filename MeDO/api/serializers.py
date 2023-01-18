from rest_framework import serializers
from todo.models import Task
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']


class TaskSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'task_status', 'created')