from django.db.models import fields
from rest_framework import serializers
from .models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'descricao', 'nivel']

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = ['id']

class ListaMatriculaSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display

class ListaAlunosMatriculadosEmUmCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source = 'alunos.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']