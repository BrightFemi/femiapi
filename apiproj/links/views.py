from rest_framework import generics
from .models import Link
from .serializers import LinkSerializer


class PostListApi(generics.ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class PostCreateApi(generics.CreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class PostDetailApi(generics.RetrieveAPIView):
    queryset = Link.objects.all()

class PostUpdateApi(generics.UpdateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class PostDeleteApi(generics.DestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer