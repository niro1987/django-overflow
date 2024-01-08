"""
context_processors.py

This file contains context processors for adding common context data 
to templates.
"""
from base import const


def template_variables(request):
    """
    Template Variables

    Adds common variables to all templates.
    """
    app_name = request.resolver_match.app_name
    v = {
        "project_name": const.PROJECT_NAME,
        "page_title": const.PROJECT_NAME + " - " + app_name.title(),
    }
    return v
