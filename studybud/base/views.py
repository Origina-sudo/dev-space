from django.shortcuts import render


rooms =[
    {"id":1,"name":"lets Learn Python!"},
    {"id":2,"name":"Design with me"},
    {"id":3,"name":"Frontend Developer!"},
]



# Create your views here.
def home(request):
    context = {"rooms" : rooms}
    return render(request,"base/home.html",context )

def room(request):
    return render(request, "base/room.html")
# ,{"rooms" : rooms})