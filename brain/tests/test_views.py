import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from brain.models import Category, Task
from django.utils import timezone
import datetime

# testing how realiable our logging in functionality is
@pytest.mark.django_db
def test_user_login(client):
    user = User.objects.create_user(username="testuser", password="testpass")
    response = client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
    assert response.status_code == 302  # Redirects after login to the tasks and stuff

# Test user registration functionality
@pytest.mark.django_db
def test_user_registration(client):
    response = client.post(reverse('register'), {
        'username': 'newuser',
        'password1': 'ComplexPass123!',
        'password2': 'ComplexPass123!'
    })

    if response.status_code != 302:
        print("Status Code:", response.status_code)
        print("Response Content:", response.content.decode())  # Print the response content for debugging
        print("Form Errors:", response.context['form'].errors)  # Print form errors if available

    assert response.status_code == 302  # Redirects after registration
    assert User.objects.filter(username='newuser').exists()

# Test creating a new task functionality
@pytest.mark.django_db
def test_create_task_view(client):
    user = User.objects.create_superuser(username="admin", password="adminpass")
    client.login(username="admin", password="adminpass")

    category = Category.objects.create(name="Test Category")
    start_time = timezone.now()
    end_time = start_time + datetime.timedelta(days=1)

    task_data = {
        'name': 'Test Task',
        'category': category.id,
        'start_date': start_time.isoformat(),
        'end_date': end_time.isoformat(),
        'priority': 'High',
        'description': 'This is a test task',
        'location': 'Test Location',
        'assigned_to': user.id,
    }

    response = client.post(reverse('create_task'), data=task_data)
    assert response.status_code == 302  # Redirects after creation
    assert Task.objects.filter(name='Test Task').exists()

# Test deleting a task functionality
@pytest.mark.django_db
def test_delete_task_view(client):
    user = User.objects.create_superuser(username="admin", password="adminpass")
    client.login(username="admin", password="adminpass")

    category = Category.objects.create(name="Test Category")
    task = Task.objects.create(
        name="Test Task",
        category=category,
        assigned_to=user,
        start_date=timezone.now(),
        end_date=timezone.now() + datetime.timedelta(days=1),
        priority="High",
        description="This is a test task",
        location="Test Location",
        organiser=user
    )

    response = client.post(reverse('delete_task', args=[task.id]))
    assert response.status_code == 302  # Redirects after deletion
    assert not Task.objects.filter(name='Test Task').exists()


# Test updating a task functionality
@pytest.mark.django_db
def test_update_task_view(client):
    user = User.objects.create_superuser(username="admin", password="adminpass")
    client.login(username="admin", password="adminpass")

    category = Category.objects.create(name="Test Category")
    task = Task.objects.create(
        name="Test Task",
        category=category,
        assigned_to=user,
        start_date=timezone.now(),
        end_date=timezone.now() + datetime.timedelta(days=1),
        priority="High",
        description="This is a test task",
        location="Test Location",
        organiser=user
    )

    updated_data = {
        'name': 'Updated Task',
        'start_date': (timezone.now() + datetime.timedelta(days=1)).isoformat(),
        'end_date': (timezone.now() + datetime.timedelta(days=2)).isoformat(),
        'priority': 'Medium',
        'description': 'This is an updated task',
        'location': 'Updated Location',
        'assigned_to': user.id,
    }

    response = client.post(reverse('update_task', args=[task.id]), data=updated_data)
    assert response.status_code == 302  # Redirects after update
    task.refresh_from_db()
    assert task.name == 'Updated Task'
    assert task.priority == 'Medium'
    assert task.location == 'Updated Location'

@pytest.mark.django_db
def test_create_category_view(client):
    user = User.objects.create_superuser(username="admin", password="adminpass")
    client.login(username="admin", password="adminpass")

    response = client.post(reverse('create_category'), {'name': 'New Category'})
    assert response.status_code == 302  # Redirects after creation
    assert Category.objects.filter(name='New Category').exists()

@pytest.mark.django_db
def test_delete_category_view(client):
    user = User.objects.create_superuser(username="admin", password="adminpass")
    client.login(username="admin", password="adminpass")

    category = Category.objects.create(name="Category to Delete")
    response = client.post(reverse('delete_category', args=[category.id]))
    assert response.status_code == 302  # Redirects after deletion
    assert not Category.objects.filter(name='Category to Delete').exists()

@pytest.mark.django_db
def test_category_tasks_view(client):
    user = User.objects.create_superuser(username="admin", password="adminpass")
    client.login(username="admin", password="adminpass")

    category = Category.objects.create(name="Test Category")
    Task.objects.create(
        name="Test Task",
        category=category,
        assigned_to=user,
        start_date=timezone.now(),
        end_date=timezone.now() + datetime.timedelta(days=1),
        priority="High",
        description="This is a test task",
        location="Test Location",
        organiser=user
    )

    response = client.get(reverse('category_tasks', args=[category.id]))
    assert response.status_code == 200
    assert 'category' in response.context
    assert 'tasks' in response.context
    assert response.context['category'] == category
    assert response.context['tasks'].count() == 1

@pytest.mark.django_db
def test_user_tasks_list_view(client):
    user = User.objects.create_user(username="testuser", password="testpass")
    client.login(username="testuser", password="testpass")

    category = Category.objects.create(name="Test Category")
    Task.objects.create(
        name="Test Task",
        category=category,
        assigned_to=user,
        start_date=timezone.now(),
        end_date=timezone.now() + datetime.timedelta(days=1),
        priority="High",
        description="This is a test task",
        location="Test Location",
        organiser=user
    )

    response = client.get(reverse('user_tasks_list'))
    assert response.status_code == 200
    assert 'tasks' in response.context
    assert response.context['tasks'].count() == 1

@pytest.mark.django_db
def test_complete_task_view(client):
    user = User.objects.create_user(username="testuser", password="testpass")
    client.login(username="testuser", password="testpass")

    category = Category.objects.create(name="Test Category")
    task = Task.objects.create(
        name="Test Task",
        category=category,
        assigned_to=user,
        start_date=timezone.now(),
        end_date=timezone.now() + datetime.timedelta(days=1),
        priority="High",
        description="This is a test task",
        location="Test Location",
        organiser=user
    )

    response = client.post(reverse('complete_task', args=[task.id]))
    assert response.status_code == 302  # Redirects after marking as complete
    task.refresh_from_db()
    assert task.is_completed
