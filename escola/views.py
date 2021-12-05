from rest_framework import serializers, viewsets, generics
from rest_framework.decorators import authentication_classes, permission_classes
from .models import Aluno, Curso, Matricula
from .serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaSerializer, ListaAlunosMatriculadosEmUmCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """" Exibindo todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """" Listando todas as matricular """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculaAluno(generics.ListAPIView):
    """"Listando as matriculas de um aluno ou aluna """
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id= self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
    """" Listando alunos matriculados em um curso """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosEmUmCursoSerializer