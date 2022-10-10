import pdfkit
import jinja2
from jinja2 import (
    Environment, 
    BaseLoader,
    FileSystemLoader
)


def imprimir_label(
    html_template,
    params,
    render_path,
    path_wkhtmltopdf="", 
    options={}
):
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    base_options = {
        'page-height': '1.5in',
        'page-width': '2.5in',
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'disable-smart-shrinking': ''
    }
    base_options.update(options)

    template = Environment(loader=BaseLoader).from_string(html_template)

    data = template.render(params)
    print(data)
    pdfkit.from_string(
        data, 
        render_path, 
        configuration = config, 
        options = base_options
    )

path_wkhtmltopdf = r'D:/gestor_2021_vite/utilitarios/wkhtmltopdf.exe'

file = open("label.html", "r")
html_template = file.read()
file.close()

def crear_parametros(nro_radicado):
    http = "http"
    ip   = "192.168.1.99"
    port = "9100"
    url = http + "://" + ip + ":" + port
    codigo_barras = url + "/codigo_barras/" + nro_radicado
    logo = url + "/logo_entidad"

    data_params = { 
        "nro_radicado": nro_radicado,
        "codigo_barras": codigo_barras,
        "logo": logo
    }

    return data_params

data_params = crear_parametros("E-2022-0120304")

imprimir_label(
    html_template,
    data_params, 
    'test.pdf', 
    path_wkhtmltopdf, 
    {}
)