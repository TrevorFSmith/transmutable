import datetime
import traceback

from django.contrib import auth
from django.conf import settings
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, Http404, HttpResponseServerError, HttpResponseRedirect, HttpResponsePermanentRedirect

from api_forms import SearchForm

@login_required
def search(request):
	if request.method == 'POST':
		search_form = SearchForm(request.POST)
		if search_form.is_valid():
			results = search_form.search(request.user)
		else:
			results = None
	else:
		search_form = SearchForm()
		results = None
	return render_to_response('backbone/search.html', {'results':results, 'search_form':search_form }, context_instance=RequestContext(request))

# Copyright 2012 Trevor F. Smith (http://trevor.smith.name/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
