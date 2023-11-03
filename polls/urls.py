# polls/urls.py
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required  # Add this import

urlpatterns = [
    path('', login_required(views.poll_list), name='poll_list'),
    path('<int:poll_id>/', login_required(views.poll_detail), name='poll_detail'),
    path('<int:poll_id>/vote/', login_required(views.vote), name='vote'),
    path('<int:poll_id>/results/', login_required(views.poll_results), name='poll_results'),

]
