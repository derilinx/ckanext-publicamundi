import zope.interface
import zope.schema
import z3c.schema.email
import zope.schema.interfaces

from ckan.plugins import toolkit

from ckanext.publicamundi.lib.metadata.widgets import base as base_widgets
from ckanext.publicamundi.lib.metadata.widgets import \
    field_widget_adapter, field_widget_multiadapter

from ckanext.publicamundi.lib import logger

# Todo: Provide readers/editors for:
#  - IBytes (upload?)

# Editors #

@field_widget_adapter(zope.schema.interfaces.IText)
class TextEditWidget(base_widgets.EditFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/edit-text.html'

@field_widget_adapter(zope.schema.interfaces.INativeString)
@field_widget_adapter(zope.schema.interfaces.ITextLine)
class TextLineEditWidget(base_widgets.EditFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/edit-textline.html'

@field_widget_adapter(zope.schema.interfaces.ITextLine, qualifiers=['email'])
@field_widget_adapter(z3c.schema.email.interfaces.IRFC822MailAddress)
class EmailEditWidget(base_widgets.EditFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/edit-textline-email.html'

@field_widget_adapter(zope.schema.interfaces.IURI)
class UriEditWidget(base_widgets.EditFieldWidget):
   
    def get_template(self):
        return 'package/snippets/fields/edit-uri.html'

@field_widget_adapter(zope.schema.interfaces.IPassword)
class PasswordEditWidget(base_widgets.EditFieldWidget):
   
    def get_template(self):
        return 'package/snippets/fields/edit-password.html'

@field_widget_adapter(zope.schema.interfaces.IInt)
class IntEditWidget(base_widgets.EditFieldWidget):

    def prepare_template_vars(self, name_prefix, data):
        tpl_vars = base_widgets.EditFieldWidget.prepare_template_vars(self, name_prefix, data)
        minval, maxval = self.field.min, self.field.max
        tpl_vars['input_classes'] = [ \
            'span2' if ((minval is None) or (maxval is None) or (maxval - minval > 1e3)) else 'span1' ]
        return tpl_vars
   
    def get_template(self):
        return 'package/snippets/fields/edit-int.html'

@field_widget_adapter(zope.schema.interfaces.IInt, qualifiers=['text'])
class IntAsTextEditWidget(IntEditWidget):
   
    def get_template(self):
        return 'package/snippets/fields/edit-int-text.html'

@field_widget_adapter(zope.schema.interfaces.IFloat)
class FloatEditWidget(base_widgets.EditFieldWidget):

    def prepare_template_vars(self, name_prefix, data):
        tpl_vars = base_widgets.EditFieldWidget.prepare_template_vars(self, name_prefix, data)
        minval, maxval = self.field.min, self.field.max
        tpl_vars['input_classes'] = [ \
            'input-small' if ((minval is None) or (maxval is None) or (maxval - minval > 1e3)) else 'span2' ]
        return tpl_vars
   
    def get_template(self):
        return 'package/snippets/fields/edit-float.html'

@field_widget_adapter(zope.schema.interfaces.IFloat, qualifiers=['text'])
class FloatAsTextEditWidget(FloatEditWidget):
   
    def get_template(self):
        return 'package/snippets/fields/edit-float-text.html'

@field_widget_adapter(zope.schema.interfaces.IBool)
class BoolEditWidget(base_widgets.EditFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/edit-bool-checkbox-1.html'

@field_widget_adapter(zope.schema.interfaces.IChoice, qualifiers=['select'], is_fallback=True)
class ChoiceEditWidget(base_widgets.EditFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/edit-choice-select.html'

@field_widget_adapter(zope.schema.interfaces.IChoice, qualifiers=['select2'])
class ChoiceTwoEditWidget(base_widgets.EditFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/edit-choice-select2.html'

@field_widget_adapter(zope.schema.interfaces.IDate, qualifiers=['datetimepicker'], is_fallback=True)
class DateEditWidget(base_widgets.EditFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/edit-date-datetimepicker.html'

@field_widget_adapter(zope.schema.interfaces.ITime)
class TimeEditWidget(base_widgets.EditFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/edit-time.html'

@field_widget_adapter(zope.schema.interfaces.IDatetime)
class DatetimeEditWidget(base_widgets.EditFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/edit-datetime.html'

@field_widget_adapter(zope.schema.interfaces.IList)
@field_widget_adapter(zope.schema.interfaces.ITuple)
class ListEditWidget(base_widgets.EditFieldWidget, base_widgets.ListFieldWidgetTraits):

    def __init__(self, field):
        assert \
            isinstance(field, zope.schema.List) or \
            isinstance(field, zope.schema.Tuple)
        base_widgets.EditFieldWidget.__init__(self, field)

    def get_template(self):
        return 'package/snippets/fields/edit-list.html'

@field_widget_multiadapter([zope.schema.interfaces.ITuple, zope.schema.interfaces.ITextLine], qualifiers=['tags'])
@field_widget_multiadapter([zope.schema.interfaces.IList, zope.schema.interfaces.ITextLine], qualifiers=['tags'])
class TagsEditWidget(base_widgets.EditFieldWidget):

    def __init__(self, field, *args):
        assert isinstance(field, zope.schema.List)
        base_widgets.EditFieldWidget.__init__(self, field)

    def get_template(self):
        return 'package/snippets/fields/edit-list-tags.html'

@field_widget_adapter(zope.schema.interfaces.IDict)
class DictEditWidget(base_widgets.EditFieldWidget, base_widgets.DictFieldWidgetTraits):

    def __init__(self, field):
        assert isinstance(field, zope.schema.Dict)
        base_widgets.EditFieldWidget.__init__(self, field)

    def get_template(self):
        return 'package/snippets/fields/edit-dict.html'

@field_widget_adapter(zope.schema.interfaces.IObject)
class ObjectEditWidget(base_widgets.EditFieldWidget, base_widgets.ObjectFieldWidgetTraits):

    def __init__(self, field):
        assert isinstance(field, zope.schema.Object)
        base_widgets.EditFieldWidget.__init__(self, field)

    def get_template(self):
        return 'package/snippets/fields/edit-object.html'

# Readers #

@field_widget_adapter(zope.schema.interfaces.IText)
@field_widget_adapter(zope.schema.interfaces.ITextLine)
@field_widget_adapter(zope.schema.interfaces.INativeString)
class TextReadWidget(base_widgets.ReadFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/read-text.html'

@field_widget_adapter(zope.schema.interfaces.ITextLine, qualifiers=['item'])
class TextAsItemReadWidget(base_widgets.ReadFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/read-text-item.html'

@field_widget_adapter(zope.schema.interfaces.ITextLine, qualifiers=['email'])
class EmailReadWidget(base_widgets.ReadFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/read-textline-email.html'

@field_widget_adapter(zope.schema.interfaces.IURI)
class UriReadWidget(base_widgets.ReadFieldWidget):
   
    def get_template(self):
        return 'package/snippets/fields/read-uri.html'

@field_widget_adapter(zope.schema.interfaces.IPassword)
class PasswordReadWidget(base_widgets.ReadFieldWidget):
   
    def get_template(self):
        return 'package/snippets/fields/read-password.html'

@field_widget_adapter(zope.schema.interfaces.IInt)
class IntReadWidget(base_widgets.ReadFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/read-int.html'

@field_widget_adapter(zope.schema.interfaces.IFloat)
class FloatReadWidget(base_widgets.ReadFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/read-float.html'

@field_widget_adapter(zope.schema.interfaces.IBool)
class BoolReadWidget(base_widgets.ReadFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/read-bool.html'

@field_widget_adapter(zope.schema.interfaces.IChoice)
class ChoiceReadWidget(base_widgets.ReadFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/read-choice.html'

@field_widget_adapter(zope.schema.interfaces.IDate)
class DateReadWidget(base_widgets.ReadFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/read-date.html'

@field_widget_adapter(zope.schema.interfaces.ITime)
class TimeReadWidget(base_widgets.ReadFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/read-time.html'

@field_widget_adapter(zope.schema.interfaces.IDatetime)
class DatetimeReadWidget(base_widgets.ReadFieldWidget):

    def get_template(self):
        return 'package/snippets/fields/read-datetime.html'

@field_widget_adapter(zope.schema.interfaces.IList)
@field_widget_adapter(zope.schema.interfaces.ITuple)
class ListReadWidget(base_widgets.ReadFieldWidget, base_widgets.ListFieldWidgetTraits):

    def __init__(self, field):
        assert \
            isinstance(field, zope.schema.List) or \
            isinstance(field, zope.schema.Tuple)
        base_widgets.ReadFieldWidget.__init__(self, field)

    def get_template(self):
        return 'package/snippets/fields/read-list.html'

@field_widget_multiadapter([zope.schema.interfaces.ITuple, zope.schema.interfaces.ITextLine], qualifiers=['tags'])
@field_widget_multiadapter([zope.schema.interfaces.IList, zope.schema.interfaces.ITextLine], qualifiers=['tags'])
class TagsReadWidget(base_widgets.ReadFieldWidget):

    def __init__(self, field, *args):
        assert isinstance(field, zope.schema.List)
        base_widgets.ReadFieldWidget.__init__(self, field)

    def get_template(self):
        return 'package/snippets/fields/read-list-tags.html'

@field_widget_adapter(zope.schema.interfaces.IDict)
class DictReadWidget(base_widgets.ReadFieldWidget, base_widgets.DictFieldWidgetTraits):

    def __init__(self, field):
        assert isinstance(field, zope.schema.Dict)
        base_widgets.ReadFieldWidget.__init__(self, field)

    def get_template(self):
        return 'package/snippets/fields/read-dict.html'

@field_widget_adapter(zope.schema.interfaces.IObject)
class ObjectReadWidget(base_widgets.ReadFieldWidget, base_widgets.ObjectFieldWidgetTraits):

    def __init__(self, field):
        assert isinstance(field, zope.schema.Object)
        base_widgets.ReadFieldWidget.__init__(self, field)
    
    def get_template(self):
        return 'package/snippets/fields/read-object.html'

