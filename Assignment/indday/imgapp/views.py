from django.shortcuts import render

# Create your views here.
def land_page(request):
    section_name = 'Page 1'
    return render(request,'imgapp/index.html',{'section_name': section_name})
def second_page(request):
    cards = [
        {'id':1,'card-title':'Card 1','card-description':'First Description'},
        {'id':2,'card-title':'Card 2','card-description':'Second Description'},
        {'id':3,'card-title':'Card 3','card-description':'Third Description'},
    ]
    return render(request,'includes/cards.html',{'cards':cards})
def detail_page(request,c_id):
    return render(request,'imgapp/detail.html')