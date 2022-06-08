from django.shortcuts import render
from django.template.loader import render_to_string
from .forms import Get_data_square
# Create your views here.

def math_square(request):
    if request.method == 'POST':
        form = Get_data_square(request.POST)
        if form.is_valid():
            value_a = form.cleaned_data['value_a']
            value_b = form.cleaned_data['value_b']
            value_c = form.cleaned_data['value_c']
            result = (value_b*value_b) - (4*value_a*value_c)
            if result < 0:
                answer = 'None'
                context = {
                    'answer': answer
                }
                print(context)
                return render(request, 'square/index.html', context)
            if result == 0:
                answer = -value_b / (2*value_a)
                context = {
                    'answer': str(answer)
                }
                print(context)
                return render(request, 'square/index.html', context)
            if result > 0:
                answer1 = (-value_b+((value_b*value_b)-(4*value_a*value_c))**0.5)/(2*value_a)
                answer2 = (-value_b-((value_b*value_b)-(4*value_a*value_c))**0.5)/(2*value_a)
                answer = [answer1, answer2]
                context = {
                    'answer': answer
                }
                print(context)
                return render(request, 'square/index.html', context)
    else:
        form = Get_data_square()
    return render(request, 'square/index.html', {'form': form})
