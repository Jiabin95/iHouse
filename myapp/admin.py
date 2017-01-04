from django.contrib import admin
from .models import IMG
# Register your models here.
from .models import Contact

admin.site.register(Contact)



# Register your models here.
class imgtest(admin.ModelAdmin):
    list_display = ['id','img','tit','des']
    class Meta : 
        model = IMG
        
admin.site.register(IMG,imgtest)