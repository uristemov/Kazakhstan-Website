from django import forms
from .models import Comment, User

class CommentCreate(forms.ModelForm):
          class Meta:
                    model=Comment
                    fields='__all__'
class AddUser(forms.ModelForm):
          class Meta:
                    model = User
                    fields = '__all__'