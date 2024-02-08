# views.py

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import generics

class AuthorUpdateView_Old(APIView):
    def put(self, request, author_id):
        author = get_object_or_404(Author, pk=author_id)
        author_serializer = AuthorSerializer(instance=author, data=request.data)

        if author_serializer.is_valid():
            # Update author information
            author_serializer.save()

            # Update or create books
            books_data = request.data.get('books', [])
            for book_data in books_data:
                book_id = book_data.get('id')
                if book_id:
                    # If book_id is provided, update the existing book
                    book = get_object_or_404(Book, pk=book_id, author=author)
                    book_serializer = BookSerializer(instance=book, data=book_data)
                else:
                    # If no book_id is provided, create a new book
                    book_serializer = BookSerializer(data=book_data)

                if book_serializer.is_valid():
                    book_serializer.save()
                else:
                    return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            return Response({'message': 'Author and books updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'

    def update2(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)