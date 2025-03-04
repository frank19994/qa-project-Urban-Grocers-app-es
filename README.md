# Proyecto Urban Grocers

## 📌 Descripción
Automatización de pruebas del campo `name` para la creación de un nuevo kit en la API del servicio.

## 🚀 Instalación

1. Crea un directorio:
   ```bash
   cd ~     # Debes estar en tu directorio de inicio
   mkdir projects # Crea una carpeta llamada projects
   cd projects
   ```
2. Clona el repositorio:
   ```bash
   git clone git@github.com:frank19994/qa-project-Urban-Grocers-app-es.git
   ```
3. Entra a la carpeta del proyecto:
   ```bash
   cd qa-project-Urban-Grocers-app-es
   ```

## 🛠️ Tecnologías utilizadas
- **Python** → Lenguaje de programación principal
- **Pytest** → Framework de pruebas
- **Requests** → Librería para realizar solicitudes HTTP

---

## 📄 Explicación de archivos clave

### `configuration.py`
Este archivo almacena las configuraciones principales del servicio API, como la URL base y los endpoints utilizados en las solicitudes.

#### 📌 Variables definidas
1. **`URL_SERVICE`** → Contiene la URL base del servicio API:
   ```python
   URL_SERVICE = "https://cnt-997a8bc5-783f-4694-8bc7-c1534f52d7ad.containerhub.tripleten-services.com"
   ```
   Todas las solicitudes a la API utilizarán esta URL como punto de partida.
2. **`CREATE_USER_PATH`** → Define el endpoint para la creación de usuarios:
   ```python
   CREATE_USER_PATH = "/api/v1/users"
   ```
   Se usa en la función `post_new_client_kit()` en `sender_stand_request.py`.
3. **`KITS_PATH`** → Define el endpoint para la creación de kits:
   ```python
   KITS_PATH = "/api/v1/kits"
   ```
   Se usa en la función `post_new_kit()` en `sender_stand_request.py`.

#### 🎯 Propósito
- Mantener centralizadas las URLs y endpoints, facilitando modificaciones en caso de cambios en la API.

---

### `data.py`
Este archivo define los datos de prueba y los encabezados utilizados en las solicitudes HTTP a la API.

#### 📌 Variables definidas
1. **`headers`** → Define los encabezados HTTP utilizados en las solicitudes:
   ```python
   headers = { "Content-Type": "application/json" }
   ```
   Indica que el cuerpo de la solicitud se enviará en formato **JSON**.

2. **`user_body`** → Contiene un ejemplo de datos para crear un nuevo usuario:
   ```python
   user_body = {
       "firstName": "Max",
       "phone": "+10005553535",
       "address": "8042 Lancaster Ave. Hamburg, NY"
   }
   ```

3. **`kit_body`** → Contiene un ejemplo de datos para crear un nuevo kit:
   ```python
   kit_body = { "name": "Max kit" }
   ```

#### 🎯 Propósito
- Permite reutilizar estos datos en las solicitudes.
- Facilita la ejecución de pruebas automatizadas con valores predefinidos.
- Mantiene el código más organizado y modular.

---

### `sender_stand_request.py`
Este archivo maneja las solicitudes **POST** a la API del servicio, permitiendo la creación de usuarios y kits.

#### 📌 Funciones principales
1. **`post_new_client_kit(body)`**
   - Envía una solicitud **POST** para crear un nuevo usuario.
   - Usa la URL definida en `configuration.URL_SERVICE + configuration.CREATE_USER_PATH`.
   - Envía el cuerpo de la solicitud (`body`) como **JSON**.
   - Usa los encabezados (`headers`) definidos en `data.headers`.
   - **Retorna** la respuesta de la API.

2. **`post_new_kit(kit_body, auth_token)`**
   - Envía una solicitud **POST** para crear un nuevo kit.
   - Usa la URL definida en `configuration.URL_SERVICE + configuration.KITS_PATH`.
   - Copia los encabezados (`headers`) de `data.headers`.
   - Agrega un **token de autorización** en el encabezado (`Authorization: Bearer <auth_token>`).
   - Envía el cuerpo de la solicitud (`kit_body`) como **JSON**.
   - **Retorna** la respuesta de la API.

#### 📌 Dependencias
- **Requests** → Para enviar solicitudes HTTP.
- **configuration.py** → Contiene las URLs del servicio.
- **data.py** → Contiene los encabezados (`headers`) usados en las solicitudes.

---

### `create_kit_name_kit_test.py`
Este archivo contiene pruebas automatizadas para verificar la creación de un kit en la API, evaluando diferentes valores en el campo **`name`**.

#### 📌 Funciones principales
1. **`get_token_user_new()`**
   - Crea un nuevo usuario mediante `post_new_client_kit()` de `sender_stand_request.py`.
   - Extrae y devuelve el **token de autenticación (`authToken`)** de la respuesta JSON.

2. **`get_name_kit(kit_body)`**
   - Crea una copia del `kit_body` del archivo `data.py`.
   - Reemplaza el valor del campo `"name"` con el que se pase como argumento.

3. **`positive_assert(kit_body)`**
   - Envía una solicitud **POST** para crear un kit con un nombre válido.
   - **Verifica que la respuesta tenga un código 201 (creado con éxito).**
   - **Verifica que el nombre en la respuesta sea el mismo que se envió.**

4. **`negative_assert(kit_body)`**
   - Envía una solicitud **POST** para crear un kit con un nombre inválido.
   - **Verifica que la respuesta tenga un código 400 (solicitud incorrecta).**

#### 🎯 Propósito
- Verificar que la API **acepta y rechaza** nombres de manera correcta.
- Garantizar que la validación del campo **`name`** funciona según lo esperado.
- Automatizar la validación para evitar errores en producción.

---

## 🧪 Ejecución de pruebas
Para correr las pruebas automatizadas, usa el siguiente comando en la terminal:

```bash
 create_kit_name_kit_test.py
```

Si no tienes **pytest**, instálalo con:

```bash
pip install pytest
```

---


