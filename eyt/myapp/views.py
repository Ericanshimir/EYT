from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .forms import Video_form
from .forms import Video
from .forms import MentorshipApplication
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return  render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already exist')
                return redirect('register')
            else:
                user =User.objects.create_user(username=username, email=email, password=password),
                messages.success(request, 'User created successfully')
                return redirect('login')
                
            
        else:
            messages.info(request, 'password is not the same')
            return redirect('register')
    else:
        return render (request, 'register.html')
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
       return render (request, 'login.html')
    

def logout(request):
    auth.logout(request)
    return redirect('/')


  

def counter(request):
    posts =[1, 2, 3, 4, 'erica', 'ange', 'franck']
    return render(request, 'counter.html', {'posts': posts})

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})


def dashboard(request):
    return render(request, 'dashboard.html' )

def training_materials(request):
    return render(request, 'training_materials.html' )

def contact(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def room(request):
    return room(request, 'room.html')

def all(request):
    if request.method == "POST":
        all_video=Video.objects.all()
        form=Video_form(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>uploaded successfully")
    else:
        form=Video_form()
    return render(request,'all.html',{"form":form,"all":all_video})

def mentorship_application(request):
    if request.method == 'POST':
        form = MentorshipApplication(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')
            # Optionally, do something after saving the form
    else:
        form = MentorshipApplication()

    # Fetch 'all' data from your model, replace YourModel with your actual model
    all_data = MentorshipApplication.objects.all()

    return render(request, 'training_materials.html', {'form': form, 'all': all_data})




def upload_video(request):
    if request.method == 'POST' and request.FILES['video_file']:
        video_file = request.FILES['video_file']
        # Handle the uploaded file, for example, save it to your database or file system
        # Example: video = VideoModel(video_file=video_file)
        # video.save()
        return JsonResponse({'message': 'Video uploaded successfully'})
    else:
        return JsonResponse({'error': 'Upload failed'})

def index(request):
    return render(request, 'index.html')
def send_info(request):
    if request.method == 'POST':
        info = request.POST.get('info')
        # Here, you can process the received information as needed
        # For demonstration purposes, we'll simply send it back as a response
        return JsonResponse({'info': info})
    return JsonResponse({'error': 'Invalid request'})

    

