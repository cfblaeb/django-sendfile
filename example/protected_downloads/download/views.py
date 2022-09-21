from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseForbidden
from django.db.models import Q
from sendfile.core import sendfile
from .models import Download


def download(request, download_id):
	download_obj = get_object_or_404(Download, pk=download_id)
	if download_obj.is_public:
		return sendfile(request, download_obj.file.path)
	return _auth_download(request, download_obj)


@login_required
def _auth_download(request, download_obj):
	if not download_obj.is_user_allowed(request.user):
		return HttpResponseForbidden('Sorry, you cannot access this file')
	return sendfile(request, download_obj.file.path)


def download_list(request):
	downloads = Download.objects.all()
	if request.user.is_authenticated:
		downloads = downloads.filter(Q(is_public=True) | Q(users=request.user))
	else:
		downloads = downloads.filter(is_public=True)
	return render(request, 'download/download_list.html', {'download_list': downloads})
