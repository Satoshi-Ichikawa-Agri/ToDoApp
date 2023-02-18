from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView ,UpdateView, DeleteView, DetailView

from TodoApp.models import Todo
from TodoApp.forms import TodoForm


class TopPageView(TemplateView):
    """
    """
    template_name = 'pages/home.html'


class TodoIndexView(ListView):
    """ TodoテーブルからアイテムListを取得する
    指定が無ければ全データを取得し、「object_list」に格納する。
    """
    model = Todo
    template_name = 'pages/index.html'


class TodoCreateView(CreateView):
    """
    """
    model = Todo
    form_class = TodoForm # 入力フォームの指定
    success_url = '/index/' # 登録後の遷移先
    template_name = 'pages/create.html'

    def form_valid(self, form):
        """ フォームが有効だった場合の処理
        """
        return super().form_valid(form)


class TodoEditView(UpdateView):
    """
    """
    model = Todo
    template_name = 'pages/edit.html'
    fields = ('summary', 'detail', 'limit')
    success_url = '/index/'


class TodoDeleteView(DeleteView):
    """
    """
    model = Todo
    template_name = 'pages/delete.html'
    success_url = '/index/'


class TodoDetailView(DetailView):
    """
    """
    model = Todo
    template_name = 'pages/details.html'
