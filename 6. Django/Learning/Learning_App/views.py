from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Model  
from .forms import Form

# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Welcome to Website</h1>")

def home(request):
    content = Model.objects.all()
    context = {'content': content}
    return render(request, 'home.html', context=context)


def vform(request):
    # context = {}
    # context['form'] = Form
    # return render(request, 'form.html', context=context)

    if request.method == 'POST':
        form = Form(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("home")
        else:

            # uncomment the below line to see errors
            # in the form (if any)
            # print(form.errors)
            return render(request, "form.html", {"form": form})
    else:
        context = {}
        context['form'] = Form
        return render(request, "form.html", context=context)