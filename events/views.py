from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserSignup, UserLogin, EventForm

from .models import Event
from django.db.models import Q

def home(request):
    events = Event.objects.all()
    query = request.GET.get("q")
    if query:
        events = events.filter(
            Q(title__icontains=query)|
            Q(description__icontains=query)|
            Q(organizer__username__icontains=query)
            ).distinct()

    context = {
        "events": events
    }
    return render(request, 'home.html', context)


class Signup(View):
    form_class = UserSignup
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            # messages.success(request, "You have successfully signed up.")
            login(request, user)
            return redirect("home")
        # messages.warning(request, form.errors)
        return redirect("signup")


class Login(View):
    form_class = UserLogin
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # messages.success(request, "Welcome Back!")
                return redirect('dashboard')
                # the new line we added
                # return redirect('home')
            # messages.warning(request, "Wrong email/password combination. Please try again.")
            return redirect("login")
        # messages.warning(request, form.errors)
        return redirect("login")


class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        # messages.success(request, "You have successfully logged out.")
        return redirect("login")



# def events_list(request):
#     events = Event.objects.all()
#     query = request.GET.get("q")
#     if query:
#         events = events.filter(
#             Q(title__icontains=query)|
#             Q(description__icontains=query)|
#             Q(organizer__icontains=query)
#             ).distinct()

#     context = {
#         "events": events
#     }
#     return render(request, 'home.html', context)


def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    context = {
        "event": event,
    }
    return render(request, 'detail.html', context)

def event_create(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('create')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def event_update(request, event_id):
    event_obj = Event.objects.get(id=event_id)
    form = EventForm(instance=event_obj)
    if request.method == "POST":
        form = EventForm(request.POST, instance=event_obj)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        "event_obj": event_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def event_delete(request, event_id):
    event_obj = Event.objects.get(id=event_id)
    event_obj.delete()
    return redirect('dashboard')


def dashboard(request):
    events = Event.objects.all()
    context = {
        "events": events
    }
    return render(request, 'dashboard.html', context)
