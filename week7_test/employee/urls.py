from django.urls import path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("position/", views.PositionView.as_view(), name="position"),
    path("project/", views.ProjectView.as_view(), name="project"),
    path("project/<int:project_id>/delete/", views.ProjectView.as_view(), name="project_delete"),
    path("project/<int:project_id>/", views.ProjectDetailView.as_view(), name="project_detail"),
    path("project/<int:project_id>/remove/<int:emp_id>/", views.ProjectDetailView.as_view(), name="project_removeStaff"),
    path("project/<int:project_id>/add/<int:emp_id>/", views.ProjectDetailView.as_view(), name="project_addStaff"),
    # path("articles/<int:year>/", views.year_archive),
    # path("articles/<int:year>/<int:month>/", views.month_archive),
    # path("articles/<int:year>/<int:month>/<slug:slug>/", views.article_detail),
]