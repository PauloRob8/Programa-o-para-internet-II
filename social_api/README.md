# API de rede social utilizando DRF (Django Rest Framework)
Esquema de rede social com Perfis, postagem e comentários. Utilizando autenticações básicas e via Token.

## Requisitos
- Python 3.7.5
- django-extensions 2.2.5
- django
- rest_framework

## Populando o banco de dados automaticamente (Opcional)
Primeiramente serão repassado os dados do arquivo **db.json** para o arquivo **db.sqlite3**

Rode os seguintes comandos: 

``` python manage.py migrate ``` 

``` python manage.py runscript import_data ```

**Obs**: a extensão django-extensions precisa ser instalada para utilização do comando ``` runscript ``` .

## Relacionamentos e Permissões

No projeto existiram **Usuários** os mesmos possuem **Perfis**

* Apenas usuários logados poderam realizar postagens.
* Apenas o perfil dono de uma postagem pode editar e excluir a mesma.
* Apenas o Perfil dono da postagem pode excluir comentários de sua postagem.

## Apresentação
