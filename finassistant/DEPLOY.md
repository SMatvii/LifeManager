# Деплой на Heroku

⚠️ **УВАГА**: Heroku більше не має безкоштовного плану. Мінімальна вартість $5-7 в місяць.

## Швидкий старт:

1. **Створіть обліковий запис на Heroku**: https://signup.heroku.com/

2. **Встановіть Heroku CLI**: https://devcenter.heroku.com/articles/heroku-cli

3. **Зайдіть в папку проекту**:
   ```bash
   cd finassistant
   ```

4. **Увійдіть в Heroku**:
   ```bash
   heroku login
   ```

5. **Створіть додаток**:
   ```bash
   heroku create your-app-name
   ```

6. **Встановіть змінні середовища**:
   ```bash
   heroku config:set SECRET_KEY="your-secret-key-here"
   heroku config:set DEBUG="False"
   heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
   ```

7. **Деплой**:
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

8. **Запустіть міграції**:
   ```bash
   heroku run python manage.py migrate
   heroku run python manage.py createsuperuser
   ```

9. **Відкрийте сайт**:
   ```bash
   heroku open
   ```

## Для OAuth (опціонально):

Якщо хочете Google/GitHub логін:
1. Створіть додатки в Google/GitHub
2. Додайте ключі:
   ```bash
   heroku config:set GOOGLE_CLIENT_ID="your-google-id"
   heroku config:set GOOGLE_CLIENT_SECRET="your-google-secret"
   ```

## Простий деплой через GitHub:

1. Завантажте код на GitHub
2. В Heroku Dashboard -> New -> Create new app
3. Connect to GitHub -> Select repository
4. Enable Automatic Deploys
5. Deploy Branch

Ваш сайт буде доступний на: `https://your-app-name.herokuapp.com`

---
## 🆓 Безкоштовні альтернативи

### Railway (Рекомендовано)
1. Перейдіть на: https://railway.app/
2. **Connect GitHub** → виберіть репозиторій
3. **Deploy** → автоматично
4. **Variables** → додайте SECRET_KEY, DEBUG=False
5. Отримайте URL: `https://your-app-name.up.railway.app`

### Render
1. Перейдіть на: https://render.com/
2. **New Web Service** → Connect GitHub
3. **Environment**: Python 3
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `gunicorn finassistant.wsgi:application`
6. **Environment Variables** → додайте змінні

### PythonAnywhere
1. Перейдіть на: https://www.pythonanywhere.com/
2. **Безкоштовний акаунт** → завантажте код
3. **Web** → створіть новий додаток
4. Налаштуйте WSGI файл для Django
