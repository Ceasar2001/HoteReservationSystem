from django.shortcuts import redirect

def manager_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.get('username') and request.session.get('type') == 'manager':
            return view_func(request, *args, **kwargs)
        else:
            return redirect('manager_login')  # Redirect to the manager login page if the user is not a manager

    return wrapper
