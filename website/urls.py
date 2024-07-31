from django.urls import path
from . import views


# Define the URL patterns for the application
urlpatterns = [
    # Home page URL pattern
    path('', views.home, name='home'),
    
    # URL pattern for logging out a user
    path('logout/', views.logout_user, name='logout'),
    
    # URL pattern for registering a new user
    path('register/', views.register_user, name='register'),
    
    # URL pattern for viewing a specific customer record
    # <int:pk> captures the primary key of the customer record
    path('record/<int:pk>', views.customer_record, name='record'),
    
    # URL pattern for deleting a specific customer record
    # <int:pk> captures the primary key of the customer record to be deleted
    path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
    
    # URL pattern for adding a new customer record
    path('add_record/', views.add_record, name='add_record'),
    
    # URL pattern for updating a specific customer record
    # <int:pk> captures the primary key of the customer record to be updated
    path('update_record/<int:pk>', views.update_record, name='update_record'),
]
