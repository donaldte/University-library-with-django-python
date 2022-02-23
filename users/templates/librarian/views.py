
from pyexpat import model
from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic
# from bootstrap_model_forms.mixins import PassRequestMixin
from .models import User, Books, Ebooks, Chats, SendFeedback
from .form import UserForm, ProfileForm, EbookForm, BookForm, ChatForm
from django.contrib import messages, auth
from django.db.models import Sum
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView, ListView
from . import models
import operator
import itertools
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# general views


def login_forms(request):
    return render(request, 'users/login.html')


def logoutView(request):
    logout(request)
    return redirect('home')


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            if user.is_admin or user.is_superuser:
                return redirect('admin')
            elif user.is_librarian:
                return redirect('librarian')
            elif user.is_student:
                return redirect('student')
            elif user.is_publisher:
                return redirect('publisher')
            else:
                return redirect("notverified")
        else:
            messages.info(request, "Invalid password or username")
            return redirect('home')
    return redirect('home')

# register


def register(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, "Account was created successfully..")
            return redirect("home")

        else:
            messages.error(request, user_form.errors, profile_form.errors)
            register = False

    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    content = {
        'form1': user_form,
        'form2': profile_form,
    }
    return render(request, 'users/register.html', content)


# Student views
@login_required
def student(request):
    return render(request, 'student/home.html')


# Publisher

class ListeBooksView(LoginRequiredMixin, ListView):
    model = Ebooks
    paginate_by = 4
    context_object_name = 'ebooks'

    def get_queryset(self):
        return Ebooks.objects.order_by('-id')


class ListBooksView(LoginRequiredMixin, ListView):
    model = Books
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        return Books.objects.order_by('-id')

 # this function it's to add a new book


@login_required
def addEbook(request):
    if request.method == 'POST':
        form = EbookForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The book was added successfully.")
            return redirect('/publisher')
        else:
            form = EbookForm(data=request.POST)
    else:
        form = EbookForm()
    return render(request, 'publisher/add_ebook.html', {'form': form})

# this function is to add a new book


@login_required
def addBook(request):
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The book was added successfully.")
            return redirect('/publisher')
        else:
            form = BookForm(data=request.POST)
    else:
        form = BookForm()
    return render(request, 'publisher/add_book.html', {'form': form})


@login_required
def sendfeedback(request):
    if request.method == 'POST':
        feedback = request.POST['feedback']
        if feedback != '' and feedback is not None:
             current_user = request.user
             username = current_user.username
             feedback = username + " " + " says:  " + feedback
             a = SendFeedback(feedback=feedback)
             a.save()
             messages.success(request, 'Feedback was sent')
        else:
            messages.error(request, "You can't send empty message.")     
           
    return render(request, 'publisher/send_feedback.html')
#------------------------------------------------------------search------------------------------------
@login_required
def lsearch(request):
    query = request.GET['query']
    print(type(query))


    #data = query.split()
    data = query
    if( len(data) == 0):
        return redirect('publisher')
    else:
        a = data

                # Searching for It
        qs5 =models.Books.objects.filter(id__iexact=a).distinct()
        qs6 =models.Books.objects.filter(id__exact=a).distinct()

        qs7 =models.Books.objects.all().filter(id__contains=a)
        qs8 =models.Books.objects.select_related().filter(id__contains=a).distinct()
        qs9 =models.Books.objects.filter(id__startswith=a).distinct()
        qs10 =models.Books.objects.filter(id__endswith=a).distinct()
        qs11 =models.Books.objects.filter(id__istartswith=a).distinct()
        qs12 =models.Books.objects.all().filter(id__icontains=a)
        qs13 =models.Books.objects.filter(id__iendswith=a).distinct()


        files = itertools.chain(qs5, qs6, qs7, qs8, qs9, qs10, qs11, qs12, qs13)

        res = []
        for i in files:
            if i not in res:
                res.append(i)


                # word variable will be shown in html when user click on search button
        word="Searched Result :"
        
        files = res


        page = request.GET.get('page', 1)
        paginator = Paginator(files, 10)
        try:
            files = paginator.page(page)
        except PageNotAnInteger:
            files = paginator.page(1)
        except EmptyPage:
            files = paginator.page(paginator.num_pages)
   


        if files:
                return render(request,'publisher/result.html',{'files':files,'word':word})
        return render(request,'publisher/result.html',{'files':files,'word':word})

