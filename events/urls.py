from django.urls import path
from .views import Login, Logout, Signup, home
from events import views
from django.conf import settings
from django.conf.urls.static import static
from events import views as user_views

urlpatterns = [
	path('', home, name='home'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('access/', views.access, name='access'),
    path('detail/<int:event_id>/', views.event_detail, name='detail'),
    path('create/', views.event_create, name='create'),
    path('update/<int:event_id>/', views.event_update, name='update'),
    path('delete/<int:event_id>/', views.event_delete, name='delete'),
    path('book/<int:event_id>/', views.event_book, name='book'),
    path('profile/', user_views.profile, name='profile'),

    
    

]