from django.http import HttpResponse


def sendfile(request, filename, **kwargs):
    # just a simple response with the filename
    # as content - so we can test without a backend active
    return HttpResponse(filename)
