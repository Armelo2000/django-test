from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'firstname', 'lastname']

class ProfileSerializer(serializers.ModelSerializer):
    person = PersonSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def update(self, instance, validated_data):
        person_data = validated_data.pop('person', None)
        if person_data:
            person = instance.person
            person.firstname = person_data.get('firstname', person.firstname)
            person.lastname = person_data.get('lastname', person.lastname)
            person.save()
        return super().update(instance, validated_data)
