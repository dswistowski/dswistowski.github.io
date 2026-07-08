
from pathlib import Path

import click
import yaml
from jinja2 import Environment, FileSystemLoader


env = Environment(
        loader=FileSystemLoader(Path(__file__).resolve().parent / "templates"),
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
@click.option(
    "--config",
    "config_path",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    default=Path("config.yaml"),
    show_default=True,
    help="YAML config used to render the CV.",
)
@click.option(
    "--output",
    "output_path",
    type=click.Path(dir_okay=False, path_type=Path),
    default=Path("latex/cv.tex"),
    show_default=True,
    help="Path where the rendered TeX file will be written.",
)
def latex(config_path, output_path):
    with config_path.open(encoding="utf-8") as config:
        config = yaml.safe_load(config)

    technology = config.get("technology") or {}
    config["technology_sections"] = [
        {"label": SECTION_LABELS[key], "items": values}
        for key, values in technology.items()
        if values
    ]

    click.echo(f"will generate `{output_path}`")
    template = env.get_template("cv.tex.j2")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as cv:
        cv.write(template.render(**config))


if __name__ == "__main__":
    cli()
