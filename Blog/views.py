#--*-- coding:utf-8 --*--
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.http import Http404
from Blog.models import *
from django.db.models import Count
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.mail import send_mail
from Blog.form import *
#from django.db import connection
# Create your views here.

#def index(request):
#    return render(request,"Article_Post.html")

def home(request):
    category_list = Category.objects.all()
    article_list = Article.objects.all()
    paginator = Paginator(article_list, 4)
    archive_list = Article.objects.distinct_date()
    return render(request,"home.html", locals())

def detail(request,id):
    try:
        category_list = Category.objects.all()
        article = Article.objects.get(id=str(id))
        archive_list = Article.objects.distinct_date()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'single_post.html', locals())

def about(request):
    archive_list = Article.objects.distinct_date()
    category_list = Category.objects.all()
    return render(request,'about.html', locals())

def archive(request):
    year = request.GET.get('year', None)
    month = request.GET.get('month', None)
    article_list = Article.objects.filter(publish_date__icontains=year+'-'+month)
    archive_list = Article.objects.distinct_date()
    category_list = Category.objects.all()
    return render(request,'archive.html', locals())
"""
def search_tag(request,tag):
    try:
        category_list = Article.objects.filter(category__iexact = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'category.html',locals())

"""

def category(request,id):
    category_list = Category.objects.all()
    archive_list = Article.objects.distinct_date()
    article_list = Article.objects.filter(category__id = id)
    return render(request,'category.html',locals())

"""
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = cd['subject']
            e_mail = cd['e_mail']
            message = cd['message']
    else:
        form = ContactForm()
        inital = {'subject':'hello world'}
        return render_to_response('login.html',{'form': form})
"""

def contact(request):
#	title='This is mail title.'
#	testmessage='Hello, This is a message'
#	testsender='123456789@qq.com'
#	testmail_list=['recv@163.com',]
#	send_mail(
#                subject=title,
#                message=testmessage,
#                from_email=testsender,
#                recipient_list=testmail_list,
#                fail_silently=False,
#                connection=None
#            )
	errors=[]
	if request.method == 'POST':
		if not request.POST.get('subject',''):
			errors.append('Enter a subject.')
		if not request.POST.get('message',''):
			errors.append('Enter a message.')
		if request.POST.get('email') and '@' not in request.POST['email']:
			errors.append('Enter a valid e-mail address.')
		if not errors:
			send_mail(
				request.POST['subject'],
				request.POST['message'],
				request.POST.get('email','0daybug@sina.com'),
				['bluespeedsky@sina.com'],
			)
			return HttpResponseRedirect('/contact/thanks/')

	return render_to_response('login.html',
		{'errors':errors,
		'subject': request.POST.get('subject',''),
		'message': request.POST.get('message',''),
		'email': request.POST.get('email',''),
		}, context_instance=RequestContext(request))

def thanks(request):
	return HttpResponse("Great Thanks!")