from django.shortcuts import render
from .forms import PeselForm
from .utils import validate_pesel, extract_pesel_data


def pesel_validator(request):
    context = {}
    if request.method == 'POST':
        form = PeselForm(request.POST)
        if form.is_valid():
            pesel = form.cleaned_data['pesel']
            is_valid = validate_pesel(pesel)
            context['is_valid'] = is_valid
            context['pesel'] = pesel

            if is_valid:
                data = extract_pesel_data(pesel)
                if data:
                    context.update(data)
                else:
                    context['is_valid'] = False
                    context['error'] = "Nieprawidłowa data w PESEL"
    else:
        form = PeselForm()

    context['form'] = form
    return render(request, 'pesel_form.html', context)