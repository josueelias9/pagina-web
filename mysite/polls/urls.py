from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

    path('cover/', views.CoverPageView.as_view(), name='cover'),
    path('carousel/', views.CarouselPageView.as_view(), name='carousel'),
    path('album/', views.AlbumPageView.as_view(), name='album'),
    path('dashboard/', views.DashboardPageView.as_view(), name='dashboard'),
    path('checkout/', views.ProyectoCheckoutCreate.as_view(), name='checkout'),

    # path('proyecto/', views.ProyectoCreate.as_view(), name='proyectoCreate'),
]