from django.shortcuts import render
#for http response 
# from django.http import HttpResponse, JsonResponse


# Create your views here.

#Home page
def home(request):
    # data = {
    #     "name":"Ankush",
    #     "phone": 9896492818,
    # }
    # return  HttpResponse("<h1>This is a ToDo Task<h2>")
    # return JsonResponse(data=data)
    return render(request, "index.html", {"page":"Home Page"})

#Contact us page
def contact(request):
    return render(request, "contact.html")

#About us page 
def about(request):
    return render(request, "about.html")

#Todolist page manager
def todolist(request):
    return render(request, "todolist.html")


