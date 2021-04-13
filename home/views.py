from django.shortcuts import render, redirect
from home.models import Photos, Categories
from django.forms import forms
from .forms import CategoryForm
# Create your views here.



def index(request):
    cats = Categories.objects.all()
    category = request.GET.get('cat')
    if category ==None:
        imgs = Photos.objects.all()
    else:
        imgs = Photos.objects.filter(category__name=category)
    context  = {'cats':cats,'imgs':imgs}
    return render(request,'home.html',context)


def view_photo(request,pk):
    photo_obj = Photos.objects.filter(id=pk)

    context = {'photo_obj':photo_obj}
    return render(request,'view_photo.html',context)

def add_photo(request):
    categories = Categories.objects.all()
    context = { 'categories':categories }
    if request.method =='POST':
        data = request.POST
        desc = request.POST.get('desc')
        image = request.FILES.get('image')
        category = Categories.objects.get(id=data['category'])
        photo = Photos(image=image,category=category,desc=desc)
        photo.save()
        return redirect('/')
    return render(request,'add_photo.html', context)



#  As the Model attribute, catergory is a forign key, I used a longer method or workaround
# def category(request,cat):
#     cat_pics = Photos.objects.all()
#     cat_photos=[]             
#     for i in cat_pics:
#         if i.category.name == cat:
#             cat_photos.append(i)

#     context = {'cat_photos':cat_photos, 'cat':cat}
#     return render(request,'category.html',context)

def category(request,id): #  As the Model attribute, catergory is a forign key, ID is user to filter the OBJECT
    cat_photos= Photos.objects.filter(category=id) #The ID is being sent from view_photo.html as slug or extra url field
    context = {'cat_photos':cat_photos}
    return render(request,'category.html',context)

def add_category(request):
    form = CategoryForm()
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add-photo')
    return render(request, 'add_category.html', {'form':form})