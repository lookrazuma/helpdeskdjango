from django.shortcuts import render, redirect, reverse
from .forms import *
from .models import * 


class ObjUpdateMixin:
    data = None
    model_form = None
    template = None

    def get(self, request, obj_id):
        data_obj = self.data.objects.get(pk=obj_id)
        bound_form = self.model_form(instance=data_obj)
        return render(request, self.template, context={'form': bound_form, 'obj': data_obj})

    def post(self, request, obj_id):
        data_obj = self.data.objects.get(pk=obj_id)
        bound_form = self.model_form(request.POST, instance=data_obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, 'obj': data_obj})

class ObjDeleteMixin:
    data = None
    template = None
    reverse_url = None
    def get(self, request, obj_id):
        data_obj = self.data.objects.get(pk=obj_id)
        return render(request, self.template, context={'obj': data_obj})

    def post(self, request, obj_id):
        data_obj = self.data.objects.get(pk=obj_id)
        data_obj.delete()
        return redirect(reverse(self.reverse_url))