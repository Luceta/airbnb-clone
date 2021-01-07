"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
]

# 아마존에 업로드 할때는 다른 방식을 사용 (개발자 모드에서 아래와 같이 사용)
if settings.DEBUG:  # debug모드 체크한 후 내 폴더안의 파일들을 제공 -> 나중에는 debug아니라면, amazon 파일 제공으로 바꿈
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
