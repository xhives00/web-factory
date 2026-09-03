from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.views.generic import TemplateView

from . import views

admin.site.site_header = "Vladimír Strunga — správa webu"
admin.site.site_title = "Správa strunga.eu"
admin.site.index_title = "Galéria a obsah"

urlpatterns = [
    # language-switcher POST target; must stay outside i18n_patterns and
    # unprefixed so it's reachable no matter which language the page is in.
    # See views.set_site_language for why this isn't Django's built-in view.
    path("i18n/setlang/", views.set_site_language, name="set_language"),
    path("admin/", admin.site.urls),
]

urlpatterns += i18n_patterns(
    path("", views.home, name="home"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about"),
    path("projects/", include("shared.apps.portfolio.urls")),
    path("gallery/", include("shared.apps.gallery.urls")),
    path("programy/", include("shared.apps.programy.urls")),
    # Czech is the default language and keeps unprefixed URLs, so the
    # calculator stays reachable at exactly /programy/pb-time/ as before
    # (that URL is cited in published papers) — only /en/... and /fr/...
    # get a language prefix.
    prefix_default_language=False,
)

# Small personal site with no separate media/CDN host — serve uploaded
# gallery photos directly through Django, in dev and in production alike.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
