from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import User, Class, Assignment, Question
from .serializers import UserSerializer, ClassSerializer, AssignmentSerializer, QuestionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  

class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == 'teacher':
                return Assignment.objects.filter(created_by=user)
            elif user.role == 'student':
                enrolled_classes = user.enrolled_classes.all()
                return Assignment.objects.filter(cls__in=enrolled_classes)
        return Assignment.objects.none() 

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == 'teacher':
                assignments = Assignment.objects.filter(created_by=user)
                return Question.objects.filter(assignment__in=assignments)
            elif user.role == 'student':
                enrolled_classes = user.enrolled_classes.all()
                assignments = Assignment.objects.filter(cls__in=enrolled_classes)
                return Question.objects.filter(assignment__in=assignments)
        return Question.objects.none() 
