from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post,Comment
from .forms import PostForm, CommentForm
from django.core.paginator import Paginator
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy 


class post_list(ListView):
    model = Post
    queryset = Post.objects.order_by('-published_date') # Default: Model.objects.all()
    context_object_name = 'posts' # Default: object_list
    template_name = 'post_list.html' # Default: <app_label>/<model_name>_list.html
    paginate_by = 4

class post_detail(DetailView):
    model = Post
    context_object_name = 'post'
    queryset = Post.objects.all()
    template_name = 'post_detail.html'
    
    

class post_new(CreateView):
    model = Post
    fields = ('author', 'title', 'text', 'source', 'source_command')
    #post.image_title = 
    template_name = 'post_edit.html'


# paginator model for Function-Based-Views

#from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#def PostList(request):
#    object_list = Post.objects.filter(status=1).order_by('-created_on')
#    paginator = Paginator(object_list, 3)  # 3 posts in each page
#    page = request.GET.get('page')
#    try:
#        post_list = paginator.page(page)
#    except PageNotAnInteger:
#            # If page is not an integer deliver the first page
#        post_list = paginator.page(1)
#    except EmptyPage:
#        # If page is out of range deliver last page of results
#        post_list = paginator.page(paginator.num_pages)
#    return render(request,
#                  'index.html',
#                  {'page': page,
#                   'post_list': post_list})





def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comment_new.html', {'form': form})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})




