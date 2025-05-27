from rest_framework.views import APIView
from rest_framework.response import Response
from notes.models import Note
from .serializers import NoteSerializer

class CreateNoteList(APIView):
  def get(self, request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many = True)
    return Response(serializer.data)
  
  def post(self, request):
    serializer = NoteSerializer(data = request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors)