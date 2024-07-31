from rest_framework.response import Response
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class CreatedModifiedModel(models.Model):
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True




def custom_response(
    data,
    status,
):
    """
    @rtype: object
    """
    return Response(data, status)



def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }