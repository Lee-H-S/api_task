from django.urls import path, include

"""
URLs for the API
"""

urlpatterns = [
    path('api/', include('api.urls')),
    path('users/', include('users.urls'))
]
