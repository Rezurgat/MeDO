from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'task_status', 'created')