{"filter":false,"title":"admin.py","tooltip":"/myapp/admin.py","undoManager":{"mark":5,"position":5,"stack":[[{"start":{"row":5,"column":28},"end":{"row":6,"column":0},"action":"insert","lines":["",""],"id":2}],[{"start":{"row":6,"column":0},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":3}],[{"start":{"row":7,"column":0},"end":{"row":15,"column":32},"action":"insert","lines":["from django.contrib import admin","from .models import IMG","# Register your models here.","class imgtest(admin.ModelAdmin):","    list_display = ['img']","    class Meta : ","        model = IMG","        ","admin.site.register(IMG,imgtest)"],"id":4}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":32},"action":"remove","lines":["from django.contrib import admin"],"id":5}],[{"start":{"row":8,"column":0},"end":{"row":8,"column":23},"action":"remove","lines":["from .models import IMG"],"id":6}],[{"start":{"row":1,"column":0},"end":{"row":1,"column":23},"action":"insert","lines":["from .models import IMG"],"id":7}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":1,"column":23},"end":{"row":1,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1482163725139,"hash":"14cc645d856c00d33ed8190aa44a48d596687d06"}