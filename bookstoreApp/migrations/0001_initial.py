# Generated by Django 3.2.7 on 2021-10-11 02:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('password', models.CharField(max_length=256, verbose_name='Password')),
                ('fullname', models.CharField(blank=True, max_length=200, null=True, verbose_name='Fullname')),
                ('datebirth', models.DateField(blank=True, null=True, verbose_name='Datebirth')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('U', 'Unsure')], default='U', max_length=1)),
                ('email', models.EmailField(blank=True, max_length=320, null=True, verbose_name='Email')),
                ('identification', models.CharField(blank=True, max_length=15, null=True, verbose_name='Identification')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone number')),
                ('address', models.CharField(blank=True, max_length=50, null=True, verbose_name='Address')),
                ('is_employee', models.BooleanField(default=False)),
                ('is_customer', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=150, null=True, verbose_name='Description')),
                ('provider_name', models.CharField(blank=True, max_length=45, null=True, verbose_name='Provider')),
                ('stock', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='WorkArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='work area name')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Books', serialize=False, to='bookstoreApp.product')),
                ('title', models.CharField(blank=True, max_length=45, null=True, verbose_name='Title')),
                ('author', models.CharField(blank=True, max_length=45, null=True, verbose_name='Autor')),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('isbn', models.CharField(blank=True, max_length=13, null=True, verbose_name='ISSN')),
                ('editorial', models.CharField(blank=True, max_length=30, null=True, verbose_name='Editorial')),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Magazines', serialize=False, to='bookstoreApp.product')),
                ('name', models.CharField(blank=True, max_length=45, null=True, verbose_name='Name')),
                ('edition', models.IntegerField(blank=True, default=0, null=True)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('issn', models.CharField(blank=True, max_length=8, null=True, verbose_name='ISSN')),
                ('editorial', models.CharField(blank=True, max_length=30, null=True, verbose_name='Editorial')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sold_products', to='bookstoreApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('datetime', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reserved_products', to='bookstoreApp.product')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='employees', serialize=False, to='bookstoreApp.user')),
                ('salary', models.BigIntegerField(blank=True, null=True, verbose_name='Salary')),
                ('is_seller', models.BooleanField(default=False)),
                ('is_inventory_manager', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('work_area', models.ForeignKey(blank=True, db_column='work_area_name', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='employees', to='bookstoreApp.workarea', to_field='name')),
            ],
        ),
    ]
