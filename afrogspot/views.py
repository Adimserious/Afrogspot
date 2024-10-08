from django.shortcuts import render
import logging

logger = logging.getLogger('django')


def four_o_four_view(request, exception=None):
    logger.error(f"404 error at {request.path}")
    return render(request, '404.html', status=404)
