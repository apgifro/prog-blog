from django import forms
from django.core.mail import EmailMessage

from app.models import Comentario


class EmailPost(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    destino = forms.EmailField()
    coments = forms.CharField(required=False,
                              widget=forms.Textarea)

    def enviar_email(self, post):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        destino = self.cleaned_data['destino']
        coments = self.cleaned_data['coments']

        conteudo = f'Recomendo ler o post: {post.titulo}\n' \
                   f'Comentários: {coments}'
        mail = EmailMessage(
            subject=f"{nome} recomenda este post!",
            body=conteudo,
            from_email='contato@meublog.com.br',
            to=[destino],
            headers={'Reply-To': email}
        )
        mail.send()


class ComentModelForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ['nome', 'email', 'texto']

    def salvar_comentario(self, post):
        novo_coment = self.save(commit=False)
        novo_coment.post = post
        novo_coment.nome = self.cleaned_data['nome']
        novo_coment.email = self.cleaned_data['email']
        novo_coment.texto = self.cleaned_data['texto']
        return novo_coment.save()
