from django.shortcuts import render


def page_not_found(request, exception):
    """error 404"""
    return render(
        request,
        "misc/404.html",
        {"path": request.path},
        status=404
    )


def server_error(request):
    """error 500"""
    return render(request, "misc/500.html", status=500)
