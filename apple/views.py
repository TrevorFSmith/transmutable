import datetime
import calendar
import pprint
import traceback
import urllib
import simplejson as json

from django.utils.html import urlize
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db.models import Q
from django.template import Context, loader
from django.http import HttpResponse, Http404, HttpResponseServerError, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.comments.models import Comment
from django.contrib.sites.models import Site
from django.utils.html import strip_tags
import django.contrib.contenttypes.models as content_type_models
from django.template import RequestContext
from django.core.cache import cache
from django.core.mail import send_mail
from django.contrib.admin.views.decorators import staff_member_required
from django.template.loader import render_to_string
from django.utils import feedgenerator
from django.utils.encoding import smart_str
from django.core.mail import send_mail

from forms import CreateAccountForm, SendTestEmailForm

@staff_member_required
def index(request): return render_to_response('apple/index.html', { }, context_instance=RequestContext(request))

@staff_member_required
def send_test(request):
	page_message = None
	if request.method == 'POST':
		send_test_email_form = SendTestEmailForm(request.POST)
		if send_test_email_form.is_valid():
			email = send_test_email_form.cleaned_data['email']
			message = render_to_string('apple/email/test_email.txt', { 'admin_name':settings.ADMINS[0][0] }, context_instance=RequestContext(request))
			send_mail('A Test Email', message, settings.DEFAULT_FROM_EMAIL, [email], fail_silently=False)
			page_message = 'Sent the email to %s' % email
	else:
		send_test_email_form = SendTestEmailForm()
	return render_to_response('apple/send_test.html', { 'page_message':page_message, 'send_test_email_form':send_test_email_form }, context_instance=RequestContext(request))

@staff_member_required
def create_account(request):
	if request.method == 'POST':
		create_account_form = CreateAccountForm(request.POST)
		if create_account_form.is_valid():
			user, password = create_account_form.save()
			message = render_to_string('apple/email/account_created.txt', { 'user':user, 'password':password, 'admin_name':settings.ADMINS[0][0] }, context_instance=RequestContext(request))
			if settings.PRODUCTION == True:
				user.email_user("Account Created", message, settings.DEFAULT_FROM_EMAIL)
			else:
				print message

			return HttpResponseRedirect(user.get_absolute_url())
	else:
		create_account_form = CreateAccountForm()
	return render_to_response('apple/create_account.html', { 'create_account_form':create_account_form }, context_instance=RequestContext(request))

# Copyright 2011 Trevor F. Smith (http://trevor.smith.name/) Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0 Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.