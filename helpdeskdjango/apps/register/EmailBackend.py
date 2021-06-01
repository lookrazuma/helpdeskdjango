from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None,):
            if '@' in username:
                kwargs = {'email': username}
            else:
                kwargs = {'username': username}

            try:
                user = User.objects.get(**kwargs)
                if user.check_password(password):
                    return user
                else:
                    return None
            except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None