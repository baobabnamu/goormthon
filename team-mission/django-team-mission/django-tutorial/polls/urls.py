from django.urls import include, path
from rest_framework import routers
from polls import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'choices', views.ChoiceViewSet)

from . import views

app_name = "polls"
urlpatterns = [
    # Django 템플릿 기반 URL
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    
    # API URL
    path('api/', include([
        path('', include(router.urls)),
    ]))
]