#-----------------------------------------------------------end search----------------------------
#     
             

# Librarian views
@login_required
def librarian(request):
    book = Books.objects.all().count()
    user = User.objects.all().count()
    ebook = Ebooks.objects.all().count()
    context = {
        'book':book,
        'user':user,
        'ebook':ebook,
    }
    return render(request, 'librarian/home.html', context)

@login_required
def laddEbook(request):
    if request.method == 'POST':
        form = EbookForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The book was added successfully.")
            return redirect('/lepublisher')
        else:
            form = EbookForm(data=request.POST)
    else:
        form = EbookForm()
    return render(request, 'librarian/add_ebook.html', {'form': form})

# this function is to add a new book


@login_required
def laddBook(request):
    if request.method == 'POST':
        form = BookForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "The book was added successfully.")
            return redirect('/lpublisher')
        else:
            form = BookForm(data=request.POST)
    else:
        form = BookForm()
    return render(request, 'librarian/add_book.html', {'form': form})

class ListFeedbackView(LoginRequiredMixin, ListView):
    model = SendFeedback
    context_object_name = 'feedbacks'
    paginate_by = 3

    def get_queryset(self):
        return SendFeedback.objects.order_by('-id')    

        
class LViewBook(LoginRequiredMixin,DetailView):
	model = Books
	template_name = 'librarian/book_detail.html'

	
class LEditView(LoginRequiredMixin,UpdateView):
	model = Books
	form_class = BookForm
	template_name = 'librarian/edit_book.html'
	success_url = reverse_lazy('lmbook')
	success_message = 'Data was updated successfully'


class LDeleteBook(LoginRequiredMixin,DeleteView):
	model = Books
	template_name = 'librarian/confirm_delete2.html'
	success_url = reverse_lazy('librarian')
	success_message = 'Data was deleted successfully'

class LeViewBook(LoginRequiredMixin,DetailView):
	model = Ebooks
	template_name = 'librarian/ebook_detail.html'

	
class LeEditView(LoginRequiredMixin,UpdateView):
	model = Ebooks
	form_class = EbookForm
	template_name = 'librarian/edit_ebook.html'
	success_url = reverse_lazy('lmbook')
	success_message = 'Data was updated successfully'



class LeDeleteBook(LoginRequiredMixin,DeleteView):
	model = Books
	template_name = 'librarian/confirme_delete2.html'
	success_url = reverse_lazy('librarian')
	success_message = 'Data was deleted successfully'





# Admin views
@login_required
def admin(request):
    return render(request, 'dashbord/home.html')


# NotVerified
@login_required
def notverified(request):
    return render(request, 'notverified/home.html')


# -------------------------------chat-------------------------------------

class ChatsCreateView(LoginRequiredMixin, CreateView):
    form_class = ChatForm
    model = Chats
    success_url = reverse_lazy('plchat')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()

        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.is_admin or self.request.user.is_superuser:
            return reverse_lazy('alchat')
        elif self.request.user.is_librarian:
             return reverse_lazy('llchat')
        elif self.request.user.is_publisher:
             return reverse_lazy('plchat')
        else:
            return reverse_lazy('slchat')      

class ChatsListView(LoginRequiredMixin, ListView):
    model = Chats

    def get_queryset(self):
        return Chats.objects.filter(posted_at__lt=timezone.now()).order_by('posted_at')      
    
#-------------------------------------------------------endchat------------------------------------------
    