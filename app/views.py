from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')


def result(request):
    if request.method == 'POST':
        goal = request.POST.get('user_input')
        return render(request, 'result.html', context={'goal': goal})
    else:
        return render(request, 'result.html', {'goal': ''})
