from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.contrib import messages
from .models import Comment
from django.db.models import Q 
from .forms import PostForm,CommentForm
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.mail import send_mail
from .forms import CaptchaForm
from django.views.generic.detail import SingleObjectMixin
from .forms import ContactForm
class home_page(ListView):
    model=Post
    template_name="home.html"
    paginate_by = 2 
    context_object_name = 'context'
    ordering=["-date"]
    def get_queryset(self): # new
        query=self.request.GET.get("q")
        if not query:
            query=""
        return Post.objects.filter(
        Q(title__icontains=query) 
        )
        

# def home_page(request):
#     objects=Post.objects.all()
#     return render(request,"home.html",{"context":objects})

def about_page(request):
    return render(request,"about.html",{})

class CreatePage(LoginRequiredMixin,CreateView):
    model=Post
    fields = ("title","content","image")
    success_url="/"
    template_name="create.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  
# class detail_page(DetailView):
#     model=Post
#     context_object_name="object"
class delete_page(LoginRequiredMixin, DeleteView):
    model=Post
    success_url="/"
    context_object_name="object"
    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.author == self.request.user:
            raise PermissionError
        return obj
    
class update_page(LoginRequiredMixin,UpdateView):
    model=Post
    success_url="/"
    fields='__all__'
    context_object_name="object"
    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.author == self.request.user:
            raise PermissionError
        return obj

# def create_page(request):
#     form=PostForm()
#     if request.method=='POST':
#         form=PostForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Post created.')
#             return redirect("home_page")
#     else:
#         form=PostForm()
#     return render(request,"create.html",{"form":form})


def detail_page(request,id):
    obj=get_object_or_404(Post ,id=id)
    comm=CommentForm()
    # here will be filtger
    all_comm=Comment.objects.filter(post__pk=id)
    if request.method=="POST":
        form=CommentForm(request.POST or None)
        if form.is_valid():
            comment_obj = form.save(commit=False)
            comment_obj.post = obj
            comment_obj.save()
    return render(request,"detail.html",{"object":obj,"comment":comm,"all_comments":all_comm})
# def delete_page(request,id):
#     obj=get_object_or_404(Post ,id=id)
#     obj.delete()
#     return redirect("/")
#     return render(request,"delete.html",{"object":obj})


# def update_page(request,id):
#     obj=get_object_or_404(Post ,id=id)
#     form=PostForm(request.POST or None,instance=obj)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Post Updated.')
#         return redirect("home_page")
#     return render(request,"update.html",{"form":form})

def contact_page(request):
    form=ContactForm()

    if request.method=="POST":
        print("ok ")
        form=ContactForm(request.POST or None)
        if form.is_valid():
            from_email=form.cleaned_data['from_email']
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['elvinc402@gmail.com',])
                print("sucess")

                messages.success(request, 'Mail sent.')
                return redirect("home_page")
            except Exception as e:
                return e
            return redirect('success')

    return render(request,"contact.html",{"form":form,"captch":CaptchaForm()})



