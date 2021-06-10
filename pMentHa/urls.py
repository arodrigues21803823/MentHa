from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("patientoverview", views.patientoverview, name="patientoverview"),
    path("mentha-care", views.mentha_care, name="mentha-care"),
    path("register", views.register, name="register"),
    path("Registo", views.regPatient, name="regPatient"),
    path("Teste<int:testID>-Paciente<int:patientID>", views.fazPrimeiraPergunta, name="fazPrimeiraPergunta"),
    path("Resolucao<int:resolutionID>-Questao<int:questionID>", views.fazPergunta, name="fazPergunta"),
    path("Report<int:testID>-<int:patientID>", views.report, name="report"),
    path("about", views.about, name="about"),
    path("contacts", views.contact, name="contact"),
    path("contactList", views.contacts_list, name="contactList"),
    path("testinho", views.test, name="test"),
    path("comments", views.comments, name="comments"),
    path("apaga-view<int:atributeID>", views.delete_contact, name="apaga-view"),
    #Django Auth

    path("login_", views.login_, name="login_"),
    path("logout_", views.logout_, name="logout_")
]
