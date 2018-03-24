from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import render , get_object_or_404,redirect

from django.contrib import messages


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from .forms import PostForm
from .models import Post
def post_create(request):
	form=PostForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Successsfuly Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request,"Not Successsfuly Created")	

	context={
			"form": form,
	}
	
	return render(request,"post_form.html",context)
def post_detail(request,id=None):
	#instance = Post.objects.get(cd=id)
	instance= get_object_or_404( Post, id=id)
	context={
			"title": instance.title,
			"instance": instance
			
	 	}
	return render(request,"post_detail.html",context)
def post_list(request):
	# if request.user.is_authenticated():
	# 	context={
	# 		"title": "my list"
	# 	}
	# else:
	# 	context={
	# 		"title": "list"
	# 	}
	queryset_list=Post.objects.all()#.order_by("-timestamp")
	paginator = Paginator(queryset_list, 10) # Show 25 contacts per page
	page_request_var="page"
	page = request.GET.get('page_request_var')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		queryset = paginator.page(1)
	except EmptyPage:
		queryset = paginator.page(paginator.num_pages)

	context={
			"object_list": queryset,
			"title": "my list",
			"page_request_var": page_request_var
	 		}
	#return render(request,"base.html",context)
	return render(request,"post_list.html",context)



# def listing(request):
#     contact_list = Contacts.objects.all()
    
#     return render(request, 'list.html', {'contacts': contacts})


def post_update(request,id=None):
	instance= get_object_or_404( Post, id=id)
	form=PostForm(request.POST or None ,request.FILES or None, instance=instance)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"Successsfuly updated")
		return HttpResponseRedirect(instance.get_absolute_url())
	context={
			"title": instance.title,
			"instance": instance,
			"form": form
	 	}
	return render(request,"post_form.html",context)
# def post_delete(request):
# 	return HttpResponse("<h1>Hello</h1>")
def post_delete(request,id=None):
	instance= get_object_or_404( Post, id=id)
	instance.delete()
	messages.success(request,"Successsfuly deleted")
	return redirect("posts:list")

