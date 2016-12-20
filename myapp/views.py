from django.shortcuts import render
from .forms import AddForm
from .models import Contact
from .models import Post
from .forms import AddPost
from django.http import HttpResponseRedirect

from myapp.models import IMG

# Create your views here.

def index(request):
	# if request.method == 'GET':
	# 	post_list = Post.objects.all()
	# 	return render(request, "myapp/index.html",
	# 		{'posts': post_list})

	# if request.method == 'POST':
	# 	django_form = AddPost(request.POST)
	# 	if django_form.is_valid():
	# 		new_post_text = django_form.data.get("text")
	# 		Post.objects.create(text = new_post_text,)
	# 		return HttpResponseRedirect("/")    
	return render(request, "myapp/index.html")


def uploadImg(request):
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img')
        )
        new_img.save()
    return render(request, 'myapp/uploadImg.html')






			
def show(request):
        imgs = IMG.objects.all()
        contact_list = Contact.objects.all()
        return render(request, 'myapp/clickpic.html', {'imgs' : imgs, 'contacts' : contact_list})
    
    
def add(request):
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
           
            """ Assign data in Django Form to local variables """
            new_member_name = django_form.data.get("name")
            
            
            """ This is how your model connects to database and create a new member """
            Contact.objects.create(
                name =  new_member_name,
                )
                 
            imgs = IMG.objects.all()
            contact_list = Contact.objects.all()
            return render(request, 'myapp/clickpic.html', {'imgs' : imgs, 'contacts' : contact_list})    
        
        else:
            """ redirect to the same page if django_form goes wrong """
            imgs = IMG.objects.all()
            contact_list = Contact.objects.all()
            return render(request, 'myapp/clickpic.html', {'imgs' : imgs , 'contacts' : contact_list}) 
    else:
    	imgs = IMG.objects.all()
        contact_list = Contact.objects.all()
        return render(request, 'myapp/clickpic.html', {'imgs' : imgs , 'contacts' : contact_list}) 
        
          

        
        



    
	
    	
   
  