from django.urls import path

from webapp.views import index_view, nums_history_view

urlpatterns = [
    path('', index_view),
    path('history/', nums_history_view),
]
