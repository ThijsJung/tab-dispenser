import os
import sys

import click
import jinja2
from yaml import load, Loader
import pdfkit

HTML_TEMPLATE_FILENAME = "template.html"
LYRICS_FILENAME = "lyrics.yaml"


def render_tab(song_id):
    # Collect template, lyrics & sheet music
    cwd = os.getcwd()
    tabs_dir = os.path.join(cwd, 'tabs.thijsjung.nl')
    song_template_file_path = os.path.join(tabs_dir, song_id, HTML_TEMPLATE_FILENAME)
    lyrics_file_path = os.path.join(tabs_dir, song_id, LYRICS_FILENAME)
    css_file_path = os.path.join(cwd, 'templates/style.css')
    rendered_file_dir = os.path.join(tabs_dir, 'rendered')

    # Get song template
    with open(song_template_file_path, 'r') as fh:
        song_template = fh.read()

    # Get lyrics
    with open(lyrics_file_path, "r") as fh:
        render_vars = load(fh, Loader=Loader)

    # Fill the templates with lyrics and sheetmusic
    # render_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(template_file_dir))
    render_environment = jinja2.Environment()
    output_text = render_environment.from_string(song_template).render(render_vars)

    # Save pdf
    # pdf_filename = os.path.join(rendered_file_dir, '{}.pdf'.format(song_id))
    # pdfkit.from_string(output_text, pdf_filename, css=css_file_path)

    # Save html
    html_filename = os.path.join(rendered_file_dir, '{}.html'.format(song_id))
    with open(html_filename, "w") as result_file:
        result_file.write(output_text)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Please provide a song ID")

    song_id = sys.argv[1]
    render_tab(song_id)