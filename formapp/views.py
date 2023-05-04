from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def form(request):
    if request.method == "POST":
        data = request.POST
        applicant_name = data.get('applicant_name')
        applicant_email = data.get('applicant_email')
        applicant_phoneNo = data.get('applicant_phoneNo')
        applicant_address = data.get('applicant_address')
        applicant_shortIntro = data.get('applicant_shortIntro')
        applicant_image = request.FILES.get('applicant_image')
        applicant_resume = request.FILES.get('applicant_resume')

        Applicant.objects.create(
            applicant_name = applicant_name,
            applicant_email= applicant_email,
            applicant_phoneNo = applicant_phoneNo,
            applicant_address = applicant_address,
            applicant_shortIntro = applicant_shortIntro,
            applicant_image = applicant_image,
            applicant_resume = applicant_resume,
        )
        return redirect('/')

    return render(request,'formapp/form.html')
