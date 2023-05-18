from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from scripts import get_company_age, get_categories_with_wines, create_company_age_string
import environs
import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        description='Сайт магазина авторского вина "Новое русское вино"')
    parser.add_argument('--path', '-p', help='Path to xlsx file, default: %(default)s',
                        default='example.xlsx')
    parser.add_argument('--images_path', '-ip', help='Path to images, default: %(default)s',
                        default='images/')
    return parser


def main():
    environs.Env().read_env()
    company_age = create_company_age_string(get_company_age())
    parser = create_parser()
    args = parser.parse_args()
    images_address = environs.Env().str('PATH_TO_IMAGES', default=args.images_path)
    path = environs.Env().str('PATH_TO_XLSX', default=args.path)
    categories_wine = get_categories_with_wines(path)
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        company_age=company_age,
        categories_wine=categories_wine,
        images_address=images_address,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
