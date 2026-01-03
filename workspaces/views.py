from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Workspace,WorkspaceMember
from .serializers import WorkspaceSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_workspace(request):
    name = request.data.get('name')
    if not name:
        return Response({'error': 'name is required'}, status=400)

    workspace = Workspace.objects.create(
        name=name,
        owner=request.user
    )

    WorkspaceMember.objects.create(
        workspace=workspace,
        user=request.user,
        role='ADMIN'
    )

    return Response(WorkspaceSerializer(workspace).data, status=201)

