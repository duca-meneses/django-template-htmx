# Django Core Template

Um template moderno para projetos Django com HTMX, TailwindCSS e Alpine.js.

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)
![Django](https://img.shields.io/badge/Django-5.0.6-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🚀 Características

- ⚡️ Stack moderna e rápida
- 🔒 Sistema de autenticação completo com django-allauth
- 👤 Gerenciamento de perfil de usuário
- 🎨 Interface responsiva com TailwindCSS
- 🔄 Interações dinâmicas com HTMX e Alpine.js
- 🐳 Containerização com Docker
- 📝 Formatação de código com Ruff
- 🧪 Testes automatizados

## 🛠️ Tecnologias

- [Django 5.0](https://www.djangoproject.com/)
- [HTMX](https://htmx.org/)
- [TailwindCSS](https://tailwindcss.com/)
- [Alpine.js](https://alpinejs.dev/)
- [Django AllAuth](https://django-allauth.readthedocs.io/)
- [Django Environ](https://django-environ.readthedocs.io/)
- [Django Cleanup](https://github.com/un1t/django-cleanup)
- [WhiteNoise](http://whitenoise.evans.io/)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/django_core_template.git
cd django_core_template
```

2. Configure o ambiente virtual com Poetry:
```bash
poetry install
```

3. Configure as variáveis de ambiente:
```bash
cp backend/.env.example backend/.env
```

4. Execute as migrações:
```bash
cd backend
python manage.py migrate
```

5. Instale as dependências do frontend:
```bash
npm install
```

6. Compile os assets:
```bash
npm run build
```

## 🚀 Executando o Projeto

### Desenvolvimento

```bash
# Backend
python manage.py runserver

# Frontend (em outro terminal)
npm run watch
```

### Docker

```bash
docker compose up
```

## 🧪 Testes

```bash
python manage.py test
```

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👥 Contribuindo

Contribuições são bem-vindas! Por favor, sinta-se à vontade para enviar um Pull Request.

1. Faça o Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

