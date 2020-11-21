from django.db import models

# Create your models here.

class Userfile(models.Model):
    SEX_CHOICES = ((u'male', u'男'),
     (u'female', u'女'),)

    user_id = models.CharField(default='',max_length=30,primary_key = True)
    sex = models.CharField(default='male', max_length=6, choices=SEX_CHOICES)
    age = models.CharField(default='0',max_length=4)
    password = models.CharField(default='',max_length=50)
    identity_id = models.CharField(default='',max_length=18)
    true_name = models.CharField(default='',max_length=18)

    def __str__(self):
        return self.true_name

class Pack(models.Model):
    CATEGORY_CHOICES = (
     (u'A', u'A'),
     (u'B', u'B'),
     (u'C', u'C'),
     (u'E', u'E'),
     (u'F', u'F'),
     (u'G', u'G'),
     (u'H', u'H'),
     (u'I', u'I'),
     (u'J', u'J'),
     (u'K', u'K'),
    )

    name = models.CharField(default='',max_length=18,primary_key = True)
    area = models.CharField(default='',max_length=500)
    edition_fee = models.CharField(default='',max_length=500)
    cost = models.CharField(default='',max_length=500)
    _5000_10000 = models.CharField(default='1',max_length=10)
    _10000_20000 = models.CharField(default='1',max_length=10)
    _20000_50000 = models.CharField(default='1',max_length=10)
    _50000 = models.CharField(default='1',max_length=10)
    string = models.CharField(default='',max_length=100)
    contrast = models.TextField(default='{"L":"长（cm）","W":"宽（cm）","H":"高（cm）","S":"侧（cm）","T":"厚度（丝）","N":"数量（个）","C":"几色","G":"克重（g）","B":"底（cm）",}',max_length=400)
    remarks = models.TextField(default='备注：无',max_length=300)
    
    def __str__(self):
        return self.name