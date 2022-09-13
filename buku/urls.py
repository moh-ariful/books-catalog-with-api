from django.urls import path, include
from .views import BookCreateView, index, SignUpView, PasswordsChangeView, password_success
from buku import views
from django.contrib.auth.decorators import login_required



urlpatterns = [
    path('', index, name='index'),
    path("accounts/", include("django.contrib.auth.urls")),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('add/', login_required(BookCreateView.as_view()), name='add_book'),
    path('detail/<int:pk>', views.DetailBook.as_view(), name='detailbook'),
    path('detail/<int:pk>/update', views.UpdateBuku.as_view(), name='updatebuku'),
    path('detail/<int:pk>/delete', views.DeleteBook.as_view(), name='deletebook'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html'), name='password-change')
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html'), name='password-change'),
    path('password_success', password_success, name='password_success'),

]
