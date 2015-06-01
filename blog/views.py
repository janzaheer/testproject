from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from models import User
from serializer import UserSerializer
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.edit import FormView
from forms import UserForm
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.views import APIView


class JSONResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

class UserList(ListView):
    model = User

class StoreUser(FormView):
    template_name = 'blog/form.html'
    form_class = UserForm
    success_url = '/blogs/user'
    def form_valid(self, form):
        form.title_save()
        return super(StoreUser, self).form_valid(form)

class GetUser(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return JSONResponse(serializer.data)
        except Exception, e:
            return JSONResponse(e, status=status.HTTP_400_BAD_REQUEST)

class TokenRequest(View):
    def get(self, request):
        new_token = Token.objects.create(user=request.user)
        return HttpResponse(new_token)