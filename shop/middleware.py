import json
from django.utils.deprecation import MiddlewareMixin


class SaveHTTPRequestMiddleware(MiddlewareMixin):
    """Сохраняет в БД данные из request.META """
    
    def process_request(self, request):
        try:
            from http_head.models import HttpHead
            
        except Exception as e:
            return None
        else:
            data = {}
            for key, value in request.META.items():
                key = key.replace('"', "'")
                data[key] = str(value).replace('"', "'")
            new = HttpHead()
            new.data = json.dumps(data, ensure_ascii=False)
            new.save()
            
        return None

    def process_response(self, request, response):
        return response
    
    def process_view(self, request, view, args, kwargs):
        return None
        
    def process_template_response(self, request, response):
        return response
        
    def process_exception(self, request, exception):
        return None
