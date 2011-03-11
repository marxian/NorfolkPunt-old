from imagekit.specs import ImageSpec
from imagekit import processors

# first we define our thumbnail resize processor
class ResizeThumb(processors.Resize):
    width = 100
    height = 75
    crop = True

# now we define a display size resize processor
class ResizeDisplay(processors.Resize):
    width = 600

# now let's create an adjustment processor to enhance the image at small sizes
class EnhanceThumb(processors.Adjustment):
    contrast = 1.2
    sharpness = 1.1

# make a greyscaler
class Greyscale(processors.Adjustment):
    color = 0.0

# now we can define our thumbnail spec
class Thumbnail(ImageSpec):
    access_as = 'thumbnail'
    pre_cache = True
    processors = [ResizeThumb, EnhanceThumb]

# and our display spec
class Display(ImageSpec):
    pre_cache = True
    processors = [ResizeDisplay]
    
class GreyscaleThumbnail(ImageSpec):
    access_as = 'thumbnail_bw'
    pre_cache = True
    processors = [ResizeThumb, Greyscale, EnhanceThumb]
