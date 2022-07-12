from django.urls import path

from .views import *


urlpatterns = [
    path('',register_view,name='register'),
    path('login/',login_view,name='login'),
    path("logout/", logout_view, name="logout"),
    path('show/',show_student,name='show'),
    path('add/',add_student,name='add'),
    path('update/<int:sid>/',update_student,name='update'),
    path('delete/<int:sid>/',delete_view,name='delete'),
    path('addsingle/',add_single,name='addsingle'),
    path('showmark/',show_marks,name='showmark'),
    path('marks/<int:mid>/',marks_student_delete,name='marks'),
    path("addmarks/",add_marks, name="addmark"),
    path('updatemark/<int:mid>/',marks_update,name='marksupdate')
]
