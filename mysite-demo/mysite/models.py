from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from cms.models import CMSPlugin, Page

from djangocms_text_ckeditor.fields import HTMLField
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from .constants import *

class EditorPluginModel(CMSPlugin):
  width_style = models.CharField(
      max_length=15,
      choices=WIDTH_STYLE_CHOICES,
      default=STANDARD,
  )
  content = HTMLField(('Content'), blank=True, null=True)

class Editor2ColumnPluginModel(CMSPlugin):
  width_style = models.CharField(
      max_length=15,
      choices=WIDTH_STYLE_CHOICES,
      default=STANDARD,
  )
  content_left = HTMLField(('Content Left'), blank=True, null=True)
  content_right = HTMLField(('Content Right'), blank=True, null=True)

class Editor3ColumnPluginModel(CMSPlugin):
  width_style = models.CharField(
      max_length=15,
      choices=WIDTH_STYLE_CHOICES,
      default=STANDARD,
  )
  content_left = HTMLField(('Content Left'), blank=True, null=True)
  content_center = HTMLField(('Content Center'), blank=True, null=True)
  content_right = HTMLField(('Content Right'), blank=True, null=True)

class MediaTextPluginModel(CMSPlugin):
  width_style = models.CharField(
      max_length=15,
      choices=WIDTH_STYLE_CHOICES,
      default=STANDARD,
  )
  image_alignment = models.CharField(
      max_length=18,
      choices=IMAGE_ALIGNMENT_CHOICES,
      default=LEFT,
  )
  image_size = models.CharField(
      max_length=15,
      choices=IMAGE_SIZE_CHOICES,
      default=COVER,
  )
  image = ThumbnailerImageField(upload_to="images", blank=True)
  image_alt = models.CharField(max_length=20, blank=True)
  content = HTMLField(('Content'), blank=True, null=True)

class SidebarTextPluginModel(CMSPlugin):
  width_style = models.CharField(
      max_length=15,
      choices=WIDTH_STYLE_CHOICES,
      default=STANDARD,
  )
  content = HTMLField(('Content'), blank=True, null=True)

class SidebarCardsPluginModel(CMSPlugin):
  title = models.CharField(max_length=60)
  description = HTMLField(('Description'), blank=True, null=True)
  button_text = models.CharField(max_length=20, blank=True, null=True)
  button_url = models.URLField(null=True, blank=True)
  button_open_in_a_new_tab = models.BooleanField(default=False)
  button_two_text = models.CharField(max_length=20, blank=True, null=True)
  button_two_url = models.URLField(null=True, blank=True)
  button_two_open_in_a_new_tab = models.BooleanField(default=False)

class CallToActionPluginModel(CMSPlugin):
  header_title = models.CharField(max_length=60)
  header_description = models.CharField(max_length=65)
  header_button_text = models.CharField(max_length=20)
  header_button_url = models.URLField(null=True, blank=True)
  header_button_open_in_a_new_tab = models.BooleanField(default=False)
  header_image = ThumbnailerImageField(upload_to="images", blank=False)
  header_image_alt = models.CharField(max_length=20, blank=True)

class CardModel(CMSPlugin):
  card_image = ThumbnailerImageField(upload_to="images", blank=True)
  card_image_alt = models.CharField(max_length=20, blank=True)
  card_title = models.CharField(max_length=60)
  card_description = models.CharField(max_length=250, blank=True)
  card_button_text = models.CharField(max_length=30, blank=True, null=True)
  card_button_url = models.URLField(null=True, blank=True)
  card_button_open_in_a_new_tab = models.BooleanField(default=False)
  card_button_two_text = models.CharField(max_length=30, blank=True, null=True)
  card_button_two_url = models.URLField(null=True, blank=True)
  card_button_two_open_in_a_new_tab = models.BooleanField(default=False)
  card_content = HTMLField(('Content'), blank=True, null=True)

