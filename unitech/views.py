# coding=utf-8

"""
unitech app views
"""

from django.shortcuts import render


def home(request):
    """Home view

    Args:
        request: HTTP request

    Returns:
        Home page render
    """
    return render(request, 'unitech/index.html', {})
