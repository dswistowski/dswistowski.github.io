
import click
import yaml
from jinja2 import Environment, FileSystemLoader


env = Environment(
        loader=FileSystemLoader("templates"),
        block_start_string="««",
        block_end_string="»»",
        variable_start_string="«",
        variable_end_string="»",
        comment_start_string="«#",
        comment_end_string="#»",
    )


@click.group()
def cli():
    pass


@cli.command()
def latex():
    with open("config.yaml") as config:
        config = yaml.safe_load(config)
    click.echo("ℹ️  will generate `cv.tex`")
    template = env.get_template("cv.tex.j2")

    with open("latex/cv.tex", "w") as cv:
        cv.write(template.render(**config))


if __name__ == "__main__":
    cli()
