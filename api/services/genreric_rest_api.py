from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response


# generic method for get element By Id
def generic_get_by_id(request, table, serializer, _id):
    """
    This Method get one item from server and return Json response.

    table: It is an model class
    request: it is a {query_param} object
    serializer: It is a serializer class of  table(model class)
    id: It is a property using for search one Item from model class

    Implementation:
        from generic_rest_api import generic_get_by_id


        def get(self, request, format=None):
            return generic_get_by_id(request, table, serializer, "id")
    """
    id = request.query_params[_id]

    if id is not None:
        result = table.objects.get(id=id)
        # result = request.data
        serializer = serializer(instance=result, data=result, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Generic method for get all items from list items
def generic_get_all(table, queryset):
    """
    This Method get all items and return Jsson responce.

    table: It is an model class
    queryset: it is a {queryset} object

    Implementation:
        from generic_rest_api import generic_get_all


        def get(self, request, format=None):
            queryset = [class].objects.all()
            generic_get_all(queryset, [class], serializer, "id")
    """
    if len(queryset) > 0:
        return Response(queryset, status=status.HTTP_200_OK)
    return Response(
        {
            '{} Not Found': '{} Not exist'
            .format(table.__class__.__name__, table.__class__.__name__)
        },
        status=status.HTTP_404_NOT_FOUND
    )


# Generic method for add item in database
def generic_post(request, serialzer):
    """
    This Method POST data on server and return Jsson responce.


    [Params]:
    request: it is a {query_param} object
    serializer: It is a serializer class of  table(model class)

    [Implementation]:
        from generic_rest_api import generic_post


        def get(self, request, format=None):
            serializer = [class_serializer]
            generic_post(request, serialize)
    """
    serializer = serialzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
