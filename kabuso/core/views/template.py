from functools import wraps

from django.template.response import TemplateResponse


def template_view(template_name):
    """ View decorator to convert returned dictionary into TemplateResponse
    You can apply template name for this decorator like this

    >>> @template_view
    >>> def page_detail(request):
    >>>     return {'page_title': 'Some Page Title'}  # This will automatically used as context.

    If you return some object excluding dictionary, `template_view` will return it directly.
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(request, *args, **kwargs):
            response = view_func(request, *args, **kwargs)
            if isinstance(response, dict):
                return TemplateResponse(request, template_name, context=response)
            else:
                return response
        return wrapped
    return decorator
