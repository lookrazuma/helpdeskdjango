from django.shortcuts import render
from .models import userManual
from django.views.generic.base import View
# Create your views here.


class userManualView(View):
    
    def get(self, request):
        manual = userManual.objects.all()
        return render(request, "userManual/manual.html", {"manual_list": manual})

    # def post(self, request, *args, **kwargs):
    #     return HttpResponse('POST request!')