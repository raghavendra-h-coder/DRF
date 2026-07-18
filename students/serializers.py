from rest_framework import serializers

from students.models import Student


class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    age = serializers.IntegerField()

    def validate_age(self, value):
        if value < 14:
            raise serializers.ValidationError(
                "Age must be at least 14."
            )

        return value

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def validate(self, attrs):
        age = attrs["age"]
        email = attrs["email"]
        if age < 21 and email.endswith("@company.com"):
            raise serializers.ValidationError(
                "Students below 21 cannot use a company email."
            )
        return attrs