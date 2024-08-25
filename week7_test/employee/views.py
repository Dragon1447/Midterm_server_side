from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


from .models import *


class IndexView(View):
    def get(self, request):
        emp_list = Employee.objects.order_by("id")
        emp_num = emp_list.count()
        context = {
            "emp_list": emp_list,
            "emp_num": emp_num
        }
        return render(request, "employee.html", context)

# Leave the rest of the views (detail, results, vote) unchanged

class PositionView(View):
    def get(self, request):
        pos_list = Position.objects.order_by("id")
        context = {
            "pos_list": pos_list,
        }
        return render(request, "position.html", context)

class ProjectView(View):
    def get(self, request):
        pro_list = Project.objects.order_by("id")
        context = {
            "pro_list": pro_list,
        }
        return render(request, "project.html", context)
    
    def delete(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        project.delete()
        return JsonResponse({'foo':'bar'}, status=200)

class ProjectDetailView(View):
    def get(self, request, project_id):
        project = Project.objects.get(pk=project_id)
        due_date = project.due_date.strftime("%Y-%m-%d")
        start_date = project.start_date.strftime("%Y-%m-%d")
        staff_project = Employee.objects.filter(project=project)
        context = {
            "project": project,
            "due_date": due_date,
            "start_date": start_date,
            "staff_project": staff_project
        }
        return render(request, "project_detail.html", context)

    def delete(self, request, project_id, emp_id):
        project = Project.objects.get(pk=project_id)
        emp = Employee.objects.get(pk=emp_id)
        project.staff.remove(emp)
        project.save()
        return JsonResponse({'foo':'bar'}, status=200)

    def put(self, request, project_id, emp_id):
        project = Project.objects.get(pk=project_id)
        emp = Employee.objects.get(pk=emp_id)
        project.staff.add(emp)
        project.save()
        return JsonResponse({'foo':'bar'}, status=200)