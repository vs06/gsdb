from django.db import connection
from django.http import HttpResponse
from django.http import response, request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from gospelsongsdb.models import Musica


# Create your views here.
def index(request):
    return redirect('/admin/')

class Log(TemplateView):
    template_name = 'admin/log.html'
        
    def get_context_data(self, **kwargs):
        def my_custom_sql(self):
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM ( SELECT usuario.username, log.action_flag, log.object_repr, modelo.model, log.action_time FROM django_admin_log log INNER JOIN auth_user usuario ON log.user_id = usuario.id INNER JOIN django_content_type modelo ON log.content_type_id = modelo.id ORDER BY action_time DESC ) TEST;")
            #row = cursor.fetchone()
            desc = cursor.description
            return [
                    dict(zip([col[0] for col in desc], row))
                    for row in cursor.fetchall()
                ]
            
        context = TemplateView.get_context_data(self, **kwargs) 
        context['logs']= my_custom_sql(self)
        return context
    
class MostPlayed(TemplateView):
    template_name = 'admin/mais_tocadas.html'
    
#     def get(self, request, *args, **kwargs):
#         return TemplateView.get(self, request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        if 'pesquisar' in request.POST:
            try:
                nomemusica= request.POST.get('nomemusica')
                musica = Musica.objects.filter(id=nomemusica)
            except Exception as e:
                raise e
        #context = self.get_context_data(**kwargs)   # refresh
        return render(request, self.template_name, context)
    
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs) 
        musica_id = ''
        if 'nomemusica' in kwargs and kwargs['nomemusica']:
            musica_id = Musica.objects.filter(id=kwargs['nomemusica'])
        print('teste -------------->', musica_id)
        def my_custom_sql(self):
                
            cursor = connection.cursor()
            cursor.execute("select c.date, m.name from gospelsongsdb_culto_musicas cm \
            inner join gospelsongsdb_culto c on c.id = cm.culto_id \
            inner join gospelsongsdb_musica m on m.id = cm.musica_id \
            where m.id = %s;",[musica_id])
            #row = cursor.fetchone()
            desc = cursor.description
        
            return [
                    dict(zip([col[0] for col in desc], row))
                    for row in cursor.fetchall()
                ]
        context['mais_tocadas']= my_custom_sql(self)
        context['musicas'] = Musica.objects.all()
        return context
