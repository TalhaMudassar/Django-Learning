from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import httpx
import time
import asyncio
def home(request):
  return HttpResponse('Hello Home Page')

# async def home(request):
#   return HttpResponse('Hello Home Page')

# Synchronous View
def sync_view(request):
  start_time = time.time()
  responses = []

  for _ in range(5):
    response = httpx.get("https://jsonplaceholder.typicode.com/posts")
    responses.append(response.json())

  end_time = time.time()
  time_taken = end_time - start_time
  return JsonResponse({
    'status':'success',
    'total_request':5,
    'time_taken': f"{time_taken:.2f} seconds"
  })

# Asynchronous View
async def async_view(request):
  start_time = time.time()

  async with httpx.AsyncClient() as client:
    tasks = [client.get("https://jsonplaceholder.typicode.com/posts") for _ in range(5)]
    responses = await asyncio.gather(*tasks)
  
  end_time = time.time()
  time_taken = end_time - start_time
  return JsonResponse({
    'status':'success',
    'total_request':5,
    'time_taken': f"{time_taken:.2f} seconds"
  })
