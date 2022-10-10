import pdfkit
import jinja2
from jinja2 import (
    Environment, 
    BaseLoader
)


path_wkhtmltopdf = r'D:/gestor_2021_vite/utilitarios/wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

options = {
    'page-height': '1in',
    'page-width': '1in',
    'margin-top': '0.00in',
    'margin-right': '0.00in',
    'margin-bottom': '0.00in',
    'margin-left': '0in',
    'encoding': "UTF-8",
    'disable-smart-shrinking': ''
}

html_template = """
<!DOCTYPE html>
<style>
div.rectangle {
  font-family: Courier New, monospace;
}
</style>
<html>
    <head></head>
    <body>
        <div class="rectangle">
        {{ nombre }}
        </div>
        <img src="file:///arquitectura.png" alt="logo" />
    </body>
</html>
"""

template = Environment(loader=BaseLoader).from_string(html_template)
data = template.render({ "nombre": "paola" })
print(data)

# outputText = template.render({})
# html_file = open(str(int(d['interest_rate'] * 100)) + '.html', 'w')
# html_file.write(outputText)
# html_file.close()
pdfkit.from_string(data, 'test.pdf', configuration = config, options = options)#
