from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import FormData

def dynamic_form(request):
    if request.method == 'POST':
        # Очистка базы перед сохранением новых данных
        FormData.objects.all().delete()
        
        latitudes = request.POST.getlist('lat')
        longitudes = request.POST.getlist('lng')
        
        for lat, lng in zip(latitudes, longitudes):
            lat_val = float(lat) if lat.strip() else 0.0
            lng_val = float(lng) if lng.strip() else 0.0
            
            FormData.objects.create(
                latitude=lat_val,
                longitude=lng_val
            )
            
        return redirect('success')
    
    return render(request, 'form.html')

def success_view(request):
    data = FormData.objects.all().order_by('-created_at')
    return render(request, 'success.html', {'data': data})

@csrf_exempt  # Временно для тестирования
def save_data(request):
    if request.method == 'POST':
        try:
            lat = float(request.POST.get('lat'))
            lng = float(request.POST.get('lng'))
            inputs = request.POST.getlist('inputs[]')
            
            FormData.objects.create(
                latitude=lat,
                longitude=lng,
                additional_inputs=inputs
            )
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
    return JsonResponse({'status': 'error'})