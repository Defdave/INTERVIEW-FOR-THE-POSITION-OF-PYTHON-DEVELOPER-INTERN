from django.shortcuts import render, get_object_or_404,  redirect
from .models import PollingUnit, AnnouncedPUResults, LGA, Ward, State
from django.db.models import Sum
from .forms import PollingUnitForm
from .forms import ResultForm
from django.http import JsonResponse
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def polling_unit_results(request):
    form = PollingUnitForm()  # Initialize form

    if request.method == 'POST':
        form = PollingUnitForm(request.POST)
        if form.is_valid():
            polling_unit_id = form.cleaned_data['polling_unit_id']
            polling_unit = get_object_or_404(PollingUnit, uniqueid=polling_unit_id)
            results = AnnouncedPUResults.objects.filter(polling_unit_uniqueid=polling_unit_id)

            context = {
                'form': form,  # Pass the form instance back
                'polling_unit': polling_unit,
                'results': results,
            }
            return render(request, 'polling_unit_results.html', context)
    
    # Render the form with no results initially or if form is invalid
    return render(request, 'polling_unit_results.html', {'form': form})


def lga_results(request):
    lgas = PollingUnit.objects.values('lga_id').distinct()

    if request.method == 'POST':
        lga_id = request.POST.get('lga_id')
        if lga_id:
            results = (
                AnnouncedPUResults.objects
                .filter(polling_unit_uniqueid=lga_id)
                .values('party_abbreviation')
                .annotate(total_score=Sum('party_score'))
            )
            lga_name = LGA.objects.filter(lga_id=lga_id).first().lga_name
            return render(request, 'lga_results.html', {'results': results, 'lga_name': lga_name, 'lgas': lgas})

    return render(request, 'lga_results.html', {'lgas': lgas})

def add_polling_unit_results(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Results added successfully!')
            return redirect('add_polling_unit_results')
    else:
        form = ResultForm()

    return render(request, 'add_polling_unit_results.html', {'form': form})


def polling_unit_list(request):
    ward_id = request.GET.get('ward_id')
    polling_units = PollingUnit.objects.filter(ward_id=ward_id).order_by('polling_unit_id')
    return JsonResponse({
        'polling_units': list(polling_units.values('id', 'polling_unit_id'))
    })