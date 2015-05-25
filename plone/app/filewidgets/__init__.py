from plone.app.z3cform.widget import BaseWidget
from z3c.form.browser.image import ImageWidget as BaseImageWidget
from plone.app.filewidgets.interfaces import IImageWidget
from zope.interface import implementsOnly
from zope.interface import implementer
from z3c.form.interfaces import IFieldWidget
from z3c.form.widget import FieldWidget

from plone.app.widgets.base import InputWidget


class ImageWidget(BaseWidget, BaseImageWidget):
    """RelatedItems widget for z3c.form."""

    _base = InputWidget

    implementsOnly(IImageWidget)

    pattern = 'imagewidget'
    pattern_options = BaseWidget.pattern_options.copy()

    def _base_args(self):
        args = super(ImageWidget, self)._base_args()
        args['type'] = 'file'
        return args


@implementer(IFieldWidget)
def ImageFieldWidget(field, request, extra=None):
    if extra is not None:
        request = extra
    return FieldWidget(field, ImageWidget(request))