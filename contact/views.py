# from django.shortcuts import render, redirect
# from contact.models import Contacts

# # Create your views here.


# def contact(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message = request.POST['message']

#         contact = Contacts(name=name, email=email,  subject=subject, message=message)
#         contact.save()
#         return redirect('contact')

#     return render(request, 'pages/index.html')