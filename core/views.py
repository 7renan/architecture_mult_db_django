from django.shortcuts import render
from django.shortcuts import redirect


def api_redirect(request):
    return redirect('/api')


