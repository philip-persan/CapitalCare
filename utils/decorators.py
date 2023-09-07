from django.shortcuts import redirect


def not_authenticated(view):
    def check(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:index')
        else:
            return view(request, *args, **kwargs)

    return check


def is_staff(view):
    def check(request, *args, **kwargs):
        if request.user.is_staff:
            return view(request, *args, **kwargs)
        else:
            return redirect('home:index')

    return check


def is_superuser(view):
    def check(request, *args, **kwargs):
        if request.user.is_superuser:
            return view(request, *args, **kwargs)
        else:
            return redirect('home:index')

    return check