class CardGridModel(CMSPlugin):
  width_style = models.CharField(
      max_length=15,
      choices=WIDTH_STYLE_CHOICES,
      default=STANDARD,
  )

  format_style = models.CharField(
      max_length=15,
      choices=FORMAT_STYLE_CHOICES,
      default=TEXT,
  )

  columns_style = models.CharField(
    max_length=15,
    choices=COLUMNS_STYLE_CHOICES,
    default=COL1,
  )

class CoverPluginModel(CMSPlugin):
  width_style = models.CharField(
      max_length=15,
      choices= [
        (STANDARD, 'standard'),
        (FULLWIDTH, 'full-width'),
      ],
      default=STANDARD,
  )
  cover_background_image = FilerImageField(verbose_name=_('Upload Image'), blank=True, null=True, on_delete=models.SET_NULL, related_name='+')
  cover_button_text = models.CharField(max_length=30, blank=True, null=True)
  cover_button_url = models.URLField(null=True, blank=True)
  cover_button_open_in_a_new_tab = models.BooleanField(default=False)
  content = HTMLField(('Content'), blank=True, null=True)

class GalleryPluginModel(CMSPlugin):
  width_style = models.CharField(
    max_length=15,
    choices=WIDTH_STYLE_CHOICES,
    default=STANDARD,
  )

  columns_style = models.CharField(
    max_length=15,
    choices=COLUMNS_STYLE_CHOICES,
    default=COL1,
  )

class GalleryImagePluginModel(CMSPlugin):
  image = FilerImageField(
    verbose_name=_('Upload Image'),
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='+',
  )

class TestimoniesPluginModel(CMSPlugin):
  width_style = models.CharField(
      max_length=15,
      choices=WIDTH_STYLE_CHOICES,
      default=STANDARD,
  )

class TestimonyPluginModel(CMSPlugin):
  title = models.CharField(max_length=60)
  quote = models.TextField(max_length=950)
  job_title = models.CharField(max_length=50, blank=True, null=True)
  location = models.CharField(max_length=50)

class AnimatedBoxesPluginModel(CMSPlugin):
  width_style = models.CharField(
    max_length=15,
    choices=WIDTH_STYLE_CHOICES,
    default=STANDARD,
  )

class AnimatedBoxPluginModel(CMSPlugin):
  title = models.CharField(max_length=30)
  content = HTMLField(('Content'), blank=False, null=True)

class AccordionsPluginModel(CMSPlugin):
  width_style = models.CharField(
    max_length=15,
    choices=WIDTH_STYLE_CHOICES,
    default=STANDARD,
  )

class AccordionPluginModel(CMSPlugin):
  title = models.CharField(max_length=60)
  content = HTMLField(('Content'), blank=False, null=True)

class PriceCardPluginModel(CMSPlugin):
  image = ThumbnailerImageField(upload_to="images", blank=True)
  image_alt = models.CharField(max_length=20)
  content = HTMLField(('Content'), blank=True, null=True)
  price = models.CharField(max_length=20)
  button_text = models.CharField(max_length=20)
  button_url = models.URLField(null=True, blank=True)
  button_open_in_a_new_tab = models.BooleanField(default=False)

class HeaderStandardPluginModel(CMSPlugin):
  columns_style = models.CharField(
    max_length=15,
    choices=COLUMNS_STYLE_CHOICES,
    default=COL1,
  )
  header_title= models.CharField(max_length=50)

class HeaderStandardImagePluginModel(CMSPlugin):
  header_image = FilerImageField(
    verbose_name=_('Upload Image'),
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='+',
  )

class BlockquotesPluginModel(CMSPlugin):
  width_style = models.CharField(
     max_length=15,
     choices=WIDTH_STYLE_CHOICES,
     default=STANDARD,
  )

class BlockquotePluginModel(CMSPlugin):
  title = models.CharField(max_length=60)
  quote = models.TextField(max_length=950)
  job_title = models.CharField(max_length=50, blank=True, null=True)
  location = models.CharField(max_length=50, blank=True, null=True)


