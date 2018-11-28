from django.shortcuts import render
from .models import HttpHead
import json

def home(request):
    qs = HttpHead.objects.all()
    if qs.count() > 10:
        qs = qs[:10]
    data = []
    for q in qs:
        data.append(json.loads(q.data))
    context = {}
    context['objects_list'] = data
    return render(request, 'http_head/home.html', context)
