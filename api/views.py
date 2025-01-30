from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .models import Professor
from .serializers import ProfessorSerializer
from rest_framework import status 

@api_view(['GET', 'POST'])

def listar_professores(request):
    if request.method == "GET":
        queryset = Professor.objects.all()
        serializer = ProfessorSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfessorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)



class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [IsAuthenticated] 

class ProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    lookup_field = 'pk'
