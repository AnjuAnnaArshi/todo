from django.urls import path

from todoapp1 import views
# app_name= 'todoapp'
urlpatterns = [
      path('',views.home,name='home'),
      path('delete/<int:taskid>/',views.delete,name='delete'),
      path('update/<int:taskid>/',views.update,name='update'),
      path('classhome/',views.tasklist.as_view(),name='classhome'),
      path('detailview/<int:pk>/',views.taskdetails.as_view(),name='detailview'),
      path('classupdate/<int:pk>/', views.taskupdate.as_view(), name='classupdate'),
      path('deletetask/<int:pk>/', views.deleteview.as_view(), name='deletetask')

      # path('details',views.details,name='details')
]
