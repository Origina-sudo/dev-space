from django.shortcuts import render


rooms =[
    {"id":1,"name":"lets Learn Python!"},
    {"id":2,"name":"Design with me"},
    {"id":3,"name":"Frontend Developer!"},
]



# Create your views here.
def home(request):
    context = {"rooms" : rooms}
    return render(request,"home.html",context )

def room(request):
    return render(request, "room.html")
# ,{"rooms" : rooms})