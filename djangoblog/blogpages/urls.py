from django.conf import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('team', views.team, name='team'),
    path('partner_with_us', views.partner_with_us, name='partner_with_us'),
    path('volunteer_with_us', views.volunteer_with_us, name='volunteer_with_us'),
    path('workshops', views.workshops, name='workshops'),
    path('STEM_tours', views.STEM_tours, name='STEM_tours'),
    path('STEM_role_models', views.STEM_role_models, name='STEM_role_models'),
    path('STEM_awareness', views.STEM_awareness, name='STEM_awareness'),
    path('STEM_sponsorship', views.STEM_sponsorship, name='STEM_sponsorship'),
    path('news', views.PostList.as_view(), name='news'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)