from django.contrib import admin
from .models import IMG
# Register your models here.
from .models import Contact




# Register your models here.
class imgtest(admin.ModelAdmin):
    list_display = ['id','img','tit','des','room']
    class Meta : 
        model = IMG
        
admin.site.register(IMG,imgtest)

class contacts(admin.ModelAdmin):
    list_display = ['name','comment','time','post_id' ]
    class Meta:
        model = Contact
        
admin.site.register(Contact,contacts)