from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),               # for homepage, about, etc.
    path('account/', include('account.urls')),    # for login/signup
    path('projects/', include('project.urls')),   # for projects
    path('projects/<uuid:project_id>/', include('todolist.urls')),  # todolist
    path('projects/<uuid:project_id>/<uuid:todolist_id>/', include('ta_sk.urls')),  # tasks
]

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
