import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Student
from .serializers import StudentSerializer, StudentModelSerializer


@csrf_exempt
def student_list(request):

    if request.method == "GET":
        students = Student.objects.all()

        data = []

        for student in students:

            data.append({
                "id": student.id,
                "name": student.name,
                "email": student.email,
                "age": student.age,
            })

        return JsonResponse(data, safe=False)

    if request.method == "POST":
        body = json.loads(request.body)
        name = body["name"]
        email = body["email"]
        age = body["age"]

        Student.objects.create(
            name=name,
            email=email,
            age=age
        )

        return JsonResponse(
            {"message": "Student created"},
            status=201

        )

class StudentAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(
            students,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(
            serializer.errors,
            status=400
        )

class Student_ModelSerializerAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentModelSerializer(
            students,
            many=True
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentModelSerializer(
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
