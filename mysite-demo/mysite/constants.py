NARROW = 'is-narrow'
STANDARD = 'standard'
WIDE = 'is-wide'
EXTRAWIDE = 'is-extra-wide'
FULLWIDTH = 'is-full-width'

WIDTH_STYLE_CHOICES = [
  (NARROW, 'narrow'),
  (STANDARD, 'standard'),
  (WIDE, 'wide'),
  (EXTRAWIDE, 'extra-wide'),
  (FULLWIDTH, 'full-width'),
]

TEXT = 'text'
IMAGETOP = 'image-top'

FORMAT_STYLE_CHOICES = [
  (TEXT, 'Text'),
  (IMAGETOP, 'Image Top'),
]

COL1 = 'columns-1'
COL2 = 'columns-2'
COL3 = 'columns-3'
COL4 = 'columns-4'

COLUMNS_STYLE_CHOICES = [
  (COL1, 'Columns 1'),
  (COL2, 'Columns 2'),
  (COL3, 'Columns 3'),
  (COL4, 'Columns 4'),
]

LEFT = 'has-image-on-left'
RIGHT = 'has-image-on-right'

IMAGE_ALIGNMENT_CHOICES = [
  (LEFT, 'left'),
  (RIGHT, 'right'),
]

COVER = 'image-cover'
CENTER = 'image-center'

IMAGE_SIZE_CHOICES = [
  (COVER, 'cover'),
  (CENTER, 'center'),
]