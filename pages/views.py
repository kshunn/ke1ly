from django.shortcuts import render


# Create your views here.
def about(request):
    return render(request, 'about.html')


def main(request):
    return render(request, 'main.html')
