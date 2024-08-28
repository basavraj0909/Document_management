from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from documents_app.views import home, CustomLoginView, SignupView
# signup

urlpatterns = [
                  path("admin/", admin.site.urls),
                  path('', home, name='home'),  # Root URL pattern

                  path("documents/", include('documents_app.urls')),
                  path('signup/', SignupView.as_view(), name='signup'),  # Custom signup view
                  path('login/', CustomLoginView.as_view(), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(), name='logout'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
