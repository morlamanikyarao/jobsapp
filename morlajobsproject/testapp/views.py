from django.shortcuts import render
from testapp.models import hydjobs,banglorejobs,punejobs

# Create your views here.
def index_view(request):
     return render(request,'testapp/index.html')

def hydjobs_view(request):
     jobs_list=hydjobs.objects.all()
     my_dict={'jobs_list':jobs_list}
     return render(request,'testapp/hydjobs.html',context=my_dict)


def banglorejobs_view(request):
     jobs_list=banglorejobs.objects.all()
     my_dict={'jobs_list':jobs_list}
     return render(request,'testapp/banglorejobs.html',context=my_dict)


def punejobs_view(request):
          jobs_list=punejobs.objects.all()
          my_dict={'jobs_list':jobs_list}
          return render(request,'testapp/punejobs.html',context=my_dict)
