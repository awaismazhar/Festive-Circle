from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


import random
from django.core.files.storage import FileSystemStorage
from ads.views import main
User = get_user_model()


def generate_code(email):

  code = ""
  for x in range(4):
    code = code + str(random.randint(0, 9))

  user = User.objects.get(email=email)
  reset_code = reset_codes.objects.filter(user=user)

  if not reset_code:
    reset_code = reset_codes.objects.create(user=user, code=code)
    reset_code.save()
  else:
    reset_code = reset_codes.objects.filter(user=user).update(code=code)

  subject = 'Password reset code'
  message = 'Your reset code is '+code+'\n\nThank you.'
  email_from = settings.EMAIL_HOST_USER
  recipient_list = [email, ]
  send_mail(subject, message, email_from, recipient_list)


def password_reset_request(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            request.session['email'] = email

            generate_code(email)

            return redirect('emailcode')
        else:
            context = {
                'message': 'This email is not registered'
            }
            return render(request, 'users/enteremail.html', context)
    else:
        return render(request, 'users/enteremail.html')


def match_code_request(request):
  if request.method == 'POST':
    print("This is post")
    code1 = request.POST.get('code')
    email = request.session.get('email')
    user = User.objects.get(email=email)
    code2 = reset_codes.objects.get(user=user)
    code2 = code2.code
    print(code1)
    print(code2)

    if code1 == code2:
        return redirect('newpassword')
    else:
        context = {
             'message': 'You enterd wrong reset code'
          }
        return render(request, 'users/emailcode.html', context)
  else:
    return render(request, 'users/emailcode.html')


def new_password_request(request):
  if request.method == 'POST':
    password = request.POST.get('password')
    user = User.objects.get(email=request.session.get('email'))
    user.set_password(password)
    user.save()
    return redirect('home')
  else:
    return render(request, 'users/enternewpassword.html')


def login(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      remember_me = request.POST.get('remember me')

      # if email == "":
      #   context = {'message': "You haven't entered an email"}
      #   return render(request, 'users/login.html', context)
      # elif password == "":
      #   context = {'message': "You haven't entered a password"}
      #   return render(request, 'users/login.html', context)

      if(remember_me == "on"):
        request.session.set_expiry(60 * 10)

      if User.objects.filter(email=email).exists():
        user = auth.authenticate(email=email, password=password)
        if user is not None:
          auth.login(request, user)
          request.session['user_id'] = user.id
          return redirect('home')
        else:
          messages.error(request, 
          "Your password is incorrect. Try again or click forgot password.", 
          extra_tags="password")
          return HttpResponseRedirect(request.path)
      else:
        messages.error(request, "This email has not been registered. Click signup to register this account.", extra_tags="email")
        return HttpResponseRedirect(request.path)
    else:
      return render(request, 'users/login.html')


def register_request(request):
  if request.user.is_authenticated:
    return redirect('home')
  else:
    if request.method == 'POST':
      email = request.POST.get('email')
      password = request.POST.get('password')
      name = request.POST.get('name')
      dob = request.POST.get('dob')
      address = request.POST.get('address')
      about_me = request.POST.get('about_me')
      
      if about_me == "":
        about_me = None
      if address == "":
        address = None

      if request.FILES:
        pfp = request.FILES['pfp']
      else:
        pfp = None
      print(pfp)
      if (email == "" or name == "" or 
            dob == "" or password == ""):
        context = {'message': 'Form is not filled properly'}
        return render(request, 'users/register.html', context)

      if address == "":
          address = None
      if about_me == "":
          about_me = None
      if User.objects.filter(email=email).exists():
        context = {'message': 'This email is already registered'}
        return render(request, 'users/register.html', context)
      else:         
        user = User.objects.create_user(email=email, password=password,
                  name=name, dob=dob, pfp=pfp, address=address, 
                    about_me=about_me)
        user.save()
        user = auth.authenticate(email=email, password=password)
        if user is not None:
          auth.login(request, user)
          request.session['user_id'] = user.id
          return redirect('home')
        else:
            return redirect('home')
    else:
      return render(request, 'users/register.html')


@login_required
def logout_request(request):
    auth.logout(request)
    return redirect('home')

@login_required
def change_password_request(request):
    if request.method == 'POST':
      old_password  = request.POST.get('old_password')
      new_password = request.POST.get('new_password')
      confirm_password = request.POST.get('confirm_password')
      if new_password == confirm_password:
        user = User.objects.get(id=request.session['user_id'])
        exists = auth.authenticate(email=user.email, password=old_password)
        if exists is not None:
          user.set_password(new_password)
          user.save()
          update_session_auth_hash(request, user)
          return redirect('home')
        else:
          context = {
             'message': "You've entered a wrong password"
          }
          return render(request, 'users/changepassword.html', context)
      else:
        context = {
            'message': "New password fields won't match"
        }
        return render(request, 'users/changepassword.html', context)      
    else:
      return render(request, 'users/changepassword.html')


def home(request):
  for key, value in request.session.items():
    print('{} => {}'.format(key, value))
  return redirect(main)

@login_required
def display_profile_request(request):
  return render(request, 'users/displayprofile.html')

@login_required
def update_profile_request(request):
  if request.method == 'POST':
    email = request.POST.get('email')
    name = request.POST.get('name')
    address = request.POST.get('address')
    dob = request.POST.get('dob')
    about_me = request.POST.get('about_me')

    if about_me == "":
      about_me = None
    if address == "":
      address = None

    # if request.FILES['pfp'] is None:
    user = User.objects.get(id=request.session['user_id'])
    if request.FILES:
      pfp = request.FILES['pfp']
    else:
      pfp = user.pfp

    print(pfp)

    user.email = email
    user.name = name
    user.address = address
    user.dob = dob
    user.about_me = about_me
    user.pfp = pfp
    user.save()
    update_session_auth_hash(request, user)

    return redirect('displayprofile')      
  else:
    return render(request, 'users/updateprofile.html')
