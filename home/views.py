from django.shortcuts import render
from home.models import Photos, Categories
# Create your views here.



def index(request):
    cats = Categories.objects.all()
    imgs = Photos.objects.all()
    context  = {'cats':cats,'imgs':imgs}
    return render(request,'home.html',context)


def view_photo(request,pk):
    photo_obj = Photos.objects.filter(id=pk)

    context = {'photo_obj':photo_obj}
    return render(request,'view_photo.html',context)

def add_photo(request):
    return render(request,'add_photo.html')



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