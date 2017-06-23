from django import forms
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)

User = get_user_model()

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		username = self.cleaned_data.get("username")
		password = self.cleaned_data.get("password")

		if username and password:
			User = authenticate(username=username, password=password)
			if not User:
				raise forms.ValidationError("Este usuario no existe")

			if not User.check_password(password):
				raise forms.ValidationError("Password Incorrecto")

			if not User.is_active:
				raise forms.ValidationError("Usuario no activado")

		return super(UserLoginForm, self).clean(*args, **kwargs)

class UserRegisterForm(forms.ModelForm):
	email = forms.EmailField(label="Correo Electronico")
	email2 = forms.EmailField(label="Confirme Correo Electronico")
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'email',
			'email2'
		]

	def clean_email2(self):
		email = self.cleaned_data.get('email')
		email2 = self.cleaned_data.get('email2')

		if email != email2:
			raise forms.ValidationError("Email debe coincidir")

		email_qs = User.objects.filter(email=email)
		if email_qs.exists():
			raise forms.ValidationError("Email ya registrado")

		return email