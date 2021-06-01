from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
#app_name = 'main'
urlpatterns = [
    path('', views.main,),
    path('task_show/', views.task_show, name='task_show'),
    path('task_list/', views.TaskView.as_view(), name='task_list'),
    path('filter/', views.FilterTaskView.as_view(), name='filter'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('task_update/<int:pk>', views.TaskUpdate.as_view(), name='task_update'),

    path('profile', views.update_profile, name='profile'),
    path('statistics', views.user_statistics, name='statistics'),
    

    path('import', views.import_data),
    path('export', views.export_tasks_to_xlsx,),
    path('chart', views.home),

    path('contractor', views.TaskContractorView.as_view(), name="contractor"),
    path('contask_up/<int:pk>', views.Task_ContractorUpdate.as_view(), name="task_contractor_update"),

    path('new_charts', views.new_charts),
    path('contractor-task-count-chart/', views.contractor_task_count_chart, name='contractor-task-count-chart'),
    path('status-task-count-chart/', views.status_task_count_chart, name='status-task-count-chart'),
    path('author-task-count-chart/', views.author_task_count_chart, name='author-task-count-chart'),
    path('dept-task-count-chart/', views.dept_task_count_chart, name='dept-task-count-chart'),
    path('month-task-count-chart/', views.month_task_count_chart, name='month-task-count-chart'),
    path('user-statistic-chart/', views.user_statistic_chart, name='user-statistic-chart'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
