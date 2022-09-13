from buku.models import Book
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from .forms import CreateUserForm
from django.views.generic.edit import CreateView
from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator
from braces.views import LoginRequiredMixin, SuperuserRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


# class BookListView(ListView):
#     model = Book
#     ordering = ['-published']
#     # paginate_by = 5
#     template_name = 'book/index.html'


# class SearchResultsView(ListView):
#     model = Book
#     template_name = "book/search_results.html"

#     def get_queryset(self):  # new
#         query = self.request.GET.get("q")
#         object_list = Book.objects.filter(
#             Q(title__icontains=query) | Q(description__icontains=query)
#         )
#         return object_list

def index(request):

    book_list = Book.objects.all().order_by('-id')
    query = request.GET.get('q')

    if query:
        book_list = book_list.filter(Q(title__icontains=query) |
                                     Q(description__icontains=query))

    paginator = Paginator(book_list, 3)
    page = request.GET.get('page')
    book_list = paginator.get_page(page)

    context = {
        'books': book_list
    }
    return render(request, 'book/index.html', context)


class SignUpView(SuccessMessageMixin, generic.CreateView):
    form_class = CreateUserForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    success_message = "User has been created, please login with your username and password"


class DetailBook(generic.DetailView):
    model = Book
    template_name = 'book/detailbook.html'


class BookCreateView(LoginRequiredMixin, SuperuserRequiredMixin, CreateView):
    model = Book
    template_name = 'book/add_book.html'
    fields = ['title', 'admin', 'published', 'author_name',
              'description', 'image', 'category']
    # success_url = reverse_lazy('index')


class UpdateBuku(LoginRequiredMixin, SuperuserRequiredMixin, generic.UpdateView):
    model = Book
    template_name = 'book/updatebuku.html'
    fields = ['title', 'category', 'description', 'author_name', 'image']
    success_url = reverse_lazy('index')


class DeleteBook(LoginRequiredMixin, SuperuserRequiredMixin, generic.DeleteView):
    model = Book
    template_name = 'book/deletebook.html'
    success_url = reverse_lazy('index')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("password_success")
    
    
def password_success(request):
    return render(request, 'registration/password_success.html', {})