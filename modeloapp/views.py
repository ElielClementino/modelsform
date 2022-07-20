from django.shortcuts import render
from modeloapp.forms import UserForm


def formulario(request):   
    if request.method == 'GET':
        form = UserForm()
        context = {
            'form': form
        }
        return render(request,'index.html', context=context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            userform = form.save()
            form = UserForm()
        context = {
            'form': form
        }
        return render(request,'index.html', context=context)