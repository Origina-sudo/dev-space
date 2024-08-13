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

def room(request, pk):
    room = None
    for i in rooms :
        if i['id'] == int(pk):
            room = i
    context = {"rooms": rooms}
    return render(request, "base/room.html", context)
# ,{"rooms" : rooms})