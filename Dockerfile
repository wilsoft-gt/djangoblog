#Docker image to use
FROM python:3.10.6-alpine3.16

#Defines the working directory for the app
WORKDIR /app/

#Copy all files to the app folder
COPY . /app/

#Defines ENV Variables
ENV SECRET_KEY="b=d6%n&lfuv$3t5e_1y)gyc#f0-9l%#8_-a83+ovxbm#by!)iy"
ENV IS_DEBUG="False"

#Required for python createuser --noinput
ENV DJANGO_SUPERUSER_EMAIL="admin@admin.com"
ENV DJANGO_SUPERUSER_USERNAME="sysadmin"
ENV DJANGO_SUPERUSER_PASSWORD="admin123."

#Install dependencies
RUN pip install -r requirements.txt

#Generate database tables and superuser
RUN python manage.py migrate
RUN python manage.py makemigrations
RUN python manage.py createsuperuser --noimput
RUN python manage.py collectstatic

#Start the server
CMD [ "python", "manage.py", "runserver", "0:8080" ]







