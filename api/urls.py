from django.urls import path


from api.views_.project_view import GetProjectById, GetAllProject

urlpatterns = [
    path('get-project/<str:id>', GetProjectById.as_view()),
    path('get-all-projects/', GetAllProject.as_view()),
]
