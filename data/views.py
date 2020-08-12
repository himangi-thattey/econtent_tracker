from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Downloads, Person, Content


class DownloadView(APIView):

    def post(self, request):
        data = request.data
        content = Content.objects.filter(content_slug=data.get('content_slug'), is_active=True)
        if not content.exists():
            return Response(data={"error": "This content does not exist"},
                            status=status.HTTP_400_BAD_REQUEST)
        content = content[0]
        person, created = Person.objects.get_or_create(uuid=data.get('uuid'))

        if not person.is_allowed:
            return Response(data={"error": "You are not allowed to access this content"},
                            status=status.HTTP_403_FORBIDDEN)

        downloadable_object, created = Downloads.objects.get_or_create(person=person, content=content)
        downloadable_object.downloads += 1
        downloadable_object.save()
        return Response(data={"url": content.drive_link}, status=status.HTTP_200_OK)
