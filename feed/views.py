from django.views.generic import TemplateView, DetailView, FormView
from .models import Post
from .forms import PostForm
from django.contrib import messages

class HomePageView(TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context

class PostListView(TemplateView):
    template_name = "posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    
class PostDetailView(DetailView):
    template_name = "detail.html"
    model = Post
    
class AddPostView(FormView):
    template_name = "new_post.html"
    form_class = PostForm
    success_url = "/posts"
    
    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        new_object = Post.objects.create(
            title=form.cleaned_data['title'],
            description=form.cleaned_data['description'],
            image=form.cleaned_data['image']
        )
        messages.add_message(self.request, messages.SUCCESS, 'Your post was successful')
        # print(form.cleaned_data['text'])
        # print(form.cleaned_data['image'])
        # print("this was valid!")
        return super().form_valid(form)
    