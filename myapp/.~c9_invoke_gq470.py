from django.shortcuts import render
from .forms import AddForm,imgForm
from .models import Contact
from .models import Post
# from .forms import AddPost
from django.http import HttpResponseRedirect
from myapp.models import IMG
from django.shortcuts import redirect ,get_object_or_404
from myapp.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from time import localtime,strftime
from django.utils import timezone

# Create your views here. 

def index(request):
    
    imgs = IMG.objects.all()
    return render(request, 'myapp/index.html', {'imgs' : imgs })
        


def uploadImg(request):
    if request.method == 'POST':
        django_form = imgForm(request.POST)
        new_room = django_form.data.get('room') 
        new_des = django_form.data.get("des")
        new_tit = django_form.data.get("tit")
        IMG.objects.create(
            img = request.FILES.get('img'),
            des = new_des,
            tit = new_tit,
            room = new_room
        )
        
        img = IMG.objects.all()
        return redirect('https://ihouse-jiabin95.c9users.io/')

    else:
        return render(request, 'myapp/uploadImg.html')

def space(request,pk):
    temp_pk = pk
    imgs = IMG.objects.filter(room=temp_pk)
    
    return render(request, 'myapp/space.html', {'imgs' : imgs })
        
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
    check_pk = pk
    """ This function is called to add one contact member to your contact list in your Database """
    if request.method == 'POST':
        
        django_form = AddForm(request.POST)
        if django_form.is_valid():
            imgs = IMG.objects.get(pk=pk)
            title = IMG.objects.get(pk=pk)
            dess = IMG.objects.get(pk=pk)
            
            return render(request, 'myapp/clickpic.html', {'img' : imgs})    
        
        else:
            """ redirect to the same page if django_form goes wrong """
            imgs = IMG.objects.get(pk=p)
            title = IMG.objects.get(pk=pk)
            dess = IMG.objects.get(pk=pk)
            contact_list = Contact.objects.filter(post_id=pk).all()
            imgs = IMG.objects.get(pk=check_pk)
            return render(request, 'myapp/clickpic.html', {'comment' : contact_list, 'img' : imgs }) 
    else:
        imgs = IMG.objects.get(pk=pk)
    	title = IMG.objects.get(pk=pk)
    	dess = IMG.objects.get(pk=pk)
        contact_list = Contact.objects.filter(post_id=pk).all()
        imgs = IMG.objects.get(pk=check_pk)
        return render(request, 'myapp/clickpic.html', {'comment' : contact_list, 'img' : imgs }) 
       
       
        

            
def comment(request,pk): 
    check_pk = pk
    
    if request.method =='POST':
        django_form = AddForm(request.POST)
        if django_form.is_valid():
            new_context = django_form.data.get("context")
            Contact.objects.create(
                  comment =  new_context,
                  name = User.objects.get(username=request.user.username),,
                  time = "",
                  post_id = check_pk,
            )
            return redirect("comment",check_pk)
    else:
        
        imgs = IMG.objects.get(pk=check_pk)
        contact_list = Contact.objects.filter(post_id=check_pk).all()
        
        if request.is_ajax():
            return render(request, 'myapp/refresh.html', {'comment' : contact_list, 'img_ifo' : imgs })
        else:
            return render(request, 'myapp/clickpic.html', {'comment' : contact_list, 'img_ifo' : imgs })            


    
	
    	
   
  