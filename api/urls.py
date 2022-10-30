from django.urls import path


from api.viewss.project_view import GetProjectById, GetAllProject

urlpatterns = [
    path('get-project/<str:id>', GetProjectById.as_view()),
    path(r'^blogpost/(?P<post_id>\w+)$', GetProjectById.as_view(),name='blogpost-list'),
    path('get-all-projects/', GetAllProject.as_view()),
]
