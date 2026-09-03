from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.translation import check_for_language

from shared.apps.gallery.models import GalleryImage


def home(request):
    """Homepage: the curated field photos in the template are fixed, plus any
    photos added later through /admin (Gallery events → images) are appended
    automatically so new finds show up without touching the template."""
    extra_images = (
        GalleryImage.objects.select_related("event").order_by("-created_at")
    )
    return render(request, "home.html", {"extra_images": extra_images})


def set_site_language(request):
    """Language switcher target.

    We can't use Django's built-in `django.views.i18n.set_language` here:
    it redirects via `translate_url()`, which internally calls `resolve()`
    using the CURRENTLY ACTIVE language rather than the prefix in `next`.
    Because this site uses `prefix_default_language=False` (needed to keep
    the calculator at the exact unprefixed /programy/pb-time/ URL that's
    cited in publications), `LocaleMiddleware` forces every unprefixed path
    — including this endpoint itself — to the default language, so
    `translate_url()` silently fails to resolve any `next` that carries a
    non-default prefix and redirects back to the same page. Instead we just
    strip/add the two-letter prefix ourselves.
    """
    known_codes = {code for code, _ in settings.LANGUAGES}
    lang_code = request.POST.get("language")
    next_path = request.POST.get("next") or "/"

    if not (lang_code in known_codes and check_for_language(lang_code)):
        return HttpResponseRedirect(next_path)

    segments = [s for s in next_path.split("/") if s]
    if segments and segments[0] in known_codes:
        segments = segments[1:]

    if lang_code == settings.LANGUAGE_CODE:
        target = "/" + "/".join(segments)
    else:
        target = "/" + lang_code + "/" + "/".join(segments)
    if not target.endswith("/"):
        target += "/"

    response = HttpResponseRedirect(target)
    response.set_cookie(
        settings.LANGUAGE_COOKIE_NAME,
        lang_code,
        max_age=settings.LANGUAGE_COOKIE_AGE,
        path=settings.LANGUAGE_COOKIE_PATH,
        domain=settings.LANGUAGE_COOKIE_DOMAIN,
        secure=settings.LANGUAGE_COOKIE_SECURE,
        httponly=settings.LANGUAGE_COOKIE_HTTPONLY,
        samesite=settings.LANGUAGE_COOKIE_SAMESITE,
    )
    return response
