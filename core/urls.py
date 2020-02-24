from django.urls import path,include

app_name = 'core'

urlpatterns = [
    path('classes/',include('core.apiv1.urls.gymclass')),
    path('attendance/',include('core.apiv1.urls.attendance')),
]
