from django.db import models

class Student(models.Model):
    nome = models.CharField("Nome", max_length=155,null=False, blank=False)
    email = models.CharField("E-mail", max_length=255, null=False, blank=False)
    cidade = models.TextField("Cidade", max_length=255, null=True, blank=True)
    formacao = models.CharField("Formação", max_length=255, null=True, blank=True)
    experiencia = models.TextField("Experiência", null=False, blank=True)
    conhecimento_tecnico = models.JSONField("Conhecimento técnico", default=dict())
    linkedin = models.CharField("Linkedin", max_length=255, null=False, blank=True)
    gitHub = models.CharField("Github", max_length=255, null=False, blank=True)
    telefone = models.CharField("Telefone", max_length=255, null=True, blank=True)
    curso = models.CharField("Curso", max_length=255, null=True, blank=True)
    idioma = models.JSONField("Idioma", null=True)
    atividades_extras = models.JSONField("Atividades extras", default=dict())

    def __str__(self):
        return self.name
