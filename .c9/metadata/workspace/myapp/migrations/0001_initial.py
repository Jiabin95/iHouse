{"changed":true,"filter":false,"title":"0001_initial.py","tooltip":"/myapp/migrations/0001_initial.py","value":"# -*- coding: utf-8 -*-\n# Generated by Django 1.9 on 2016-12-18 06:35\nfrom __future__ import unicode_literals\n\nfrom django.db import migrations, models\n\n\nclass Migration(migrations.Migration):\n\n    initial = True\n\n    dependencies = [\n    ]\n\n    operations = [\n        migrations.CreateModel(\n            name='POST',\n            fields=[\n                ('id', models.AutoField(auto_created=Tru, primary_key=True, serialize=False, verbose_name='ID')),\n                ('text', models.CharField(max_length=30)),\n            ],\n        ),\n    ]\n","undoManager":{"mark":54,"position":62,"stack":[[{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"remove","lines":["t"],"id":2}],[{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"remove","lines":["s"],"id":3}],[{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"remove","lines":["o"],"id":4}],[{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"remove","lines":["P"],"id":5}],[{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"insert","lines":["D"],"id":8}],[{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"insert","lines":["E"],"id":9}],[{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"remove","lines":["E"],"id":10}],[{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"insert","lines":["E"],"id":11}],[{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"insert","lines":["L"],"id":12}],[{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"insert","lines":["E"],"id":13}],[{"start":{"row":16,"column":22},"end":{"row":16,"column":23},"action":"insert","lines":["T"],"id":14}],[{"start":{"row":16,"column":23},"end":{"row":16,"column":24},"action":"insert","lines":["E"],"id":15}],[{"start":{"row":16,"column":23},"end":{"row":16,"column":24},"action":"remove","lines":["E"],"id":16}],[{"start":{"row":16,"column":22},"end":{"row":16,"column":23},"action":"remove","lines":["T"],"id":17}],[{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"remove","lines":["E"],"id":18}],[{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"remove","lines":["L"],"id":19}],[{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"remove","lines":["E"],"id":20}],[{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"remove","lines":["D"],"id":21}],[{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"insert","lines":["p"],"id":22}],[{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"insert","lines":["o"],"id":23}],[{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"remove","lines":["o"],"id":24}],[{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"remove","lines":["p"],"id":25}],[{"start":{"row":16,"column":18},"end":{"row":16,"column":19},"action":"insert","lines":["P"],"id":26}],[{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"insert","lines":["O"],"id":27}],[{"start":{"row":16,"column":20},"end":{"row":16,"column":21},"action":"insert","lines":["S"],"id":28}],[{"start":{"row":16,"column":21},"end":{"row":16,"column":22},"action":"insert","lines":["T"],"id":29}],[{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"remove","lines":["e"],"id":30}],[{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"remove","lines":["u"],"id":31}],[{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"remove","lines":["r"],"id":32}],[{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"remove","lines":["T"],"id":33}],[{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"insert","lines":["F"],"id":34}],[{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"insert","lines":["A"],"id":35}],[{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"insert","lines":["L"],"id":36}],[{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"insert","lines":["S"],"id":37}],[{"start":{"row":18,"column":57},"end":{"row":18,"column":58},"action":"insert","lines":["E"],"id":38}],[{"start":{"row":18,"column":57},"end":{"row":18,"column":58},"action":"remove","lines":["E"],"id":39}],[{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"remove","lines":["S"],"id":40}],[{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"remove","lines":["L"],"id":41}],[{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"remove","lines":["A"],"id":42}],[{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"remove","lines":["F"],"id":43}],[{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"insert","lines":["f"],"id":44}],[{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"insert","lines":["a"],"id":45}],[{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"insert","lines":["l"],"id":46}],[{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"insert","lines":["s"],"id":47}],[{"start":{"row":18,"column":57},"end":{"row":18,"column":58},"action":"insert","lines":["e"],"id":48}],[{"start":{"row":18,"column":57},"end":{"row":18,"column":58},"action":"remove","lines":["e"],"id":49}],[{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"remove","lines":["s"],"id":50}],[{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"remove","lines":["l"],"id":51}],[{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"remove","lines":["a"],"id":52}],[{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"remove","lines":["f"],"id":53}],[{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"insert","lines":["F"],"id":54}],[{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"insert","lines":["a"],"id":55}],[{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"insert","lines":["l"],"id":56}],[{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"insert","lines":["s"],"id":57}],[{"start":{"row":18,"column":57},"end":{"row":18,"column":58},"action":"insert","lines":["e"],"id":58}],[{"start":{"row":18,"column":57},"end":{"row":18,"column":58},"action":"remove","lines":["e"],"id":59}],[{"start":{"row":18,"column":56},"end":{"row":18,"column":57},"action":"remove","lines":["s"],"id":60}],[{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"remove","lines":["l"],"id":61}],[{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"remove","lines":["a"],"id":62}],[{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"remove","lines":["F"],"id":63}],[{"start":{"row":18,"column":53},"end":{"row":18,"column":54},"action":"insert","lines":["T"],"id":64}],[{"start":{"row":18,"column":54},"end":{"row":18,"column":55},"action":"insert","lines":["r"],"id":65}],[{"start":{"row":18,"column":55},"end":{"row":18,"column":56},"action":"insert","lines":["u"],"id":66}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":18,"column":56},"end":{"row":18,"column":56},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1482077536609}