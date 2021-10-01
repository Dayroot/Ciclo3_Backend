from django.db import models


class AbstracBasePerson(models.Model):

    fullname = models.CharField('Fullname', max_length=200)
    identification = models.CharField('Identification', max_length=15)
    address = models.CharField('Address', max_length=50)
    phone_number = models.CharField('Phone number',max_length=15)
    datebirth = models.DateField('Datebirth')
    email =models.EmailField('Email', max_length=256)

    class Meta:
        abstract = True