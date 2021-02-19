from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import (EditorPluginModel, Editor2ColumnPluginModel, Editor3ColumnPluginModel, MediaTextPluginModel, SidebarTextPluginModel, SidebarCardsPluginModel, CallToActionPluginModel, CardModel, CardGridModel, CoverPluginModel,
GalleryPluginModel, GalleryImagePluginModel, TestimoniesPluginModel, TestimonyPluginModel, AnimatedBoxesPluginModel, AnimatedBoxPluginModel, AccordionsPluginModel, AccordionPluginModel, PriceCardPluginModel, HeaderStandardPluginModel,
                     HeaderStandardImagePluginModel,BlockquotesPluginModel,BlockquotePluginModel)

@plugin_pool.register_plugin  # register the plugin
class EditorPublisher(CMSPluginBase):
    model = EditorPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Editor")  # name of the plugin in the interface
    render_template = "sections/article/editor_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class Editor2ColumnPublisher(CMSPluginBase):
    model = Editor2ColumnPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("2 Column Editor")  # name of the plugin in the interface
    render_template = "sections/article/editor_2_column_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class Editor3ColumnPublisher(CMSPluginBase):
    model = Editor3ColumnPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("3 Column Editor")  # name of the plugin in the interface
    render_template = "sections/article/editor_3_column_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class MediaTextPublisher(CMSPluginBase):
    model = MediaTextPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Media + Text")  # name of the plugin in the interface
    render_template = "sections/article/media_text_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class SidebarTextPublisher(CMSPluginBase):
    model = SidebarTextPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Text + Sidebar")  # name of the plugin in the interface
    render_template = "sections/article/sidebar_text_plugin.html"
    allow_children = True
    child_classes = ['SidebarCardsPublisher']
    max_children = 2

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class SidebarCardsPublisher(CMSPluginBase):
    model = SidebarCardsPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Sidebar Cards")  # name of the plugin in the interface
    render_template = "sections/article/sidebar_card_plugin.html"
    require_parent = True
    parent_classes = ['SidebarTextPublisher']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class CallToActionPublisher(CMSPluginBase):
    model = CallToActionPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Header Call To Action")  # name of the plugin in the interface
    render_template = "sections/action_header_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class GridPublisher(CMSPluginBase):
  model = CardGridModel  # model where plugin data are saved
  module = _("mysite Components")
  name = _("Card Grid")  # name of the plugin in the interface
  render_template = "sections/article/card_grid_plugin.html"
  allow_children = True
  max_children = 3
  child_classes = [
    'cardPublisher',
  ]

  def render(self, context, instance, placeholder):
    context.update({'instance': instance})
    return context

@plugin_pool.register_plugin  # register the plugin
class cardPublisher(CMSPluginBase):
  model = CardModel  # model where plugin data are saved
  module = _("mysite Components")
  name = _("Card")  # name of the plugin in the interface
  render_template = "sections/article/card_plugin.html"
  require_parent = True
  parent_classes = [
    'GridPublisher'
  ]

  fieldsets = [
    (None, {
        'fields': (
            'card_title',
            'card_description',
            ('card_button_text', 'card_button_url','card_button_open_in_a_new_tab'),
            ('card_button_two_text','card_button_two_url','card_button_two_open_in_a_new_tab'),
        )
    }),
    (_('Image Top'), {
      'classes': ('collapse',),
        'fields': (
            'card_content',
            'card_image',
            'card_image_alt',
        )
    }),
  ]

  def render(self, context, instance, placeholder):
    context.update({'instance': instance})
    return context

@plugin_pool.register_plugin  # register the plugin
class CoverPublisher(CMSPluginBase):
    model = CoverPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Cover")  # name of the plugin in the interface
    render_template = "sections/article/cover_plugin.html"

    fieldsets = [
      (None, {
          'fields': (
              'width_style',
              'content',
              'cover_button_text',
              'cover_button_url',
              'cover_button_open_in_a_new_tab',
          )
      }),
      (_('Full Width'), {
        'classes': ('collapse',),
          'fields': (
              'cover_background_image',
          )
      }),
    ]

    def render(self, context, instance, placeholder):
      context.update({'instance': instance})
      return context

