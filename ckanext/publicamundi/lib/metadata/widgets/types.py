import zope.interface

from ckanext.publicamundi.lib.metadata import schemata
from ckanext.publicamundi.lib.metadata import types
from ckanext.publicamundi.lib.metadata import adapter_registry
from ckanext.publicamundi.lib.metadata.widgets.ibase import IObjectWidget
from ckanext.publicamundi.lib.metadata.widgets import base as base_widgets

## Define widgets ##

class PointEditWidget(base_widgets.EditObjectWidget):

    def get_template(self):
        return 'package/snippets/objects/edit-point.html'

class PointReadWidget(base_widgets.ReadObjectWidget):

    def get_template(self):
        return 'package/snippets/objects/read-point.html'

## Register adapters ##

def register_object_widget(object_iface, widget_cls):
    adapter_registry.register(
        [object_iface], IObjectWidget, widget_cls.action, widget_cls)

default_widgets = [
    (schemata.IPoint, PointReadWidget),
    (schemata.IPoint, PointEditWidget),
]

for object_iface, widget_cls in default_widgets:
    register_object_widget(object_iface, widget_cls)

