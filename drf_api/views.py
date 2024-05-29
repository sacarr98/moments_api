from rest_framework.decorators import api_view
from rest_framework.response import responses


@api_view()
def rest_route(request):
    return Response({
        "message":"welcome to the drf API"
    })