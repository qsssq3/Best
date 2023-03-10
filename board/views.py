from django.shortcuts import render, redirect, get_object_or_404
import os
from config import settings
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from board.models import Base
from board.forms import BaseCreateForm, BaseUpdateForm
# Create your views here.

class List(ListView):
  model = Base
  template_name = 'base/list.html'
  ordering = '-pk'
  paginate_by = 10

class Create(CreateView):
  model = Base
  form_class = BaseCreateForm
  template_name = 'base/create.html'
  
  def form_valid(self, form):
    current_user = self.request.user
    if current_user.is_authenticated:
      form.instance.author = current_user
      return super().form_valid(form)
    else:
      return redirect('/base')

class Detail(DetailView):
  model = Base
  template_name = 'base/detail.html'
  def dispatch(self, request, *args, **kwargs):
    if request.user.is_authenticated:
      return super().dispatch(request, *args, **kwargs)
    else:
      raise PermissionDenied

class Update(UpdateView):
    model = Base
    form_class = BaseUpdateForm
    template_name = 'base/update.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def form_valid(self, form):
      if self.get_object().file_upload.name != '':
        if self.object.file_upload != self.get_object().file_upload.name:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
        if 'upload_clear' in self.request.POST:
          file_upload_path=os.path.join(settings.MEDIA_ROOT, self.get_object().file_upload.path)
          if os.path.exists(file_upload_path):
              os.remove(file_upload_path)
              self.object.file_upload = ''
      return super().form_valid(form)


@login_required(login_url='app:login')
def Delete(request, pk):
  base = get_object_or_404(Base, pk=pk)
  if request.user != base.author:
    return redirect('base:detail', pk=pk)
  if base.file_upload:
    file_upload_path = os.path.join(settings.MEDIA_ROOT, base.file_upload.path)
    if os.path.exists(file_upload_path):
      os.remove(file_upload_path)
  base.delete()
  return redirect('base:list')