from .models import *
from rest_framework import serializers, fields


class BookSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'published_date']
        # read_only_fields = ('author',)


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    # name = serializers.SerializerMethodField()
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
        
    def update(self, instance, validated_data):
        related_data = validated_data.pop('books', [])
        instance = super().update(instance, validated_data)

        self.update_related_object(instance, related_data)
   
        return instance
    
    def update_related_object(self, instance, books):
    
        # books_from_same_author = Books.objects.filter(id=instance.pk).values_list('id', flat=True)
        keep_choices = []
        for book in books:
            if "id" in book.keys():
                if Book.objects.filter(id=book["id"]).exists():
                    c = Book.objects.get(id=book["id"])
                    c.title = book.get('title', c.title)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = Book.objects.create(**book, author=instance)
                keep_choices.append(c.id)
        print(instance.books.count())
        print(instance.books.values_list('id', flat=True))
        if instance.books.exists():
            for book_id in instance.books.values_list('id', flat=True):
                if book_id not in keep_choices:
                    Book.objects.get(id=book_id).delete()

