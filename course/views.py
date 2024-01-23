from django.http import JsonResponse
from .models import Course
import requests
import time

def get_current_usd(request):
    last_rate = Course.objects.order_by('-date').first()
    if last_rate and (time.time() - last_rate.date.timestamp() < 10):
        return JsonResponse({'error': 'Please wait at least 10 seconds between requests'}, status=429)
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    data = response.json()
    rate = data['rates']['RUB']
    Course.objects.create(rate=rate)
    last_10_rates = Course.objects.order_by('-date')[:10]
    result = {'rate': rate, 'last_10_rates': list(last_10_rates.values())}
    return JsonResponse(result)
