from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class customUserCreationForm(UserCreationForm):

    class Meta:
        model=get_user_model()
        fields=('email','username','age')


class customUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username','age')
