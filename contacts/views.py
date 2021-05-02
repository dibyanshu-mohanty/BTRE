from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
# Create your views here.
def contact(request):
    if request.method=="POST":
        listing_id=request.POST['listing_id']
        listing=request.POST['listing']
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        realtor_email=request.POST['realtor_email']
        user_id=request.POST['user_id']
        # Check if inquiry has already been Made
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted= Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an inquiry for this listing.")
                return redirect('/listings/'+listing_id)
        contact = Contact(listing=listing,listing_id=listing_id, name=name, email=email, phone=phone, message=message, 
        user_id=user_id)
        contact.save()
        # send MAIL
        send_mail(
            'Property Lising Inquiry',
            'There Has been an Inquiry for'+listing+' Sign In into the Admin panel for more Info.',
            'dibyanshu.m2002@gmail.com',
            [realtor_email,'dibyanshu2002@gmail.com'],
            fail_silently= False
        )
        messages.success(request,"Your Enquiry has been recieved. Our realtor will get back to you soon.")
        return redirect('/listings/'+listing_id)
