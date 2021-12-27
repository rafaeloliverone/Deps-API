from django.contrib import admin 

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    fields = ('nome', 'email', 'cidade', 'formacao', 'experiencia', 'conhecimento_tecnico', 'linkedin', 'gitHub', 'telefone', 'curso', 'idioma', 'atividades_extras')

admin.site.register(Student, StudentAdmin)
