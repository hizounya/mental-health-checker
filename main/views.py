from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306245661',
        'name': 'Hizounya',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
