# from django.http import Http404
# from django.shortcuts import render, get_object_or_404, redirect
# from django.urls import reverse
#
# from .models import Category, Post
#
# from .forms import AddPostForm, EditPostForm
#
#
# # получение всех объектов модели:Class.objects.al()
# # SELECT * FROM model
# # получение объектов по условию Class.objects.filter(условие)
# # SELECT *FROM model WHERE условие
# # исключение объектов из результата по условию Model.objects.exclude(условие)
# # .filter(age>30) -> select*from employee where age>35;
# # .exclusive(age >35) ->select*from employee where not age >35
# # получение объектов по услоыию или айди : Model.objects.get(учловие)
# # SELECT *FROM model WHERE условие/
# # получение первого объекта из списка: Model.objects.first() ili model..objects.filter)_first()
# # SELECT * FROM model [WHERE...] [ORDER BY...] LIMIT 1;
# # Получение последнего оъекта из списка  Model.objects.last()
# # создание объектов Model.objects.create
# # INSERT INTO model( поля) VALUES();
# # обновление объектов  Model.objects.update()
# # удаление объектов Model.objects.delete()
# # получение количества объектов в запросе : model.objects.count() или model.objects.filter().count()
# # select count from model where///;
#
# def index_page(request):
#     categories_list = Category.objects.all()
#     return  render(request, 'blog/index.html', {'categories': categories_list})
#
# # # categories/slug/
# # def category_details(request, slug):
# #     category = Category.objects.get(slug=slug)
# #     # post = Post.objects.filter(category=category)
# #     posts= category.posts.all()
# #     return render(request, 'blog/category_details.html',{'category':category,'posts':posts})
#
# # posts/?category='slug'
# def posts_list(request):
#     category_slug=request.GET.get('category')
#     posts = Post.objects.all()
#     if category_slug is not None:
#         posts = posts.filter(category_id=category_slug)
#     return  render(request,'blog/post_list.html',{'posts':posts})
#
# def post_details(request, pk):
#     # try:
#     #     post = Post.objects.get(id=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404
#     post = get_object_or_404(Post, pk=pk)
#     return render (request, 'blog/post_details.html', {'post':post})
# # CRUD(CREATE, RETRIEVE, UPDATE, DELETE)
# # GET(list, details), POST (create, update, delete)
# # GET(list, details), POST(create), PUT/PATCH(update), DELETE(delete)
#
# #TODO: Вьюшка для создания поста
# def add_post(request):
#     if request.POST:
#         post_form = AddPostForm(request.POST, request.FILES)
#         if post_form.is_valid():
#             post = post_form.save()
#             return redirect(post.get_absolute_url())
#     else:
#         post_form = AddPostForm()
#     return render(request, 'blog/add_post.html', {'post_form': post_form})
#
#
# def edit_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     post_form = EditPostForm(request.POST or None, request.FILES or None, instance=post)
#     if post_form.is_valid():
#         post_form.save()
#         return redirect(post.get_absolute_url())
#     return render(request, 'blog/edit_post.html', {'post_form': post_form, 'post': post})
# #TODO: Вьюшка для удаления поста.
#
# def delete_post(request,pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.POST:
#         post.delete()
#         return redirect(reverse('index-page'))
#     return render(request, 'blog/delete_post.html', {})
# # Function-Based Views (FBV)
# # Class-Based Views (CBV)
