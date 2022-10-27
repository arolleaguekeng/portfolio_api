from rest_framework import generics

from api.models import Project
from api.services.genreric_rest_api import generic_get_all,generic_get_by_id

from api.serializers import ProjectSerializer


class getAllProject(generics.ListAPIView):
    queryset = Project.objects.all().order_by('created_ad')
    generic_get_all(table=Project, queryset=queryset)
    serializer_class = ProjectSerializer


class getProjectById(generics.ListAPIView):
    serializer_class = ProjectSerializer
    def get(self, request):
        return generic_get_by_id(request=request, table=Project, serializer=ProjectSerializer, _id="id")
