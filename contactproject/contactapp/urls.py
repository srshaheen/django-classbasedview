from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactList.as_view(), name='contact_list'),
    path('detail/<int:pk>', views.ContactDetails.as_view(), name='contact_details'),
    path('create/', views.CreateContact.as_view(), name='create_contact'),
    path('update/<int:pk>', views.ContactUpdate.as_view(), name='contact_update'),
    path('delete/<int:pk>', views.ContactDelete.as_view(), name='contact_delete'),

]
