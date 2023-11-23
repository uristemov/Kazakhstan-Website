from http.client import HTTPResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
from kazakhapp.models import City, Comment, Region
from .forms import AddUser, CommentCreate
# Create your views here.
def main(request):
          form = Comment.objects.all()
          return render(request, "Main.html", {'comment': form}) 
def sign_up(request):
          return render(request, "sign_up.html")

def data_loading(request):
          return render(request, "sign_up2.html")

def art(request):
          return render(request, "Art.html")

def trad(request):
          return render(request, "Tradition.html")
def sport(request):
          return render(request, "Sport.html")
def medicine(request):
          form = Region.objects.all()
          return render(request, "Medicine.html" ,{'form': form})

def explore(request):
          return render(request, "project-12.html")


#CRUD 
def upload(request):
          upload = CommentCreate()
          if request.method == "POST":
                    upload= CommentCreate(request.POST, request.FILES)
                    if upload.is_valid():
                              upload.save()
                              return redirect('main')
                    else:
                              return HTTPResponse("""ERROR""")
          else:
                    return render(request, "Comments.html", {'comment': upload})

def update(request, comment_id):
    comment_id = int(comment_id)
    try:
        sel = Comment.objects.get(id = comment_id)
    except Comment.DoesNotExist:
        return redirect('main')
    comment_form = CommentCreate(request.POST or None, instance = sel)
    if comment_form.is_valid():
       comment_form.save()
       return redirect('main')
    return render(request, 'Comments.html', {'comment':comment_form})

def delete(request, comment_id):
    comment_id = int(comment_id)
    try:
        sel = Comment.objects.get(id = comment_id)
    except Comment.DoesNotExist:
        return redirect('main')
    sel.delete()
    return redirect('main')


def show_post (request, post_slug):
          post = get_object_or_404(City, slug=post_slug)
          context = {'post' : post}
          return render(request, 'post.html', context=context)

def adduser(request):
        if request.method == 'POST':
            form = AddUser(request.POST)
            if form.is_valid():
                # print(form.cleaned_data)
                form.save()
                email = form.cleaned_data.get("email")
                send_mail("A cool subject", "A stunning message", "200103034@stu.sdu.edu.kz", [email], fail_silently=False)

                return redirect('main')
        else:
            form = AddUser()
        
        return render(request, 'sign_up.html' , {'form': form})

def index(request):
    return render(request, "index.html")