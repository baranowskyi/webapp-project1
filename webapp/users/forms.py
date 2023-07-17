from django.contrib.auth.forms import UserCreationForm
from users.models import UserSite


# custom registration form
class CustomRegisterForm(UserCreationForm):
	class Meta:
		model = UserSite
		fields = ('username', 'email', 'password1', 'password2')


