from django.shortcuts import render, redirect
from django.contrib.auth import logout
from rest_framework import viewsets, permissions, authentication
from todos import models
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [authentication.SessionAuthentication, authentication.BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query_set = super().get_queryset()
        if self.request.user.is_authenticated:
            query_set = query_set.filter(created_by = self.request.user)
        return query_set

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

def Login(request):
    return render(request, 'Login.html')

def Register(request):
    return render(request, 'Register.html')

def Home(request):
    return render(request, 'Home.html')

def Logout(request):
    logout(request)
    return redirect('Login')