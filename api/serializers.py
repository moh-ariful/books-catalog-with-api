from rest_framework import serializers
from buku.models import Book


class BookSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False)
    
    class Meta:
        fields = ('id', 'category', 'author_name','title', 'description', 'image','admin', 'published',)
        model = Book