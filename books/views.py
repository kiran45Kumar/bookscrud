from django.shortcuts import render

# Create your views here.
def create(request):
    return render(request, 'books/create.html')
def read(request):
    return render(request, 'books/read.html')
def update(request):
    return render(request, 'books/update.html') 
def delete(request):
    return render(request, 'books/delete.html')