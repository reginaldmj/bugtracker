from django.shortcuts import render
from BugTrackerApp.forms import LoginForm, SignupForm, AddBugTicketForm
from BugTrackerApp.models import MyUser, MyTicket
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    form = 'index.html'
    return render(request, 'index.html')

@login_required
def bug(request, id):
    html = 'ticket_detail.html'
    ticket = MyTicket.objects.get(id=id)
    return render(request, html, {'ticket': ticket})

def home(request):
    html = 'home.html'
    user = request.user
    new = MyTicket.objects.filter(status='N').order_by('-status')
    in_progress = MyTicket.objects.filter(status='P').order_by('-status')
    done = MyTicket.objects.filter(status='D').order_by('-status')
    invalid = MyTicket.objects.filter(status='I').order_by('-status')
    
    return render(request, html, {'user': user, 'new': new, 'in_progress': in_progress, 'done': done, 'invalid': invalid})

def signup(request):
    form = SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/')
        else:
            form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('index')))
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_action(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def add_bug(request):
    form = AddBugTicketForm(request.POST) 
    if request.method == 'POST':
        form = AddBugTicketForm(request.POST) 
        if form.is_valid():
            data = form.cleaned_data
            MyTicket.objects.create(
                title=data['title'],
                description=data['description'],
                creator=request.user,
                status='N',
                user_assigned_to=request.user,
                user_who_completed=request.user,
            )
            
            return HttpResponseRedirect(reverse('home'))
    else:
        form = AddBugTicketForm()
    
    return render(request, 'generic_form.html', {'form': form})

@login_required
def edit_bug(request, id):
    ticket = MyTicket.objects.get(id=id)
    if request.method == 'POST':
        form = AddBugTicketForm(request.POST, instance=ticket)
        form.save()
        return HttpResponseRedirect(reverse('bug', args=(id,)))
    form = AddBugTicketForm(instance=ticket)
    return render(request, 'generic_form.html', {'form': form})

@login_required
def user(request, id):
    html = 'user_detail.html'
    user = MyUser.objects.get(id=id)
    creator = MyTicket.objects.filter(creator=id).order_by('-status')
    assigned_to = MyTicket.objects.filter(user_assigned_to=id).order_by('-status')
    user_completed = MyTicket.objects.filter(user_who_completed=id).order_by('-status')

    return render(request, html, {'user': user, 'creator': creator, 'assigned_to': assigned_to, 'user_completed': user_completed})

@login_required
def assignticket(request, id):
    ticket = MyTicket.objects.get(id=id)
    ticket.status = 'P'
    ticket.creator = request.user
    ticket.user_who_completed = None
    ticket.user_assigned_to = request.user
    ticket.save()
    return HttpResponseRedirect(reverse('bug', kwargs={'id': id}))

@login_required
def assigncomplete(request, id):
    ticket = MyTicket.objects.get(id=id)
    ticket.status = 'D'
    ticket.creator = request.user
    ticket.user_who_completed = ticket.user_assigned_to
    ticket.user_assigned_to = None    
    ticket.save()
    return HttpResponseRedirect(reverse('bug', kwargs={'id': id}))

@login_required
def assigninvalid(request, id):
    ticket = MyTicket.objects.get(id=id)
    ticket.status = 'I'
    ticket.creator = request.user
    ticket.user_who_completed = None
    ticket.user_assigned_to = None
    ticket.save()
    return HttpResponseRedirect(reverse('bug', kwargs={'id': id}))