from rest_framework import generics

from api.models import Project
from api.services.genreric_rest_api import generic_get_all,generic_get_by_id

from api.serializers import ProjectSerializer


# Get All projects from server.
class GetAllProject(generics.ListAPIView):
    queryset = Project.objects.all()
    generic_get_all(table=Project, queryset=queryset)
    serializer_class = ProjectSerializer


class GetProjectById(generics.ListAPIView):
    serializer_class = ProjectSerializer

    # Get one project By Id.
    def get(self, request):
        return generic_get_by_id(
            request=request,
            table=Project,
            serializer=ProjectSerializer,
            _id="id"
        )
