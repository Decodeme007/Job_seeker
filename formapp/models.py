from django.db import models

# Create your models here.
class Applicant(models.Model):
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField(max_length = 254)
    applicant_phoneNo = models.IntegerField()
    applicant_address = models.CharField(max_length=600)
    applicant_shortIntro = models.TextField(null=True, blank=True)
    applicant_image = models.ImageField(upload_to="applicant",null=True, blank=True)
    applicant_resume = models.FileField(upload_to="applicant",null=True, blank=True)
