from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLoginView, RegisterPage, \
    GroupTaskList, BoardList, GroupTaskCreate, GroupTaskUpdate, GroupTaskDelete
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('gtasks/<int:group_tasks_id>/tasks/', TaskList.as_view(), name='tasks'),
    path('gtasks/', GroupTaskList.as_view(), name='gtasks'),
    path('', BoardList.as_view(), name='boards'),
    path('gtasks/<int:group_tasks_id>/task/<int:pk>/', TaskDetail.as_view(), name='task'),
    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('gtasks/<int:group_tasks_id>/task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('gtasks/<int:group_tasks_id>/task-delete/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
    path('gtask-create/', GroupTaskCreate.as_view(), name='gtask-create'),
    path('gtask-update/<int:pk>/', GroupTaskUpdate.as_view(), name='gtask-update'),
    path('gtask-delete/<int:pk>/', GroupTaskDelete.as_view(), name='gtask-delete'),
]
