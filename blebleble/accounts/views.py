from django.shortcuts import render

from .forms import UserForm
# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Usuario criado com sucesso!')
    else:
        form = UserForm()
    return render(request, 'accounts/add_user.html', {'form': form})
