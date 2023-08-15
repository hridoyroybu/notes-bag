from django.urls import path
from . import views

urlpatterns = [
    path('', views.showTasks),
    path('show-tasks/', views.showTasks, name='show-tasks'),
    path('create-tasks/', views.createTasks, name='create-tasks'),
    path('edit-tasks/<int:id>', views.editTasks, name='edit-tasks'),
    path('delete-tasks/<int:id>', views.deleteTasks, name='delete-tasks'),
    path('completed-tasks/', views.completedTasks, name='completed-tasks'),
    path('complete-tasks/<int:id>', views.completeTask, name='complete-tasks'),
    path('add-category/<int:id>/<int:cat>', views.addCategory, name='add-category'),
    path('filter-note/<int:id>', views.filterNoteCategory, name='filter-note'),
]
