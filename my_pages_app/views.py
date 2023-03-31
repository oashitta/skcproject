from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ContactForm
from django.core.mail import send_mail

def home(request):
    return render(request, 'home.html', {})

def who_we_are(request):
    return render(request, 'who_we_are.html', {})

def programs(request):
    return render(request, 'programs.html', {})

def community_support(request):
    return render(request, 'programs_community.html', {})

def mentoring_counselling(request):
    return render(request, 'programs_counselling.html', {})

def placement_reintegration(request):
    return render(request, 'programs_reintegration.html', {})

def mobile_learning(request):
    return render(request, 'programs_learning.html', {})

def make_an_impact(request):
    return render(request, 'make_an_impact.html', {})

def gallery(request):
    return render(request, 'gallery.html', {})

def upcomingevents(request):
    return render(request, 'upcomingevents.html', {})

def get_in_touch(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email
            message = 'Name: ' + form.cleaned_data['name'] + '\nEmail: ' + form.cleaned_data['email'] + '\nMessage: ' + form.cleaned_data['message']
            send_mail(
                'Form Submission',
                message,
                'mottestingapplications@gmail.com',  # Replace with your email address
                ['omotundeakinsola@gmail.com'],  # Replace with the recipient's email address
                fail_silently=False,
            ) 
            context = {'section':'contact'}
            return render(request, 'success.html', context)

    form = ContactForm()
    context = {'form':form}
    return render(request, 'get_in_touch.html', context)

def donate(request):
    return render(request, 'donate.html', {})

def success(request):
    return HttpResponse("Thank you for contacting us. Your message has been sent successfully!")

# def partner_view(request):
#     if request.method == "POST":
#         form = PartnershipForm(request.POST)
#         if form.is_valid():
#             form.save()
#             context = {'section':'partner'}
#             return render(request, 'success.html', context)

#     form = PartnershipForm()
#     context = {'form':form}
#     return render(request, 'partnership_form.html', context)
