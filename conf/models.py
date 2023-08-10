from django.db import models

# Create your models here.


class Usermodel(models.Model):
    Name = models.CharField(max_length=70, null= True ,blank=True)
    Fathers_Name = models.CharField(max_length=70, null= True ,blank=True)
    Email_Id = models.EmailField(max_length=100, null= True ,blank=True)
    Contact_No = models.IntegerField( null= True ,blank=True)
    Address = models.CharField(max_length=300, null= True ,blank=True)

    class Meta:
        permissions = [
            ("can_view_email_id", "Can View Email-ID"),
        ]
