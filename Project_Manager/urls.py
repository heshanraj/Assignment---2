from brain import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.user_tasks_list, name='user_tasks_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path("logout/", views.LogoutPage, name="logout"),
    path('', views.category_list, name='category_list'),
    path('categories/create/', views.create_category, name='create_category'),
    path('categories/<int:category_id>/', views.category_tasks, name='category_tasks'),
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),
    path('tasks/', views.user_task_list, name='user_task_list'),
    path('tasks/complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/update/<int:task_id>/', views.update_task, name='update_task'),
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('task-chart/', views.task_chart, name='task_chart'),

]

