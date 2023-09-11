from django.views import generic
from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'news.html'
    paginate_by = 3

# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def team(request):
    return render(request, 'team.html')

def partner_with_us(request):
    return render(request, 'partner_with_us.html')


def volunteer_with_us(request):
    return render(request, 'volunteer_with_us.html')

def workshops(request):
    return render(request, 'workshops.html')

def STEM_tours(request):
    return render(request, 'STEM_tours.html')

def STEM_role_models(request):
    return render(request, 'STEM_role_models.html')

def STEM_awareness(request):
    return render(request, 'STEM_awareness.html')

def STEM_sponsorship(request):
    return render(request, 'STEM_sponsorship.html')

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})