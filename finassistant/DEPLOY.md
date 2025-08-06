# Деплой на Heroku

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
