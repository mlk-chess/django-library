from django.shortcuts import render, redirect
from .models import readingGroup
from .forms import GroupForm


def group_list(request):
    groups = readingGroup.objects.all()
    return render(request, 'group/index.html', {'groups': groups})


def group_create(request):
    form = GroupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/group')
    return render(request, 'group/group_form.html', {'form': form})


def group_update(request, id):
    group = readingGroup.objects.get(id=id)
    form = GroupForm(request.POST or None, instance=group)
    if form.is_valid():
        form.save()
        return redirect('/group')
    return render(request, 'group/group_form.html', {'form': form, 'group': group})


def group_delete(request, id):
    readingGroup.objects.get(id=id).delete()
    return redirect('/group')


def group_details(request, group_id):
    group = readingGroup.objects.get(id=group_id)
    members = group.members.all()
    return render(request, 'group/group_details.html', {'group': group, 'members': members})


def join_group(request, group_id):
    group = readingGroup.objects.get(id=group_id)
    user = request.user
    group.members.add(user)
    return redirect('/group', group_id=group_id)
