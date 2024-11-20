from django.shortcuts import render,redirect,get_object_or_404
from .forms import * 
from .models import *


# Create your views here.


def index (request):
   books=Book.objects.all()
   sold=Book.objects.filter(status='sold').count()
   rental=Book.objects.filter(status='rental').count()
   available=Book.objects.filter(status='available').count()
   categorys=Category.objects.all()

   form=BookForm()
   form_cat=CategoryForm()

   if 'add_book' in request.POST :

      form=BookForm(request.POST , request.FILES)
      if form.is_valid():
         form.save()
   elif 'add_cat'in request.POST :
      form_cat=CategoryForm(request.POST)
      if form_cat.is_valid():
         form_cat.save()




   context={
      'categorys':categorys,
      'books':books,
      'form':form,
      'form_cat':form_cat,
      'total_books':Book.objects.all().count(),
       'sold':sold,
       'rental':rental,
       'available':available,
       'sum':sum,

   }
   return render (request,'pages/index.html',context)


def books (request):
   categorys=Category.objects.all()
   searsh=Book.objects.all()
   form_cat=CategoryForm()

   title =None

   if 'search_name' in request.GET :
      title = request.GET['search_name']
      if title :
         searsh =searsh.filter(title__icontains=title)
   context={
      'categorys':categorys,
      'books':searsh,
      'form_cat':form_cat,
   }
   return render (request,'pages/books.html',context)

def delete (request,i_d):

   book=get_object_or_404(Book,id=i_d)#this is another way tow get the book

   if request.method=="POST":
      book.delete()
      return redirect('/')
   

   

   return render(request,'pages/delete.html')


def update (request,i_d):
   book=Book.objects.get(id=i_d)
   form=BookForm(instance=book)
   if request.method == "POST":

      form=BookForm(request.POST , request.FILES ,instance=book)
      if form.is_valid():
         form.save()
         return redirect('/')

   content={
      'form':form
   }

   return render(request,'pages/update.html',content)
