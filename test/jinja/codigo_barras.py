import os
import uuid

import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from PIL import Image
from PIL import ImageDraw

import tempfile
  
def _paint_text(self, xpos, ypos):
    pass

def _init(self, code):
    size = (420, 200)
    self._image = Image.new(self.mode, size, self.background)
    self._draw = ImageDraw.Draw(self._image)

ImageWriter._paint_text = _paint_text
ImageWriter._init = _init

directorio_temporal = tempfile.gettempdir() + os.path.sep
def codigo_barras(texto):
    nombre_unico = directorio_temporal + str(uuid.uuid4())
    code128 = barcode.get_barcode_class('code128')
    writer = ImageWriter()
    my_ean = code128(texto, writer=writer)
    fullname = my_ean.save(nombre_unico)
    fp = BytesIO()
    my_ean.write(fp)

    return fullname

print(codigo_barras("E-2022-005678"))