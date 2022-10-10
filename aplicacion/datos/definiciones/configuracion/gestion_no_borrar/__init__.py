#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

import os
os.environ["NLS_LANG"] = "AMERICAN_AMERICA.AL32UTF8"

from .databases_general               import *
from .databases_usuario               import *
from .databases_geografia             import *
from .databases_remitentes            import *
from .databases_archivos_electronicos import *
from .databases_temas_subtemas        import *
from .databases_plantillas            import *
from .databases_roles                 import *
from .databases_ubicaciones           import *
from .databases_grupo                 import *
from .databases_dependencia           import *
from .databases_virtuales             import *