from django.contrib import admin
from django.urls import path

from django.urls import path

from employee import views
urlpatterns = [
    # ex: /employee/
    path("", views.IndexView.as_view(), name="employee"),
    # ex: /employee/5/
    path("positon/", views.PositionView.as_view(), name="positon"),
    # ex: /employee/5/vote/
    path("project/", views.PojectView.as_view(), name="project"),
    # ex: /employee/5/vote/
    path("project/<int:project_id>/", views.PojectdetailView.as_view(), name="projectdetail"),
    path("project/<int:id>/delete/", views.PojectView.as_view(), name="projectdel"),
    path("project/<int:project_id>/add_staff/<int:emp_id>/", views.PojectdetailView.as_view(), name="add_staff"),
    path("project/<int:project_id>/delete_staff/<int:emp_id>/", views.PojectdetailView.as_view(), name="delete_staff"),

]