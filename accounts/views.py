from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from django.http import HttpResponse
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import register
from django.contrib import messages

def registerPage(request):
    # form = CreateUserForm()

    if request.method == "POST":
        username=request.POST["username"]
        email=request.POST["email"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]
        # assert isinstance(User.objects.create_user,)
        x = register(username=username, email=email, password1=password1, password2=password$
        x.save()
        print("User Successfully Created")
        return redirect("/")
    else:
        return render(request,'accounts/register.html')

def home(request):
    return render(request,'accounts/dashboard.html')

def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            #auth.login(request,user)
            return redirect('chat/index/')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect("/")
    else:
        return render(request, 'accounts/login.html')

def customers(request):
    return render(request, 'accounts/customers.html')

def products(request):
    return render(request, 'accounts/products.html')

# from django.shortcuts import render, redirect
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages, auth
# from django.http import HttpResponse
# from .forms import CreateUserForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from .models import register
# from django.contrib import messages
#
#
# def registerPage(request):
#     # form = CreateUserForm()
#
#     if request.method == "POST":
#         username=request.POST["username"]
#         email=request.POST["email"]
#         password1=request.POST["password1"]
#         password2=request.POST["password2"]
#         # assert isinstance(User.objects.create_user,)
#         if password1==password2:
#             #check the username is existed in database using the filter object by django
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'User-Name taken')
#                 return redirect('register')
#             #checks the email is existed in database using the filter object by django
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'Email taken')
#                 return redirect('register')
#
#             #else create user in the database
#             else:
#                 x = register(username=username, email=email, password1=password1, password2=password2)
#                 x.save()
#                 # using the jwt token
#                 payload = {'id': username}
#                 key = "encode"
#                 algorithm = 'HS256'
#                 current_site = get_current_site(request)
#                 mail_subject = "Activate your account"
#                 # loading a template and rendering it with a context
#                 message = render_to_string('acc_active.html', {
#                     'user': username,
#                     'domain': current_site.domain,
#                     # Generating the token by sending payload, key, alogorithm
#                     'token': Token.encode(payload, key, algorithm),
#                 })
#                 to_email = User.objects.get(email=email)
#                 # Sending a single message to the recipient list
#                 send_mail(mail_subject, message, EMAIL_HOST_USER, [to_email.email])
#                 # print('User created')
#
#                 # redirects to the homepage
#                 messages.info(request, 'verify the mail')
#                 return redirect('/')
#                 print("User Successfully Created")
#                 return redirect("/")
#                 # form = CreateUserForm(request.POST)
#                 # if form.is_valid():
#                 #     form.save()
#                 #     user = form.cleaned_data.get('username')
#                 #     messages.success(request, 'Account Successfully created for '+ user)
#                 #     return redirect('chat/index')
#     else:
#         # form = CreateUserForm()
#         return render(request,'accounts/register.html')
#
# def home(request):
#     return render(request,'accounts/dashboard.html')
#
# def loginPage(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None:
#             # login(request, user)
#             return render(request, 'chat/index.html')
#         else:
#             messages.info(request, 'Username or Password is incorrect')
#             return redirect('/')
#     else:
#         return render(request,'accounts/login.html')
