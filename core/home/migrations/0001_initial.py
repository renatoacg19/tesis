# Generated by Django 4.2.6 on 2023-11-12 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='factura',
            fields=[
                ('total', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Total')),
                ('fecha_emision', models.CharField(max_length=15, null=True, verbose_name='Fecha_emision')),
                ('fecha_vencimiento', models.CharField(max_length=15, verbose_name='Fecha_vencimiento')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Rut')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=50, verbose_name='Apellido')),
                ('direccion', models.CharField(blank=True, max_length=120, null=True, verbose_name='Direccion')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'db_table': 'Persona',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='productos',
            fields=[
                ('id_productos', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Id_Productos')),
                ('nombre', models.CharField(max_length=20, null=True, verbose_name='Nombre')),
                ('precio_unitario', models.CharField(max_length=20, null=True, verbose_name='Precio_unitario')),
                ('cantidad', models.CharField(max_length=20, null=True, verbose_name='Cantidad')),
                ('cantidad_minima', models.CharField(max_length=20, null=True, verbose_name='Cantidad_minima')),
            ],
        ),
        migrations.CreateModel(
            name='proveedores',
            fields=[
                ('fecha_pago', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='Fecha_Pago')),
                ('monto', models.CharField(max_length=15, verbose_name='Monto')),
            ],
        ),
        migrations.CreateModel(
            name='salidas_fijas',
            fields=[
                ('nombre', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Nombre')),
                ('fecha', models.CharField(max_length=20, verbose_name='Fecha')),
                ('monto', models.CharField(max_length=15, verbose_name='Monto')),
            ],
        ),
        migrations.CreateModel(
            name='servicio',
            fields=[
                ('id_servicio', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Id_servicio')),
                ('nombre', models.CharField(max_length=20, null=True, verbose_name='Nombre')),
                ('costo', models.CharField(max_length=10, null=True, verbose_name='Costo')),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.persona')),
                ('tipo', models.CharField(max_length=50, null=True, verbose_name='Tipo')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'Cliente',
                'ordering': ['id'],
            },
            bases=('home.persona',),
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.persona')),
                ('cargo', models.CharField(max_length=25, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Empleado',
                'verbose_name_plural': 'Empleados',
                'db_table': 'Empleado',
                'ordering': ['id'],
            },
            bases=('home.persona',),
        ),
        migrations.CreateModel(
            name='servicio_producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(max_length=20, verbose_name='Cantidad')),
                ('costo', models.CharField(max_length=15, verbose_name='Costo')),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.productos')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='ingresos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.factura')),
            ],
        ),
        migrations.CreateModel(
            name='Egresos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proveedores', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.proveedores')),
                ('salidas_fijas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.salidas_fijas')),
            ],
        ),
        migrations.CreateModel(
            name='detalles_servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.CharField(max_length=15, verbose_name='Subtotal')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.factura')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='detalles_facturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.factura')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.cliente')),
            ],
        ),
    ]
