from django.template import TemplateDoesNotExist, TemplateSyntaxError

from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy

import pystache
from pystache.common import TemplateNotFoundError

class Mustache(BaseEngine):

    app_dirname = 'mustache'

    def __init__(self, params):
        options = params.pop('OPTIONS').copy()
        super(Mustache, self).__init__(params)
        self.renderer = pystache.Renderer(
            search_dirs=self.template_dirs,
            file_extension=False,
        )

    def from_string(self, template_code):
        return Template(template_code)

    def get_template(self, template_name):
        try:
            return Template(self.renderer.load_template(template_name))
        except TemplateNotFoundError as exc:
            raise TemplateDoesNotExist(exc.args)

class Template(object):
    def __init__(self, template):
        self.template = template

    def render(self, context=None, request=None):
        if context is None:
            context = {}
        if request is not None:
            context['request'] = request
            context['csrf_input'] = csrf_input_lazy(request)
            context['csrf_token'] = csrf_token_lazy(request)
        return pystache.render(self.template, context)
