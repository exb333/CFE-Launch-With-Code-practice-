from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import EmailForm, JoinForm
from .models import Join
import uuid


def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ""
    return ip


def get_ref_id():
    ref_id = str(uuid.uuid4())[:11].replace('-', '').lower()
    try:
        id_exists = Join.objects.get(ref_id=ref_id)
        get_ref_id()
    except:
        return ref_id


def home(request):
    # Regular Forms

    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    # 	email = form.cleaned_data['email']
    # 	new_join, created = Join.objects.get_or_create(email=email)

    # Model Forms
    try:
        poll_id = request.session['ref']
        obj = Join.objects.get(id=poll_id)
    except:
        obj = None

    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        if created:
            new_join_old.ref_id = get_ref_id()
            # adding referred friends
            if not obj == None:
                new_join_old.friend = obj
            new_join_old.ip_address = get_ip(request)
            new_join_old.save()
            # new_join.ip_address = get_ip(request)
            # new_join.save()
        return HttpResponseRedirect("/%s" % (new_join_old.ref_id))

    context = {"form": form}
    templates = 'home.html'
    return render(request, templates, context)


def share(request, ref_id):
    try:
        join_object = Join.objects.get(ref_id=ref_id)
        friends_referred = Join.objects.filter(friend = join_object)
        count = join_object.referral.all().count()
        ref_url = 'http://eliezerborde.com/?ref=%s' %(join_object.ref_id)
        context = {'ref_id': join_object.ref_id, 'count':count, 'ref_url':ref_url}
        templates = 'share.html'
        return render(request, templates, context)
    except:
        raise Http404
