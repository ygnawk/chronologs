from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect


from register.models import Entry, Visit
# Create your views here.

@login_required
def index(request):
    return render(request, 'myaccount/index.html', { 'user' : request.user })

@login_required
def add_visit(request):
    print("adding visit")
    return render(request, 'myaccount/addvisit.html', { 'username' : request.user.username })

@login_required
def new_visit(request):
    visit = request.user.visit_set.create()
    dictionary = request.POST.dict()
    print(dictionary)
    dictionary['visit_id'] = visit.id
    create_entry(request, dictionary)
    return HttpResponseRedirect('/myaccount/')



@login_required
def edit_entry(request):
    visit_id = request.GET['visit_id']
    visit = Visit.objects.get(id=request.GET['visit_id'])

    entry = visit.entry_set.last()
    username = request.user.username
    return render(request, 'myaccount/editentry.html', {
        'entry' : entry,
        'visit_id': visit_id,
        'username': username
    })


@login_required
def make_entry(request):
    return create_entry(request, request.POST.dict())
    

def create_entry(request, dictionary):
    visit = Visit.objects.get(id=dictionary['visit_id'])
    entry = visit.entry_set.create(
        doctor_note       = dictionary['doctor_note'],
        doctor_first_name = dictionary['doctor_first_name'],
        doctor_last_name  = dictionary['doctor_last_name'],
        hospital          = dictionary['hospital'],
        date_visit        = dictionary['date_visit'],
        edit_note         = dictionary['edit_note'])
    visit.save()
    entry.save()
    return HttpResponseRedirect('/myaccount/')
    

def show_entry(request):
    visit = Visit.objects.get(id=request.GET['visit_id'])
    return render(request, 'myaccount/showentry.html', {
        'visit' : visit
    })
