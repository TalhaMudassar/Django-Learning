from django.shortcuts import render
from myapp.models import Student

# ================================
#   Sync View Example
# ================================
def home(request):
    # Synchronous Query
    students = Student.objects.all()
    for student in students:
        print(f"name: {student.name}  age: {student.age}  email: {student.email}")

    return render(request, 'myapp/home.html', {'students': students})


# ================================
#   Async View Example - Method 1
# ================================
async def home(request):
    # Async iteration directly (❌ not supported on plain QuerySet)
    async for student in Student.objects.all():
        print(f"name: {student.name}  age: {student.age}  email: {student.email}")

    return render(request, 'myapp/home.html')


# ================================
#   Async View Example - Method 2
# ================================
async def home(request):
    # Using aiterator() ✅ (correct way)
    students = Student.objects.all()

    async for student in students.aiterator():
        print(f"name: {student.name}  age: {student.age}  email: {student.email}")

    return render(request, 'myapp/home.html', {'students': students})


# ================================
#   Async View Example - Other Async ORM Methods
# ================================
async def home(request):
    # Example: Async iteration
    async for student in Student.objects.all().aiterator():
        print(f"name: {student.name}  age: {student.age}  email: {student.email}")

    # Example: Async create
    await Student.objects.acreate(
        name='kunal',
        age=30,
        email='kunal@example.com'
    )

    # Example: Async count
    total_students = await Student.objects.acount()
    print(total_students)

    # Example: Async get by primary key
    student = await Student.objects.aget(pk=1)
    print(f"name: {student.name}  age: {student.age}  email: {student.email}")

    # Example: Async delete
    student = await Student.objects.aget(pk=4)
    await student.adelete()

    return render(request, 'myapp/home.html')
