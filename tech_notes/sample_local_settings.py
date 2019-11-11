"""store all local settings here and exclude it from git"""

import os

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'app_name',
		'USER': 'app_admin',
		# 'PASSWORD': os.environ.get('app_admin_pwd'),
		'PASSWORD':'******',
		'HOST': 'localhost',
        # 'HOST': '127.0.0.1',
		'PORT': '5432',
	}
}
