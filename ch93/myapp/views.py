from django.http import HttpResponse, JsonResponse
from django.views import View
import httpx
import time
import asyncio

# Home View (Async)
class HomeView(View):
    async def get(self, request, *args, **kwargs):
        return HttpResponse("Hello Home Page")


# Synchronous Class-Based View
class SyncView(View):
    def get(self, request, *args, **kwargs):
        start_time = time.time()
        responses = []

        for _ in range(5):
            response = httpx.get("https://jsonplaceholder.typicode.com/posts")
            responses.append(response.json())

        end_time = time.time()
        time_taken = end_time - start_time
        return JsonResponse({
            'status': 'success',
            'view_type': 'sync',
            'total_request': 5,
            'time_taken': f"{time_taken:.2f} seconds"
        })


# Asynchronous Class-Based View
class AsyncView(View):
    async def get(self, request, *args, **kwargs):
        start_time = time.time()

        async with httpx.AsyncClient() as client:
            tasks = [client.get("https://jsonplaceholder.typicode.com/posts") for _ in range(5)]
            responses = await asyncio.gather(*tasks)

        end_time = time.time()
        time_taken = end_time - start_time
        return JsonResponse({
            'status': 'success',
            'view_type': 'async',
            'total_request': 5,
            'time_taken': f"{time_taken:.2f} seconds"
        })
