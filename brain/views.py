from django.contrib.auth import login, logout
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Category
from .models import Task
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required

#function to check and see if the user is an admin or not
def is_admin(user):
    return user.is_superuser

#this is a decorator used to restict the view access to admin users only
admin_required = user_passes_test(lambda user: user.is_superuser)

#vieww to handle user login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.is_superuser:  # If the user is an admin
                return redirect('category_list')
            else:  # If the user is a normal user
                return redirect('user_tasks_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

#view to display tasks assigned to the logged in user
@login_required
def user_tasks_list(request):
    tasks = request.user.tasks.all() # it fetces the tasks that were assigned to the logged-in user
    return render(request, 'user_task_list.html', {'tasks': tasks})

# A form for user user registration
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# a form for user login
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

#view to handle user registrationn
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save() #save the new users
            # login(request, user)
            return redirect('login') #redirects to the login page after succesful registration
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

# view to handle logout page
def LogoutPage(request):
    logout(request) # logouts the current users
    return redirect("login") # then it redirects them to the login page after they log out


# view to delete a task, but only for admins
@login_required
@admin_required
def delete_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.delete()
    return redirect(reverse('category_list'))


#View to create a new task, only for admins
@login_required
@admin_required
def create_task(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        priority = request.POST.get('priority')
        description = request.POST.get('description')
        location = request.POST.get('location')
        assigned_to_id = request.POST.get('assigned_to')

        category = Category.objects.get(pk=category_id)

        # Use the current user as the organiser
        organiser = request.user

        task = Task.objects.create(
            name=name,
            category=category,
            start_date=start_date,
            end_date=end_date,
            priority=priority,
            description=description,
            location=location,
            organiser=organiser,  # Ensure organiser is set
            assigned_to_id=int(assigned_to_id)
        )

        return redirect('category_list')
    else:
        categories = Category.objects.all()
        users = User.objects.all()
        return render(request, 'create_task.html', {'categories': categories, 'users': users})


#A view to update an existing taask, just for admin
@login_required
@admin_required
def update_task(request, task_id):
    task = Task.objects.get(pk=task_id)
    if request.method == 'POST':
        # Update task fields based on form data
        task.name = request.POST.get('name')
        task.start_date = request.POST.get('start_date')
        task.end_date = request.POST.get('end_date')
        task.priority = request.POST.get('priority')
        task.description = request.POST.get('description')
        task.location = request.POST.get('location')
        task.organiser = request.POST.get('organiser')
        task.assigned_to_id = request.POST.get('assigned_to')
        task.save()
        return redirect('category_list')
    else:
        # Render the update task page with task data
        return render(request, 'update_task.html', {'task': task})


#view to display a list of categories, just for admins
@login_required
@admin_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

# A vuew to create a new category for admins
@login_required
@admin_required
def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Category.objects.create(name=name)
        return redirect('category_list')
    return render(request, 'create_category.html')

#vuew to delete a category, just for da admin !
@login_required
@admin_required
def delete_category(request, category_id):
    category = Category.objects.get(pk=category_id)
    if category.task_set.exists():
        messages.error(
            request, "You cannot delete this category as it contains tasks.")
    else:
        category.delete()
        messages.success(request, "Category deleted successfully.")
    return redirect('category_list')


#view to display task witithin a specific category, AADMIINN ONLY!!!!
@login_required
@admin_required
def category_tasks(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    tasks = category.task_set.all()
    return render(request, 'category_tasks.html', {'category': category, 'tasks': tasks})

# VIEW TO display a cHART of pending tasks in each category admins only
@login_required
@admin_required
def task_chart(request):
    categories = Category.objects.all()
    pending_counts = {}
    for category in categories:
        pending_counts[category.name] = Task.objects.filter(
            category=category,
            start_date__gt=timezone.now()
        ).count()
    return render(request, 'task_chart.html', {'pending_counts': pending_counts})


# View to display tasks within a specific category for the logged-in user. NO MORE ADMIN :(
@login_required
def category_task(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    tasks = Task.objects.filter(category=category).order_by('-priority')
    return render(request, 'category_tasks.html', {'category': category, 'tasks': tasks})

#Vuew to display tasks assigned to the logged-in user
@login_required
def user_task_list(request):
    user = request.user
    tasks = Task.objects.filter(assigned_to=user).order_by('-priority')
    categories = Category.objects.all()
    return render(request, 'user_task_list.html', {'tasks': tasks, 'categories': categories})

# View to mark a task as complete or incomplete
@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == 'POST':
        task.is_completed = not task.is_completed
        task.save()
    return redirect('user_task_list')

