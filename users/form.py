
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile, Ebooks, Books, Chats, CommandBook

User = get_user_model()
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields=[
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]

class ProfileForm(forms.ModelForm):
    matricule = forms.CharField(max_length=15, initial="UBA")
    class Meta():
        model = Profile
        fields = [
            'matricule',
            'school',
            'department',
            'level',
            'picture'
        ]

        labels = {
            'picture': 'Upload a clear 4x4 photo',
        }

    def clean_matricule(self,*args, **kwargs):
        matricule = self.cleaned_data.get('matricule')
        mat = matricule.lower()
        if not 'uba' in mat:
            raise forms.ValidationError("UBA need to be inside your matricle")
        else:
            return matricule 

class EbookForm(forms.ModelForm):
    pdf = forms.FileField()
    class Meta():
        model = Ebooks
        fields  = ('title', 'author', 'description', 'category', 'pdf', 'cover')
        labels = {
            'pdf':'Choose PDF Book',
            'cover':'Choose Cover Book'
              
        }

    def clean_pdf(self, *args, **kwargs):
        pdf = self.cleaned_data.get('pdf')
        ext = pdf.split('.')[-1].lower()
        if ext != 'pdf':
            raise forms.ValidationError("Please the file need to be a pdf format")
        else:
            return pdf        

class BookForm(forms.ModelForm):
    class Meta():
        model = Books
        fields  = ('title', 'author', 'description', 'category',  'cover')
        labels = {
            'cover':'Choose Cover Book',
              
        } 

class ChatForm(forms.ModelForm):
    class Meta():
        model = Chats
        fields = ('message',)   
        labels = {
            'message':'Message..'
        }            

class UserAdminForm(forms.ModelForm):
    class Meta():
        model = User
        fields=[
            'username',
            'email',
            'first_name',
            'last_name',
            'is_admin',
            'is_librarian',
            'is_student',
            'is_not_verified',
        ]   


class CommandForm(forms.ModelForm):
    class Meta():
        model = CommandBook
        fields = ('__all__')   
                       

            