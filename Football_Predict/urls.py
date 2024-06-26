"""
URL configuration for Football_Predict project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Betting.views import my_table_view, PersonAPIView, PredictionAPIView, TeamAPIView, MatchAPIView, PersonListAPIView, MatchUpdateAPIView, plot_view, plot_view2, match_res

urlpatterns = [
    path('admin/', admin.site.urls),
    path('table/', my_table_view),
    path('persons/', PersonListAPIView.as_view(), name='People'),
    path('persons/<str:name>/', PersonAPIView.as_view()),
    path('predictions/', PredictionAPIView.as_view(), name='Predictions'),
    path('teams/', TeamAPIView.as_view(), name='Teams'),
    path('matches/', MatchAPIView.as_view(), name='Matches'),
    path('matches/<int:pk>/', MatchUpdateAPIView.as_view(), name='Match Update'),
    path('plot/scores/', plot_view, name='scores view'),
    path('plot/predictions/', plot_view2, name='predictions view'),
    path('plot/matches/', match_res, name='matches results'),
]