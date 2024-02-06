from .models import *
from rest_framework import serializers, fields


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    class Meta:
        model = Author
        fields = '__all__'
        
    def update_test(self, instance, validated_data):
        children_data = validated_data.pop('books', [])
        instance = super().update(instance, validated_data)

        for child_data in children_data:
            child_instance, created = Book.objects.update_or_create(
                author=instance,
                # title=child_data['title'],  # Replace with actual field names
                # defaults={'title': child_data['title']},
                defaults={'title': child_data['title'], 'published_date': child_data['published_date']}
            )

        return instance

    def update(self, instance, validated_data):
        books = validated_data.pop('books')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        keep_choices = []
        for book in books:
            if "id" in book.keys():
                if Book.objects.filter(id=book["id"]).exists():
                    c = Book.objects.get(id=book["id"])
                    c.text = book.get('text', c.text)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = Book.objects.create(**book, question=instance)
                keep_choices.append(c.id)

        for book in instance.books:
            if book.id not in keep_choices:
                book.delete()

        return instance