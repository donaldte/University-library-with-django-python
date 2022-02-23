from django.urls import path
from . import views

urlpatterns = [
    #GENERAL URL'S
    path('', views.login_forms, name='home'),
    path('register', views.register, name='regform'),
    path('dashboard', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),



    #Librarian URL's
    path('librarian/', views.librarian, name="librarian"),
    
    path("lchat/", views.ChatsCreateView.as_view(template_name='librarian/chat_form.html'),  name="lchat"),
    path("llchat/", views.ChatsListView.as_view(template_name='librarian/chat_list.html'),  name="llchat"),
    path("lepublisher/", views.ListeBooksView.as_view(template_name='librarian/home1.html'), name="lepublisher"),
    path("lpublisher/", views.ListBooksView.as_view(template_name='librarian/home2.html'),  name="lpublisher"),
    path("listfeedback/", views.ListFeedbackView.as_view(template_name='librarian/feedback.html'),  name="listfeedback"),
    path('lmbook/', views.LManageBook.as_view(), name='lmbook'),
    path('lmebook/', views.LeManageBook.as_view(), name='lmebook'),
    path("ldelete/<int:pk>", views.LDeleteBook.as_view(),  name="ldelete"),
    path("ledelete/<int:pk>", views.LeDeleteBook.as_view(),  name="ledelete"),
    path("ledit/<int:pk>", views.LEditView.as_view(),  name="ledit"),
    path("leedit/<int:pk>", views.LeEditView.as_view(),  name="leedit"),
    path("lview/<int:pk>", views.LViewBook.as_view(),  name="lview"),
    path("leview/<int:pk>", views.LeViewBook.as_view(),  name="leview"),
    path("laddnewebook/", views.laddEbook, name="laddebook"),
    path("laddnewbook/", views.laddBook, name="laddbook"),

     #----------------------------command-----------------------------------------
    path("listcommand/", views.ListCommandView.as_view(),  name="listcommand"),
    path("listborrow/", views.ListBorrowView.as_view(),  name="listborrow"),
    path("command_edit/<int:pk>/", views.CommandEditView.as_view(),  name="command_edit"),
    path("command_delete/<int:pk>/", views.CommandDeleteView.as_view(),  name="command_delete"),







    #Publisher URL's 
    path("epublisher/", views.ListeBooksView.as_view(template_name='publisher/home.html'), name="epublisher"),
    path("publisher/", views.ListBooksView.as_view(template_name='publisher/home1.html'),  name="publisher"),
    path("pchat/", views.ChatsCreateView.as_view(template_name='publisher/chat_form.html'),  name="pchat"),
    path("plchat/", views.ChatsListView.as_view(template_name='publisher/chat_list.html'),  name="plchat"),
    path('psend_feedback', views.sendfeedback, name='send_feedback'),
    path('lsearch', views.lsearch, name='lsearch'),
    path("addnewebook/", views.addEbook, name="addebook"),
    path("addnewbook/", views.addBook, name="addbook"),



    #Student URL's
    path('student/', views.student, name="student"),
    path("studentbook/", views.ListBooksView.as_view(template_name='student/home1.html'),  name="studentbook"),
    path('setting/<int:pk>/', views.update, name='setting'),
    path("studentebook/", views.ListeBooksView.as_view(template_name='student/home2.html'),  name="studentebook"),
    path("schat/", views.ChatsCreateView.as_view(template_name='student/chat_form.html'),  name="schat"),
    path("slchat/", views.ChatsListView.as_view(template_name='student/chat_list.html'),  name="slchat"),
    path("bookdetail/<int:pk>", views.LViewBook.as_view(template_name="student/book_detail.html"), name='bookdetail'),
    path('confirmborrow', views.confirmBorrow, name="confirmborrow"),
    path('studentcard', views.studentcard, name='studentcard' ),
  
    




    #Not verified URL
    path('notverified/', views.notverified, name="notverified"),



    #Admin URL
    path('dashboard/', views.admin, name="admin"),
    path("achat/", views.ChatsCreateView.as_view(template_name='dashbord/chat_form.html'),  name="achat"),
    path("alchat/", views.ChatsListView.as_view(template_name='dashbord/chat_list.html'),  name="alchat"),
    path("listuser/", views.ListUserView.as_view(),  name="listuser"),
    path("user_detail/<int:pk>/", views.UserDetailView.as_view(),  name="user_detail"),
    path("user_edit/<int:pk>/", views.UserEditView.as_view(),  name="user_edit"),
    path("user_delete/<int:pk>/", views.UserDeleteView.as_view(),  name="user_delete"),
    path("create_user_form/", views.create_user_form, name="create_user_form"),
    path("create_user/", views.create_user, name="create_user"),

]   