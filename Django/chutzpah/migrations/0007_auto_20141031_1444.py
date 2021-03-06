# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chutzpah', '0006_auto_20141031_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmes',
            name='name',
            field=models.CharField(max_length=6, choices=[('', 'A4109'), ('', 'A4111'), ('', 'A4125'), ('', 'B4101'), ('', 'B4107'), ('', 'B4109'), ('', 'B4110'), ('', 'B4111'), ('', 'B4117'), ('', 'B4125'), ('', 'B4128'), ('', 'B5210'), ('', 'B5219'), ('', 'B5221'), ('', 'B5226'), ('', 'B5229'), ('', 'B5234'), ('', 'B5235'), ('', 'B5244'), ('', 'B5245'), ('', 'B5503'), ('', 'C4110'), ('', 'C4111'), ('', 'C4125'), ('', 'D4107'), ('', 'D4109'), ('', 'D4110'), ('', 'D4111'), ('', 'D4112'), ('', 'D4117'), ('', 'D4125'), ('', 'D4136'), ('', 'D4139'), ('', 'D5205'), ('', 'D5210'), ('', 'D5216'), ('', 'D5220'), ('', 'D5305'), ('', 'E4110'), ('', 'E4111'), ('', 'E4125'), ('', 'G4101'), ('', 'G4102'), ('', 'G4105'), ('', 'G4107'), ('', 'G4109'), ('', 'G4110'), ('', 'G4111'), ('', 'G4115'), ('', 'G4120'), ('', 'G4121'), ('', 'G4122'), ('', 'G4125'), ('', 'G4127'), ('', 'G4130'), ('', 'G4133'), ('', 'G5101'), ('', 'G5201'), ('', 'G5203'), ('', 'G5208'), ('', 'G5210'), ('', 'G5215'), ('', 'G5216'), ('', 'G5222'), ('', 'G5225'), ('', 'G5230'), ('', 'G5231'), ('', 'G5239'), ('', 'G5243'), ('', 'G5247'), ('', 'G5248'), ('', 'G5251'), ('', 'G5253'), ('', 'G5501'), ('', 'G5503'), ('', 'G5504'), ('', 'G5505'), ('', 'G5506'), ('', 'G5507'), ('', 'H4107'), ('', 'H4109'), ('', 'H4110'), ('', 'H4111'), ('', 'H4118'), ('', 'H4125'), ('', 'J4110'), ('', 'J4111'), ('', 'J4125'), ('', 'J4138'), ('', 'K4101'), ('', 'K4103'), ('', 'K4107'), ('', 'K4109'), ('', 'K4110'), ('', 'K4111'), ('', 'K4123'), ('', 'K4125'), ('', 'K4201'), ('', 'K4202'), ('', 'K4203'), ('', 'K4204'), ('', 'M4101'), ('', 'M4107'), ('', 'M4109'), ('', 'M4110'), ('', 'M4111'), ('', 'M4117'), ('', 'M4125'), ('', 'M4127'), ('', 'M4132'), ('', 'M5201'), ('', 'M5202'), ('', 'M5207'), ('', 'M5210'), ('', 'M5212'), ('', 'M5213'), ('', 'M5215'), ('', 'M5216'), ('', 'M5217'), ('', 'M5218'), ('', 'M5227'), ('', 'M5228'), ('', 'M5236'), ('', 'M5237'), ('', 'M5238'), ('', 'M5241'), ('', 'M5249'), ('', 'M5250'), ('', 'M5601'), ('', 'M5602'), ('', 'N4107'), ('', 'N4111'), ('', 'N4125'), ('', 'P4110'), ('', 'P4111'), ('', 'P4125'), ('', 'R4104'), ('', 'R4107'), ('', 'R4109'), ('', 'R4110'), ('', 'R4111'), ('', 'R4114'), ('', 'R4125'), ('', 'R4127'), ('', 'R4135'), ('', 'R4136'), ('', 'R4137'), ('', 'R5101'), ('', 'R5211'), ('', 'R5214'), ('', 'R5223'), ('', 'R5224'), ('', 'R5242'), ('', 'R5302'), ('', 'R5303'), ('', 'R5403'), ('', 'R5502'), ('', 'R5503'), ('', 'R5507'), ('', 'S4107'), ('', 'S4110'), ('', 'S4111'), ('', 'S4114'), ('', 'S4119'), ('', 'S4125'), ('', 'S4129'), ('', 'S4130'), ('', 'S4131'), ('', 'S4134'), ('', 'S5246'), ('', 'S5247'), ('', 'S5252'), ('', 'S5305'), ('', 'S5401'), ('', 'S5402'), ('', 'S5701'), ('', 'S5702'), ('', 'U4110'), ('', 'U4111'), ('', 'U4125'), ('', 'V4106'), ('', 'V4107'), ('', 'V4109'), ('', 'V4110'), ('', 'V4111'), ('', 'V4113'), ('', 'V4125'), ('', 'V4126'), ('', 'V4130'), ('', 'V4301'), ('', 'V5204'), ('', 'V5206'), ('', 'V5209'), ('', 'V5214'), ('', 'V5216'), ('', 'V5223'), ('', 'V5232'), ('', 'V5233'), ('', 'V5240'), ('', 'V5247'), ('', 'V5301'), ('', 'V5304'), ('', 'V5305'), ('', 'V5801'), ('', 'W4104'), ('', 'W4107'), ('', 'W4108'), ('', 'W4109'), ('', 'W4110'), ('', 'W4114'), ('', 'W4116'), ('', 'W4117'), ('', 'W4124'), ('', 'W4125'), ('', 'W4401')]),
            preserve_default=True,
        ),
    ]
