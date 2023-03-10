from django import forms
from .models import Base
from django.utils.safestring import mark_safe

class CustomFileWidget(forms.FileInput):
  def __init__(self, attrs={}):
      super().__init__(attrs)

  def render(self, name, value, attrs=None, renderer=None):
    output = []
    if value and hasattr(value, "url"):
      file_name = value.url.split('/')[-1]
      output.append(super().render(name, value, attrs))
      output.append(f'<span class="form-control">첨부파일 : <a class="text-reset text-decoration-none" target="_blank" href="{value.url}">{file_name}</a><input class="form-check-input ms-2 me-1" type="checkbox" name="upload_clear" id="upload_clear_id" value="upload_del">Delete</span>')
      return mark_safe(u''.join(output))
    output.append(super().render(name, value, attrs))
    return mark_safe(u''.join(output))

class BaseCreateForm(forms.ModelForm):  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update({'class' : 'form-control'})
    self.fields['email'].widget.attrs.update({'class' : 'form-control'})
    self.fields['file_upload'].widget.attrs.update({'class' : 'form-control'})
    self.fields['content'].widget.attrs.update({'class' : 'form-control', 'rows' : '20'})
    
    
  class Meta:
    model = Base
    fields = ('title', 'email', 'file_upload', 'content') 
    
class BaseUpdateForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['title'].widget.attrs.update({'class': 'form-control'})
    self.fields['file_upload'].widget.attrs.update({'class': 'form-control'})
    self.fields['content'].widget.attrs.update({'class': 'form-control', 'rows':'20'})

  class Meta:
    model = Base
    fields = ('title', 'file_upload', 'content')
    widgets = {
      'file_upload': CustomFileWidget,
    }