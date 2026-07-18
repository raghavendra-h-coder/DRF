from django.urls import path
from rest_framework.routers import DefaultRouter

from students import views
from students.views import StudentAPIView, Student_ModelSerializerAPIView, StudentDetailAPIView, StudentGenericAPIView, \
    StudentDetailGenericAPIView, StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView, StudentViewSet, \
    StudentModelViewSet, StudentPaginationAPIView

router = DefaultRouter()

router.register(
    r"modelviewset",
    StudentModelViewSet,
    basename="student-model-viewset"
)

router.register(
    r"viewset",
    StudentViewSet,
    basename="student-viewset"
)

urlpatterns = [
    path("", views.student_list, name="student_list"),
    path("drf/", StudentAPIView.as_view(), name="student_list_drf"),
    path("drf/paginate/", StudentPaginationAPIView.as_view(), name="student_list_paginate_drf"),
    path("drf/modelserializer/", Student_ModelSerializerAPIView.as_view(), name="student_list_drf_modelserializer"),
    path("<int:id>", StudentDetailAPIView.as_view(), name="student"),
    path("generic/", StudentGenericAPIView.as_view(), name="student_list_generic"),
    path("generic/<int:id>", StudentDetailGenericAPIView.as_view(), name="student_detail_list_generic"),
    path("listcreate/", StudentListCreateAPIView.as_view(), name="student_list_create"),
    path("retrieveupdatedestroy/<int:id>", StudentRetrieveUpdateDestroyAPIView.as_view(),
         name="student_retrieve_update_destroy"),

]

urlpatterns += router.urls