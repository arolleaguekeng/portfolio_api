from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response


# generic method for get element By Id
def generic_get_by_id(request, table, serializer, _id):
    id = request.query_params[_id]

    if id is not None:
        result = table.objects.extra(
            where=[
                "{}=%s".format(_id)
            ], params=[id]
        )
        data = {}
        for i in range(len(result)):
            data[i] = serializer(result[i]).data
        return Response(data, status=status.HTTP_200_OK)


# Generic method for get all items from list items
def generic_get_all(table, queryset):
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
    serializer = serialzer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)