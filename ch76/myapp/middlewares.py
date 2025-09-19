from asgiref.sync import iscoroutinefunction, markcoroutinefunction
from django.utils.decorators import sync_and_async_middleware, sync_only_middleware, async_only_middleware

@sync_and_async_middleware
# @sync_only_middleware
# @async_only_middleware
def my_fun_middleware(get_response):
    print("One-time initialization")
    if iscoroutinefunction(get_response):
        async def middleware(request):
            print(f"Before view (Async): {request.path}")
            # Call Next Middleware or Final View
            response = await get_response(request)
            print(f"After view (Async): {request.path}")
            return response
    else:
        def middleware(request):
            print(f"Before view (Sync): {request.path}")
            # Call Next Middleware or Final View
            response = get_response(request)
            print(f"After view (Sync): {request.path}")
            return response

    return middleware

class MyAsyncClassMiddleware:
    async_capable = True
    sync_capable = False

    def __init__(self, get_response):
        self.get_response = get_response
        if iscoroutinefunction(self.get_response):
            markcoroutinefunction(self)
        print("One-time initialization")

    async def __call__(self, request):
        print(f"Before view (Async): {request.path}")
        # Call Next Middleware or Final View
        response = await self.get_response(request)
        print(f"After view (Async): {request.path}")
        return response

class MySyncClassMiddleware:
    async_capable = False
    sync_capable = True

    def __init__(self, get_response):
        self.get_response = get_response
        print("One-time initialization")

    def __call__(self, request):
        print(f"Before view (Sync): {request.path}")
        # Call Next Middleware or Final View
        response = self.get_response(request)
        print(f"After view (Sync): {request.path}")
        return response

