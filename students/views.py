import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins, viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Student
from .pagination import StudentPagination
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

class StudentDetailAPIView(APIView):
    def get(self, request, id):
        student = get_object_or_404(
            Student,
            id=id
        )
        serializer = StudentModelSerializer(student)
        return Response(serializer.data)

    def put(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentModelSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(
            serializer.errors,
            status=400
        )

    def patch(self, request, id):
        student = get_object_or_404(Student, id=id)
        serializer = StudentModelSerializer(
            student,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        student = get_object_or_404(Student, id=id)
        student.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

class StudentGenericAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class StudentDetailGenericAPIView(
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"

    def put(self, request, *args, **kwargs):
        return self.update(request,*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request,*args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request,*args, **kwargs)


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer


class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    lookup_field = "id"
    lookup_url_kwarg = "id"

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        students = Student.objects.all()
        serializer = StudentModelSerializer(
            students,
            many=True
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentModelSerializer(student)
        return Response(serializer.data)

    def create(self, request):
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

    def update(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentModelSerializer(
            student,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def partial_update(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        serializer = StudentModelSerializer(
            student,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    pagination_class = StudentPagination
    permission_classes = [
        IsAuthenticated
    ]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["name"]
    ordering_fields = [
        "id",
        "age"
    ]
    filterset_fields = [
        "age",
        "email"
    ]

class StudentPaginationAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        paginator = StudentPagination()

        search = request.query_params.get("search")

        if search:
            students = students.filter(
                name__icontains=search
            )

        age = request.query_params.get("age")

        if age:
            students = students.filter(age=age)

        ordering = request.query_params.get("ordering")

        if ordering:
            students = students.order_by(ordering)

        page = paginator.paginate_queryset(
            students,
            request
        )

        serializer = StudentModelSerializer(
            page,
            many=True
        )
        return paginator.get_paginated_response(
            serializer.data
        )

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(
            serializer.errors,
            status=400
        )
