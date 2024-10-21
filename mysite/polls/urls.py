from django.urls import path
from . import views

# namespace:
app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/5
    path("<int:question_id>/", views.detail, name='detail'),
    # /polls/5/result
    path("<int:question_id>/results/", views.results, name="results"),
    # /plls/5/vote
    path("<int:question_id>/vote/", views.vote, name='vote'),
]
