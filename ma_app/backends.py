from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


User = get_user_model()

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None

        # Agrega tus propias validaciones aquí, por ejemplo, verificar el estado de la cuenta, etc.
        if user.check_password(password):
            return user
        else:
            return None
