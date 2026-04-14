
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


LATEX_ESCAPE_TABLE = str.maketrans({
    "\\": r"\textbackslash{}",
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
})


SECTION_LABELS = {
    "languages": "Languages",
    "backend": "Backend",
    "data_storage": "Data & Storage",
    "cloud_infra": "Cloud & Infrastructure",
    "workflow_data_processing": "Workflow & Data Processing",
    "other": "Other",
}


def tex_escape(value):
    if value is None:
        return ""
    return str(value).translate(LATEX_ESCAPE_TABLE)


def bullet_join(values):
    return r" \textbar\ ".join(tex_escape(value) for value in values)


env.filters["tex_escape"] = tex_escape
env.filters["bullet_join"] = bullet_join


@click.group()
def cli():
    pass


@cli.command()
def latex():
    with open("config.yaml") as config:
        config = yaml.safe_load(config)

    technology = config.get("technology") or {}
    config["technology_sections"] = [
        {"label": SECTION_LABELS[key], "items": values}
        for key, values in technology.items()
        if values
    ]

    click.echo("ℹ️  will generate `cv.tex`")
    template = env.get_template("cv.tex.j2")

    with open("latex/cv.tex", "w") as cv:
        cv.write(template.render(**config))


if __name__ == "__main__":
    cli()
