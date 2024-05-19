
from django.urls import path
from .views import process_parameter_sample_list, process_parameter_list

urlpatterns = [
    path('process-parameter-sample/', process_parameter_sample_list, name='process-parameter-sample'),
    path('process-parameter/', process_parameter_list, name='process-parameter'),
]


'''from django.urls import path
from .views import (
    process_parameter_sample_list,
    process_parameter_sample_create,
    process_parameter_list,
    process_parameter_create
)

urlpatterns = [
    path('process-parameter-sample-list/', process_parameter_sample_list, name='process-parameter-sample-list'),
    path('process-parameter-sample-create/', process_parameter_sample_create, name='process-parameter-sample-create'),
    path('process-paramete-list/', process_parameter_list, name='process-parameter-list'),
    path('process-parameter-create/', process_parameter_create, name='process-parameter-create'),
]'''

