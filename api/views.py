from rest_framework import generics
from buku.models import Book
from .serializers import BookSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated


class BookList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