@plugin_pool.register_plugin  # register the plugin
class GalleryPublisher(CMSPluginBase):
    model = GalleryPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Gallery")  # name of the plugin in the interface
    render_template = "sections/article/gallery_plugin.html"
    allow_children = True
    child_classes = ['GalleryImagePublisher']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class GalleryImagePublisher(CMSPluginBase):
    model = GalleryImagePluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Image")  # name of the plugin in the interface
    render_template = "sections/article/image_plugin.html"
    require_parent = True
    parent_classes = ['GalleryPublisher']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class TestimoniesPublisher(CMSPluginBase):
    model = TestimoniesPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Testimonies")  # name of the plugin in the interface
    render_template = "sections/article/testimonies_plugin.html"
    allow_children = True
    max_children = 3
    child_classes = [
      'TestimonyPublisher',
    ]

    def render(self, context, instance, placeholder):
      context.update({'instance': instance})
      return context

@plugin_pool.register_plugin  # register the plugin
class TestimonyPublisher(CMSPluginBase):
    require_parent = True
    parent_classes = [
      'TestimoniesPublisher'
    ]
    model = TestimonyPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Testimony")  # name of the plugin in the interface
    render_template = "sections/article/testimony_card_plugin.html"

    def render(self, context, instance, placeholder):
      context.update({'instance': instance})
      return context

@plugin_pool.register_plugin  # register the plugin
class AnimatedBoxesPublisher(CMSPluginBase):
    model = AnimatedBoxesPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Animated Boxes")  # name of the plugin in the interface
    render_template = "sections/article/animated_boxes_plugin.html"
    allow_children = True
    child_classes = ['AnimatedBoxPublisher']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class AnimatedBoxPublisher(CMSPluginBase):
    model = AnimatedBoxPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Animated Box")  # name of the plugin in the interface
    render_template = "sections/article/animated_box_plugin.html"
    require_parent = True
    parent_classes = ['AnimatedBoxesPublisher']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class AccordionsPublisher(CMSPluginBase):
    model = AccordionsPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Accordions")  # name of the plugin in the interface
    render_template = "sections/article/accordions_plugin.html"
    allow_children = True
    child_classes = ['AccordionPublisher']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class AccordionPublisher(CMSPluginBase):
    model = AccordionPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Accordion")  # name of the plugin in the interface
    render_template = "sections/article/accordion_plugin.html"
    require_parent = True
    parent_classes = ['AccordionsPublisher']

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

@plugin_pool.register_plugin  # register the plugin
class PriceCardPublisher(CMSPluginBase):
    model = PriceCardPluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = ("Price Card")  # name of the plugin in the interface
    render_template = "sections/article/price_card_plugin.html"

    def render(self, context, instance, placeholder):
      context.update({'instance': instance})
      return context


@plugin_pool.register_plugin  # register the plugin
class HeaderStandardPublisher(CMSPluginBase):
  model = HeaderStandardPluginModel  # model where plugin data are saved
  module = _("mysite Components")
  name = _("Header Standard")  # name of the plugin in the interface
  render_template = "sections/header_standard_plugin.html"
  allow_children = True
  max_children = 3
  child_classes = [
    'HeaderStandardImagePublisher',
  ]

  def render(self, context, instance, placeholder):
    context.update({'instance': instance})
    return context

@plugin_pool.register_plugin  # register the plugin
class HeaderStandardImagePublisher(CMSPluginBase):
    model = HeaderStandardImagePluginModel  # model where plugin data are saved
    module = _("mysite Components")
    name = _("Header Standard Image")  # name of the plugin in the interface
    render_template = "sections/header_standard_child_plugin.html"
    require_parent = True
    parent_classes = ['HeaderStandardPublisher']

    def render(self, context, instance, placeholder):
      context.update({'instance': instance})
      return context

@plugin_pool.register_plugin  # register the plugin
class BlockquotesPublisher(CMSPluginBase):
  model = BlockquotesPluginModel  # model where plugin data are saved
  module = _("mysite Components")
  name = _("Blockquotes")  # name of the plugin in the interface
  render_template = "sections/article/blockquote_plugin.html"
  allow_children = True
  child_classes = [
    'BlockquotePublisher'
  ]

  def render(self, context, instance, placeholder):
      context.update({'instance': instance})
      return context

@plugin_pool.register_plugin  # register the plugin
class BlockquotePublisher(CMSPluginBase):
  model = BlockquotePluginModel  # model where plugin data are saved
  module = _("mysite Components")
  name = _("Blockquote")  # name of the plugin in the interface
  render_template = "sections/article/blockquote_plugin_child.html"
  require_parent = True
  parent_classes = ['BlockquotesPublisher']

  def render(self, context, instance, placeholder):
   context.update({'instance': instance})
   return context
