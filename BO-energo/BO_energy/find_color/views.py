from django.shortcuts import render
from .forms import Get_color
from .models import Number_info


def color_finder(request):
    if request.method == 'POST':
        form = Get_color(request.POST)
        if form.is_valid():
            find_number = form.cleaned_data['number']
            if find_number <= 19:
                form.cleaned_data['color'] = 'red'
                save_color = Number_info.objects.create(**form.cleaned_data)
            if find_number >= 20 and find_number <= 48:
                form.cleaned_data['color'] = 'green'
                save_color = Number_info.objects.create(**form.cleaned_data)
            if find_number >= 49:
                form.cleaned_data['color'] = 'blue'
                save_color = Number_info.objects.create(**form.cleaned_data)
        else:
            print("data not found")
    else:
        form = Get_color()
    return render(request, 'find_color/index.html', {'form': form})

def out_all_color(request):
    all_colors = Number_info.objects.all()
    context = {
        'all_colors': all_colors,
    }
    return render(request, 'find_color/out_all_data.html', context)
