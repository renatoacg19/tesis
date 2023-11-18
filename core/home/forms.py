from django.forms import *
from core.home.models import *


class ServicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_servicio'].widget.attrs['autofocus'] = True

    class Meta:
        model = servicio
        fields = '__all__'
        widgets = {

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingresar Nombre',
                }
            ),
            'costo': TextInput(
                attrs={
                    'placeholder': 'Ingresar costo',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ServicioFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id_servicio'].widget.attrs['autofocus'] = True
        self.fields['id_servicio'].widget.attrs['readonly'] = True

    class Meta:
        model = servicio
        fields = '__all__'

        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
    

class EmpleadoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['id'].widget.attrs['autofocus'] = True

    class Meta:
        model = Empleado
        fields = '__all__'

        widgets = {

            'id' : TextInput(
                attrs={
                    'placeholder': 'Ingrese un Rut'
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
            
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class EmpleadoFormEdit(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        self.fields['id'].widget.attrs['autofocus'] = True
        self.fields['id'].widget.attrs['readonly'] = True

    class Meta:
        model = Empleado
        fields = '__all__'

        widgets = {

            'id' : TextInput(
                attrs={
                    'placeholder': 'Ingrese un Rut'
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
            
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class FacturaForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        #    form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['id'].widget.attrs['autofocus'] = True

    class Meta:
        model = factura
        fields = '__all__'

        widgets = {

            'id': TextInput(
                attrs={
                    'placeholder': 'Ingrese '
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class FacturaFormEdit(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #    form.field.widget.attrs['class'] = 'form-control'
        self.fields['id'].widget.attrs['autofocus'] = True
        self.fields['id'].widget.attrs['readonly'] = True

    class Meta:
        model = factura
        fields = '__all__'

        widgets = {

            'id': TextInput(
                attrs={
                    'placeholder': 'Ingrese '
                }
            )
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class Detalles_facturasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['factura'].widget.attrs['autofocus'] = True

    class Meta:
        model = detalles_facturas
        fields = '__all__'
        widgets = {

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingresar Nombre',
                }
            ),
            'costo': TextInput(
                attrs={
                    'placeholder': 'Ingresar costo',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class Detalles_facturasFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['factura'].widget.attrs['autofocus'] = True
        self.fields['factura'].widget.attrs['readonly'] = True

    class Meta:
        model = detalles_facturas
        fields = '__all__'

        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class IngresosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['factura'].widget.attrs['autofocus'] = True

    class Meta:
        model = ingresos
        fields = '__all__'
        widgets = {

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingresar Nombre',
                }
            ),
            'costo': TextInput(
                attrs={
                    'placeholder': 'Ingresar costo',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class IngresosFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['factura'].widget.attrs['autofocus'] = True
        self.fields['factura'].widget.attrs['readonly'] = True

    class Meta:
        model = ingresos
        fields = '__all__'

        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ProductosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['autofocus'] = True

    class Meta:
        model = productos
        fields = '__all__'
        widgets = {

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingresar Nombre',
                }
            ),
            'costo': TextInput(
                attrs={
                    'placeholder': 'Ingresar costo',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ProductosFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id'].widget.attrs['autofocus'] = True
        self.fields['id'].widget.attrs['readonly'] = True

    class Meta:
        model = productos
        fields = '__all__'

        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ProveedoresForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['autofocus'] = True

    class Meta:
        model = proveedores
        fields = '__all__'
        widgets = {

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingresar Nombre',
                }
            ),
            'costo': TextInput(
                attrs={
                    'placeholder': 'Ingresar costo',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ProveedoresFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id'].widget.attrs['autofocus'] = True
        self.fields['id'].widget.attrs['readonly'] = True

    class Meta:
        model = proveedores
        fields = '__all__'

        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class EgresosForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['proveedores'].widget.attrs['autofocus'] = True

    class Meta:
        model = Egresos
        fields = '__all__'
        widgets = {

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingresar Nombre',
                }
            ),
            'costo': TextInput(
                attrs={
                    'placeholder': 'Ingresar costo',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class EgresosFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['proveedores'].widget.attrs['autofocus'] = True
        self.fields['proveedores'].widget.attrs['readonly'] = True

    class Meta:
        model = Egresos
        fields = '__all__'

        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class Salidas_fijasForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['autofocus'] = True

    class Meta:
        model = salidas_fijas
        fields = '__all__'
        widgets = {

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingresar Nombre',
                }
            ),
            'costo': TextInput(
                attrs={
                    'placeholder': 'Ingresar costo',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class Salidas_fijasFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['id'].widget.attrs['autofocus'] = True
        self.fields['id'].widget.attrs['readonly'] = True

    class Meta:
        model = salidas_fijas
        fields = '__all__'

        widgets = {
            'id': TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class Detalles_servicioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['factura'].widget.attrs['autofocus'] = True

    class Meta:
        model = detalles_servicio
        fields = '__all__'
        widgets = {

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingresar Nombre',
                }
            ),
            'costo': TextInput(
                attrs={
                    'placeholder': 'Ingresar costo',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class Detalles_servicioFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['factura'].widget.attrs['autofocus'] = True
        self.fields['factura'].widget.attrs['readonly'] = True

    class Meta:
        model = detalles_servicio
        fields = '__all__'

        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class ClienteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {

            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingresar Nombre',
                }
            ),
            'costo': TextInput(
                attrs={
                    'placeholder': 'Ingresar costo',
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ClienteFormEdit(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['tipo'].widget.attrs['autofocus'] = True
        self.fields['tipo'].widget.attrs['readonly'] = True

    class Meta:
        model = Cliente
        fields = '__all__'

        widgets = {
            'nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el codigo'
                }
            ),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():

                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data
