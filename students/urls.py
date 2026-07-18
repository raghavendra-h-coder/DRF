from django.urls import path
from rest_framework.routers import DefaultRouter

from students import views
from students.views import StudentAPIView, Student_ModelSerializerAPIView, StudentDetailAPIView, StudentGenericAPIView, \
    StudentDetailGenericAPIView, StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView, StudentViewSet, \
    StudentModelViewSet, StudentPaginationAPIView

router = DefaultRouter()

router.register(
    r"students/modelviewset",
    StudentModelViewSet,
    basename="student-model-viewset"
)

router.register(
    r"students/viewset",
    StudentViewSet,
    basename="student-viewset"
)

urlpatterns = [
    path("students/", views.student_list, name="student_list"),
    path("students/drf/", StudentAPIView.as_view(), name="student_list_drf"),
    path("students/drf/paginate/", StudentPaginationAPIView.as_view(), name="student_list_paginate_drf"),
    path("students/drf/modelserializer/", Student_ModelSerializerAPIView.as_view(), name="student_list_drf_modelserializer"),
    path("students/<int:id>", StudentDetailAPIView.as_view(), name="student"),
    path("students/generic/", StudentGenericAPIView.as_view(), name="student_list_generic"),
    path("students/generic/<int:id>", StudentDetailGenericAPIView.as_view(), name="student_detail_list_generic"),
    path("students/listcreate/", StudentListCreateAPIView.as_view(), name="student_list_create"),
    path("students/retrieveupdatedestroy/<int:id>", StudentRetrieveUpdateDestroyAPIView.as_view(),
         name="student_retrieve_update_destroy"),

]

urlpatterns += router.urls