# Generated by Django 2.2.4 on 2019-09-14 16:11

import apps.base.models.company
import apps.base.models.product
import apps.base.models.usercustom
import apps.base.rename_image
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='PyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('password', models.CharField(max_length=128, verbose_name='Password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last login')),
                ('is_superuser', models.BooleanField(db_index=True, default=False, verbose_name='Super Admin')),
                ('is_staff', models.BooleanField(db_index=True, default=False, verbose_name='Staff')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active')),
                ('username', models.CharField(db_index=True, max_length=150, unique=True, verbose_name='User name')),
                ('first_name', models.CharField(max_length=30, verbose_name='Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('email', models.CharField(db_index=True, max_length=254, unique=True, verbose_name='Email')),
                ('telefono', models.CharField(blank=True, max_length=255, null=True, verbose_name='Phone')),
                ('celular', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mobile Phone')),
                ('fecha_nacimiento', models.DateField(blank=True, null=True, verbose_name='Birthdate')),
                ('sexo', models.CharField(blank=True, choices=[('F', 'FEMALE'), ('M', 'MALE')], max_length=255, null=True, verbose_name='Sex')),
                ('avatar', models.ImageField(blank=True, default='avatar/default_avatar.png', max_length=255, null=True, storage=apps.base.rename_image.RenameImage(), upload_to=apps.base.models.usercustom.image_path)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'People',
                'verbose_name': 'Person',
                'db_table': 'auth_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(max_length=500)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PyApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('author', models.CharField(max_length=80, verbose_name='Author')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('installed', models.BooleanField(blank=True, default=False, null=True)),
                ('website', models.CharField(blank=True, max_length=180, null=True, verbose_name='Website')),
                ('color', models.CharField(blank=True, max_length=20, null=True, verbose_name='Color')),
                ('fa', models.CharField(blank=True, max_length=20, null=True, verbose_name='Icon')),
                ('version', models.CharField(blank=True, max_length=20, null=True, verbose_name='Version')),
                ('sequence', models.IntegerField(default=100, verbose_name='Sequence')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PyCountry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PyCron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('active', models.BooleanField(default=False, verbose_name='Activo')),
                ('interval_type', models.CharField(choices=[('minutes', 'Almacenable'), ('hours', 'Horas'), ('work_day', 'Días laborales'), ('weeks', 'Semanas'), ('month', 'Meses')], default='hours', max_length=64)),
                ('model_name', models.CharField(max_length=40, verbose_name='Modelo')),
                ('function', models.CharField(max_length=40, verbose_name='Método')),
                ('number_call', models.IntegerField(default=-1, verbose_name='Número de llamadas')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='PyCurrency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=3, verbose_name='Nombre')),
                ('alias', models.CharField(max_length=40, verbose_name='Alias')),
                ('symbol', models.CharField(max_length=1, verbose_name='Símbolo')),
                ('position', models.CharField(choices=[('before', 'Antes de la Cantidad'), ('after', 'Después de la Cantidad')], default='after', max_length=64)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PyFaq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
                ('content', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('note', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='PyPaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40)),
                ('plugin', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PyPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=255, verbose_name='Nombre')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('keywords', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PyWebsiteConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('show_blog', models.BooleanField(default=False, verbose_name='Show Blog')),
                ('show_shop', models.BooleanField(default=False, verbose_name='Show Shop')),
                ('show_price', models.BooleanField(default=True, verbose_name='Show price')),
                ('show_chat', models.BooleanField(default=False, verbose_name='Show chat')),
                ('under_construction', models.BooleanField(default=False, verbose_name='Under Construction')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PyWPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40, verbose_name='Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PyProductWebCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40)),
                ('parent_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.PyProductWebCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PyProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40)),
                ('parent_id', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.PyProductCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PyProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('code', models.CharField(blank=True, max_length=80, verbose_name='Code')),
                ('bar_code', models.CharField(blank=True, max_length=80, verbose_name='Bar Code')),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Price')),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='cost')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('img', models.ImageField(blank=True, default='product/default_product.png', max_length=255, null=True, storage=apps.base.rename_image.RenameImage(), upload_to=apps.base.models.product.image_path)),
                ('web_active', models.BooleanField(default=False, verbose_name='Web')),
                ('type', models.CharField(choices=[('product', 'Almacenable'), ('consu', 'Consumible'), ('service', 'Servicio')], default='consu', max_length=64, verbose_name='type')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.PyProductCategory')),
                ('web_category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.PyProductWebCategory')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='PyPartner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40, verbose_name='Nombre')),
                ('street', models.CharField(blank=True, max_length=100, verbose_name='Calle')),
                ('street_2', models.CharField(blank=True, max_length=100, verbose_name='Calle 2')),
                ('city', models.CharField(blank=True, max_length=50, verbose_name='Ciudad')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Teléfono')),
                ('email', models.EmailField(blank=True, max_length=40, verbose_name='Correo')),
                ('customer', models.BooleanField(default=True, verbose_name='Es cliente')),
                ('provider', models.BooleanField(default=True, verbose_name='Es proveedor')),
                ('for_invoice', models.BooleanField(default=True, verbose_name='Para Facturar')),
                ('note', models.TextField(blank=True, null=True)),
                ('not_email', models.BooleanField(default=False, verbose_name='No Email')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pypartner_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='PyCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, default=True, null=True)),
                ('fc', models.DateTimeField(auto_now_add=True, null=True)),
                ('fm', models.DateTimeField(auto_now=True, null=True)),
                ('uc', models.IntegerField(blank=True, null=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('company_id', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=40)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('street_2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=40)),
                ('giro', models.CharField(blank=True, max_length=80)),
                ('social_facebook', models.CharField(blank=True, max_length=255)),
                ('social_instagram', models.CharField(blank=True, max_length=255)),
                ('social_linkedin', models.CharField(blank=True, max_length=255)),
                ('slogan', models.CharField(blank=True, max_length=250, verbose_name='Eslogan')),
                ('logo', models.ImageField(blank=True, default='logo/default_logo.png', max_length=255, null=True, storage=apps.base.rename_image.RenameImage(), upload_to=apps.base.models.company.image_path)),
                ('currency_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.PyCurrency')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BaseConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online', models.BooleanField(default=False, verbose_name='Online')),
                ('open_menu', models.BooleanField(default=True, verbose_name='Menu Abierto')),
                ('load_data', models.BooleanField(default=False, verbose_name='Data Cargada')),
                ('main_company_id', models.ForeignKey(blank=True, null=True, on_delete='cascade', to='base.PyCompany')),
            ],
        ),
    ]
