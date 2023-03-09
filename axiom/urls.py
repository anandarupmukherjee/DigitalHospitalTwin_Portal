from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("link_a/", views.link_a, name="link_a"),
    path("link_b/", views.link_b, name="link_b"),
    path("link_c/", views.link_c, name="link_c"),
    path("link_d/", views.link_d, name="link_d"),
    path("link_e/", views.link_e, name="link_e"),
    # path("<int:pk>/", views.project_detail, name="project_detail"),
    # path("home/", views.home, name="home"),
    # path("createpost/", views.createpost, name="createpost"),
    # path('analysis/', views.analysis, name='analysis'),
    # path('analysis1/', views.analysis1, name='analysis1'),
    # path('analysis2/', views.analysis2, name='analysis2'),
    # path('export/', views.csv_database_write, name='csv_database_write'),
    # path('summary/', views.summary, name='summary'),
#    path("insights/", views.insights, name="insights")

]
