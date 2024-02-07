## Contenido del repositorio
El repositorio contiene una app desarrollada usando Svelte, Tailwind CSS y FastAPI. El objetivo es crear una aplicación base que sea fácil de extender para distintas funcionalidades que se le quieran agregar dependiendo del contexto. Para esto se quiere crear secciones de formularios que pueden ser utilizados por determinados usuarios y poder visualizar los datos que se vayan agregando a la base de datos.

### Backend

Instalación
```
    pip install "fastapi[all]"
    pip install sqlalchemy
    pip install "python-jose[cryptography]"
    pip install bcrypt==4.0.1
    pip install "passlib[bcrypt]"
```
Despliegue
```
    uvicorn main:app --reload
```