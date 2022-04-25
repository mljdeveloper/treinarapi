from django.http import JsonResponse

def api_home (request, *args, **kwargs):
    return JsonResponse({"message": "Vai Corinthians"})

# Create your views here.
