"""event_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls')),

    path('events/list/', views.UpcomingList.as_view(), name="events-list"),
    #error
    path('organizer/list/<int:organizer_id>/', views.OrganizerList.as_view(), name="organizer-list"),

    
    path('user/list/', views.UserList.as_view(), name="user-list"), 

    path('event/book/<int:event_id>/', views.BookingEvent.as_view(), name="book-event"),      
    path('create/event/', views.CreateEvent.as_view(), name="create-event"),

    path('event/modify/<int:event_id>/', views.ModifyEvent.as_view(), name="modify-event"),
    
    
    path('event/<int:event_id>/attendants/', views.AttendantsView.as_view(), name="event-attendants"),

    path('log/', TokenObtainPairView.as_view(), name="login"),
    path('register/',  views.Register.as_view() , name="register"),
]



if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)