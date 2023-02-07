from django.shortcuts import render, redirect
from .models import Group
from .forms import GroupForm


def group_list(request):
    groups = Group.objects.all()
    return render(request, 'group/index.html', {'groups': groups})


def group_create(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/group')
    return render(request, 'group/group_form.html', {'form': form})


def group_update(request, id):
    group = Group.objects.get(id=id)
    form = GroupForm(request.POST or None, instance=group)
    if form.is_valid():
        form.save()
        return redirect('/group')
    return render(request, 'group/group_form.html', {'form': form, 'group': group})


def group_delete(request, id):
    Group.objects.get(id=id).delete()
    return redirect('/group')
