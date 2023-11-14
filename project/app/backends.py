from django.contrib.auth.backends import ModelBackend
from .models import Author

class AuthorBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = self.user_class.objects.get(username=username)
        except self.user_class.DoesNotExist:
            return None

        if user.check_password(password) and hasattr(user, 'author'):
            return user
        return None

    @property
    def user_class(self):
        return Author