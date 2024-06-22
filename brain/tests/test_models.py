import pytest
from django.contrib.auth.models import User
from brain.models import Category, Task
from django.utils import timezone
from datetime import timedelta




@pytest.mark.django_db
def test_category_creation():
    category = Category.objects.create(name="Test Category")
    assert category.name == "Test Category"
    assert str(category) == "Test Category"  # Ensurse the string representation is correct

@pytest.mark.django_db
def test_task_str():
    user = User.objects.create_user(username='testuser', password='password')
    category = Category.objects.create(name="Test Category")
    start_date = timezone.now()
    end_date = start_date + timedelta(days=1)

    task = Task.objects.create(
        name="Test Task",
        category=category,
        assigned_to=user,
        start_date=start_date,
        end_date=end_date,
        priority="High",
        description="Test Description",
        location="Test Location",
        organiser=user,
        is_completed=False
    )

    assert str(task) == "Test Task"  # Ensures the string representation is correct

@pytest.mark.django_db
def test_task_creation():
    user = User.objects.create_user(username='testuser', password='password')
    category = Category.objects.create(name="Test Category")
    start_date = timezone.now()
    end_date = start_date + timedelta(days=1)

    task = Task.objects.create(
        name="Test Task",
        category=category,
        assigned_to=user,
        start_date=start_date,
        end_date=end_date,
        priority="High",
        description="Test Description",
        location="Test Location",
        organiser=user,
        is_completed=False
    )

    assert task.name == "Test Task"
    assert task.category == category
    assert task.assigned_to == user
    assert task.start_date == start_date
    assert task.end_date == end_date
    assert task.priority == "High"
    assert task.description == "Test Description"
    assert task.location == "Test Location"
    assert task.organiser == user
    assert not task.is_completed  # Ensures the task is not completed

@pytest.mark.django_db
def test_task_duration():
    user = User.objects.create_user(username='testuser', password='password')
    category = Category.objects.create(name="Test Category")
    start_date = timezone.now()
    end_date = start_date + timedelta(days=1)

    task = Task.objects.create(
        name="Test Task",
        category=category,
        assigned_to=user,
        start_date=start_date,
        end_date=end_date,
        priority="High",
        description="Test Description",
        location="Test Location",
        organiser=user,
        is_completed=False
    )

    duration = task.end_date - task.start_date
    assert duration == timedelta(days=1)  # Ensurez the task duration is correct


@pytest.mark.django_db
def test_task_completion():
    user = User.objects.create_user(username='testuser', password='password')
    category = Category.objects.create(name="Test Category")
    start_date = timezone.now()
    end_date = start_date + timedelta(days=1)

    task = Task.objects.create(
        name="Test Task",
        category=category,
        assigned_to=user,
        start_date=start_date,
        end_date=end_date,
        priority="High",
        description="Test Description",
        location="Test Location",
        organiser=user,
        is_completed=False
    )

    task.is_completed = True
    task.save()
    task.refresh_from_db()

    assert task.is_completed  # Ensures the task is marked as completed


@pytest.mark.django_db
def test_task_category_relationship():
    user = User.objects.create_user(username='testuser', password='password')
    category = Category.objects.create(name="Test Category")
    start_date = timezone.now()
    end_date = start_date + timedelta(days=1)

    task1 = Task.objects.create(
        name="Test Task 1",
        category=category,
        assigned_to=user,
        start_date=start_date,
        end_date=end_date,
        priority="High",
        description="Test Description 1",
        location="Test Location 1",
        organiser=user,
        is_completed=False
    )

    task2 = Task.objects.create(
        name="Test Task 2",
        category=category,
        assigned_to=user,
        start_date=start_date,
        end_date=end_date,
        priority="Medium",
        description="Test Description 2",
        location="Test Location 2",
        organiser=user,
        is_completed=True
    )

    assert category.task_set.count() == 2  # Ensures both tasks are related to the category

