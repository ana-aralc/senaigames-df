# urls exclusivas do app crud_base
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    # path('sou_membro/',views.sou_membro,name='sou_membro'),
    path('membro/',views.autentica_membro,name='membro'),
]

# urls exclusivas do aplicativo crud_base
# from django.urls import path
# from . import views
# urlpatterns=[
#    path('',views.index,name='index'),
#    path('membro/',views.autentica_membro,name='membro'),
 
# ]

# urls exclusivas do aplicativo crud_base
# from django.urls import path
# from . import views
# urlpatterns=[
#    path('',views.index,name='index'),
#    path('membro/',views.autentica_membro,name='membro'),
# ]