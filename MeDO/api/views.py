from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request):
    return Response({
        'List': '/task-list/',
        'Detail': '/task-detail/<int:pk>/',
        'Create': '/task-create/',
        'Update': 'task-update/<int:pk>/',
        'Delete': 'task-delete/<int:pk>/',
})
