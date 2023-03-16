from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from .forms import ImageForm
from .models import UploadImage
from authentication.models import User
from django.db.models import Q

# Create your views here.
@login_required(login_url="/login")
def dashboard(request):
    current_user = request.user.username
    if request.user.is_superuser:
        get_images = UploadImage.objects.all()
    elif request.user.is_staff:
        users_ids = User.objects.filter(role="student")
        get_images = UploadImage.objects.filter(Q(user=request.user.id) | Q(user__in=users_ids))
    else:
        get_images = UploadImage.objects.filter(user=request.user.id)
    return render(request, 'dashboard.html', {"user":current_user, "get_images":get_images})

@login_required(login_url="/login")
def upload_images(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        user_id = User.objects.get(email=request.user)
        print(request.FILES, "kkkkk")
        print(user_id.id, "=--=-")
        print(request.FILES.getlist('image'), "request.FILES.getlist('image')")
        if form.is_valid():
            print("valid")
            for image in request.FILES.getlist('image'):
                print(image, "oooo")
                UploadImage.objects.create(image=image, user=user_id)
            print("succ")
            return redirect("/")
    else:
        print("error")
        form = ImageForm()
        print(form, "error formmm resulr")
    print("else")
    return render(request, 'image_upload.html', {'form': form})

@login_required(login_url="/login")
def logout_user(request):
    logout(request)
    messages.success(request, 'User logout Successfully')
    return redirect('/login')