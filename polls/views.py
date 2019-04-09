from django.shortcuts import render
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import Question, Choice
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly, DidOwnerCreateQuestion
from .serializer import QuestionSerializer, ChoiceSerializer


# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


question_list = QuestionViewSet.as_view({ 'get': 'list', 'post': 'create' })
question_detail = QuestionViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy' })


class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


choices_list = ChoiceViewSet.as_view({ 'get': 'list', 'post': 'create' })
choices_detail = ChoiceViewSet.as_view({ 'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy' })