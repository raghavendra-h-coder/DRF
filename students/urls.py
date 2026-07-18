from django.urls import path

from students import views
from students.views import StudentAPIView, Student_ModelSerializerAPIView

urlpatterns = [
    path("students/", views.student_list, name="student_list"),
    path("students/drf/", StudentAPIView.as_view(), name="student_list_drf"),
    path("students/drf/modelserializer/", Student_ModelSerializerAPIView.as_view(), name="student_list_drf_modelserializer"),
]