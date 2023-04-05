
from django.urls import path

from .views import addphoto,addcomment,likepost,postview,filter,search,contact,postview,postcreate, subview, ContactView,PostCreateView,PostListView,PostDetailView,PostEditView,PostDeleteView,commentdelete,apply
from .forms import ContactFormTwo
from .pdf import contact_pdf
app_name = 'tuition'


urlpatterns = [
    #path('contact/',contact, name="contact"),
    path('search/',search, name="search"),
    path('filter/',filter, name="filter"),
    path('pdf/',contact_pdf, name="pdf"),
    path('likepost/<int:id>/',likepost, name="likepost"),
    path('addphoto/<int:id>/',addphoto, name="addphoto"),
    path('commentdelete/<int:id>/',commentdelete, name="commentdelete"),
    path('addcomment/',addcomment, name="addcomment"),
    path('postview/',postview, name="postview"),
    path('contact/', ContactView.as_view(), name="contact"),
    #path('contact2/', ContactView.as_view(form_class= ContactFormTwo, template_name="contact2.html"), name="contact2"),
    path('posts/',postview,name="posts"),
    path('postlist/',PostListView.as_view(),name="postlist"),
    path('postdetail/<int:pk>/',PostDetailView.as_view(),name="postdetail"),
    path('edit/<int:pk>/',PostEditView.as_view(),name="edit"),
    path('apply/<int:id>/',apply,name="apply"),
    path('delete/<int:pk>/',PostDeleteView.as_view(),name="delete"),
    path('create/', postcreate, name="create"),
    #path('create/', PostCreateView.as_view(), name="create"),
    path('subjects/', subview, name="subjects"),
    
   
]