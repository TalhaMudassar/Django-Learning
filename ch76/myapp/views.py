from django.shortcuts import HttpResponse

async def async_view(request):
    print("Inside Async view")
    return HttpResponse("Async View Page")

def sync_view(request):
    print("Inside Sync view")
    return HttpResponse("Sync View Page")
