from django.shortcuts import render
from django.contrib import messages
from .models import Contact
from .forms import Contact_form


def contact_view(request):
    if request.method == "POST":
        contactform = Contact_form(data=request.POST)
        if contactform.is_valid():
            contactform.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Thank you for getting in touch,\
                we will respond as soon as possible!"
            )

    contact = Contact.objects.all().order_by('-updated_on').first()
    contactform = Contact_form()

    return render(
        request,
        "contact/contact.html",
        {
            "contact": contact,
            "contactform": contactform
        },
    )
