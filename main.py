from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from scripts import get_company_age, get_categories_with_wines, get_company_with_us


company_age = get_company_with_us(get_company_age())

categories_with_wines = get_categories_with_wines('example.xlsx')
images_address = 'images/'

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

rendered_page = template.render(
    company_age=company_age,
    categories_wine=categories_with_wines,
    images_address=images_address,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)


server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
