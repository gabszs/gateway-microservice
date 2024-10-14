# 🚀 API de Conversão de Vídeos em Áudio

Este projeto implementa uma API que permite a conversão de vídeos em arquivos de áudio. A API utiliza serviços de mensageria para orquestrar a conversão, armazenamento no Cloudflare R2, e envio de notificações por email com o link de download do áudio convertido.

## 📦 Instalação

Para instalar o projeto, utilize os seguintes comandos:

### 1. Clone o repositório:
git clone https://github.com/gabszs/gateway-microservice.git
cd gateway-microservice

### 2. Instale as dependências utilizando Poetry:
poetry install

## 🚀 Uso

### Conversão de Vídeo para Áudio
O serviço permite que você envie um vídeo, que será armazenado no bucket S3 da Cloudflare R2. Após o envio, a conversão para áudio será realizada por um serviço consumidor, e o arquivo de áudio será salvo no bucket. Em seguida, uma notificação será enviada ao usuário com o link de download.

**Endpoint:**  
POST /upload/{email}

```bash
@router.post("/upload/{email}", status_code=status.HTTP_204_NO_CONTENT)
@authorize(role=[UserRoles.MODERATOR, UserRoles.BASE_USER])
async def upload(email: EmailStr, file: fileUpload, service: SaveBucket, current_user: CurrentUser):
    await service.upload_video_file(file, client_email=email)
```
### Autenticação de Usuários
O endpoint permite que os usuários se autentiquem na API fornecendo suas informações de login. Após a validação, um token de autenticação é gerado e retornado para o usuário.
```bash
@router.post("/sign-in", response_model=SignInResponse)
async def sign_in(user_info: SignIn, service: AuthServiceDependency):
    return await service.sign_in(user_info)
```
que faz chamadas remotas no servico de auth e validada a identidate do user, que tambem retorna os atributos do user, permitindo a validacao de RBAC pelo servico.

Para a validacao no endpoint da autencidade do token do user, se usar a dependencia 
```bash
async def get_current_user(user_credentials: UserSchema = Depends(JWTBearer())) -> UserSchema:
    return user_credentials
```


## 🛠 Funcionalidades

- **Upload de Vídeo:** Permite o upload de vídeos que serão armazenados no Cloudflare R2 (S3-compatible).
- **Conversão Assíncrona:** A conversão de vídeos em áudio é realizada de forma assíncrona através de serviços de mensageria.
- **Armazenamento de Áudio:** O áudio convertido é armazenado no Cloudflare R2.
- **Notificações:** O serviço envia emails com o link para download do áudio convertido.

## 🗂 Estrutura de Diretórios

C:.
├───.github
│   └───workflows
├───app
│   ├───core
│   ├───helpers
│   ├───routes
│   │   └───v1
│   ├───schemas
│   └───services
└───tests
    ├───schemas

## ⚙️ Requisitos

- Python 3.8 ou superior
- FastAPI
- MinIO
- JWT para autenticação

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request ou entrar em contato para discutir novas funcionalidades.

## 📝 Licença

Este projeto é licenciado sob a licença MIT. Consulte o arquivo LICENSE para obter mais informações.
