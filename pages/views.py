from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from django.core.paginator import Paginator
from realtors.models import Realtor
from listings.choices import price_choices,bedroom_choices,state_choices

def index(request):
    about=Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(about, 3)
    page_number = request.GET.get('page')
    paged_about = paginator.get_page(page_number)
    contest={
        'about' : paged_about,
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedroom_choices':bedroom_choices,
    }
    return render(request ,'pages/index.html',contest)
def about(request):
    real = Realtor.objects.order_by("-hire_date")
    mvp_real=Realtor.objects.all().filter(is_mvp=True)
    context= { 
        'real': real,
        'mvp_real' : mvp_real
    }
    return render(request ,'pages/about.html',context) 
