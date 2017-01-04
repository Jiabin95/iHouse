from django.shortcuts import render
from .forms import AddForm,imgForm
from .models import Contact
from .models import Post
from .forms import AddPost
from django.http import HttpResponseRedirect
from myapp.models import IMG

from myapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here. 

def index(request):
    
    imgs = IMG.objects.all()
   
    
    return render(request, 'myapp/index.html', {'imgs' : imgs })
        


def uploadImg(request):
    if request.method == 'POST':
        django_form = imgForm(request.POST)
        new_des = django_form.data.get("des")
        new_tit = django_form.data.get("tit")
        img_id = IMG.objects.create(
           img = request.FILES.get('img'),
           des = new_des,
           tit = new_tit
          )
        return render(request, 'myapp/clickpic.html',{'img_id':img_id.pk})
    else:
        return render(request, 'myapp/uploadImg.html')
        
    
   
        
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'myapp/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'myapp/success.html',
    )

 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'myapp/index.html',
    { 'user': request.user }
    )




			

    
    
def add(request,pk):
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
                 
            imgs = IMG.objects.get(pk=pk)
            title = IMG.objects.get(pk=pk)
            dess = IMG.objects.get(pk=pk)
            contact_list = Contact.objects.all()
            return render(request, 'myapp/clickpic.html', {'img_id' : imgs.pk, 'contacts' : contact_list })    
        
        else:
            """ redirect to the same page if django_form goes wrong """
            imgs = IMG.objects.get(pk=pk)
            title = IMG.objects.get(pk=pk)
            dess = IMG.objects.get(pk=pk)
            contact_list = Contact.objects.all()
            return render(request, 'myapp/clickpic.html', {'img_id' : imgs.pk , 'contacts' : contact_list }) 
    else:
    	imgs = IMG.objects.get(pk=pk)
    	title = IMG.objects.get(pk=pk)
    	dess = IMG.objects.get(pk=pk)
        contact_list = Contact.objects.all()
        return render(request, 'myapp/clickpic.html', {'img_id' : imgs.pk , 'contacts' : contact_list }) 
        
        #   imgs = IMG.objects.get(pk=pk)
        #  return render(request, 'myapp/clickpic.html', {'imgs': imgs , 'contacts' : contact_list})
       
        
#def comment(request,pk):      



    
	
    	
   
  