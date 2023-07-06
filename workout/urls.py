from . import views
from django.urls import path

app_name = 'workout'
urlpatterns = [
    path('signup/', views.MySignupView.as_view(), name='signup'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('user/', views.MyUserView.as_view(), name='user'),
    # path('other/', views.MyOtherView.as_view(), name='other'),
    path('changeweight/', views.UserWightChangeView.as_view(), name='changeweight'),
    path('choicetraining/', views.ChoiceTrainingView.as_view(), name='choicetraining'),
    path('choicerecord/', views.ChoiceRecordView.as_view(), name='choicerecord'),
    
]