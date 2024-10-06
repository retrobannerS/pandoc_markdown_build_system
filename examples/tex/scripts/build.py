import os
import shutil
import tomllib
import yaml

# Change the current working directory to the root of the project
os.chdir(os.path.join(os.path.dirname(__file__), ".."))

# Ensure ./out exists and is empty
os.makedirs("out", exist_ok=True)
for filename in os.listdir("out"):
    os.remove(os.path.join("out", filename))

# Recursively remove temporary directory and then create it again
shutil.rmtree("tmp", ignore_errors=True)
os.makedirs("tmp", exist_ok=True)

with open("build-conf.toml", "rb") as file:
    conf = tomllib.load(file)

with open("tmp/metadata.yaml", "w") as file:
    file.write(
        yaml.dump(
            {
                "title": conf["metadata"]["title"],
                "subtitle": conf["metadata"]["subtitle"],
                "author": conf["metadata"]["author"],
                "date": conf["metadata"]["date"],
                "geometry": conf["metadata"]["format"]["geometry"],
                "papersize": conf["metadata"]["format"]["papersize"],
                "lang": conf["metadata"]["lang"],
                "linkcolor": conf["metadata"]["format"]["linkcolor"],
                "toc-own-page": conf["metadata"]["format"]["toc-own-page"],
                "titlepage": conf["metadata"]["title-page"]["title-page"],
                "titlepage-background": (
                    os.path.join(
                        "assets",
                        "title-page",
                        conf["metadata"]["title-page"]["background"],
                    )
                    if "background" in conf["metadata"]["title-page"]
                    else None
                ),
                "titlepage-logo": (
                    os.path.join(
                        "assets",
                        "title-page",
                        conf["metadata"]["title-page"]["logo"],
                    )
                    if "logo" in conf["metadata"]["title-page"]
                    else None
                ),
                "logo-width": (
                    conf["metadata"]["title-page"]["logo-width"]
                    if "logo-width" in conf["metadata"]["title-page"]
                    else None
                ),
                "titlepage-rule-height": conf["metadata"]["title-page"]["rule-height"],
                "disable-header-and-footer": conf["metadata"]["format"][
                    "disable-header-and-footer"
                ],
                "block-headings": conf["metadata"]["format"]["block-headings"],
                "listings-no-page-break": conf["metadata"]["format"][
                    "listings-no-page-break"
                ],
                "caption-justification": conf["metadata"]["format"][
                    "caption-justification"
                ],
                "footnotes-pretty": conf["metadata"]["format"]["footnotes-pretty"],
                "book": conf["metadata"]["format"]["book"],
                "header-right": conf["metadata"]["format"]["header"]["right"],
                "header-left": conf["metadata"]["format"]["header"]["left"],
                "footer-left": conf["metadata"]["format"]["footer"]["left"],
                "footer-right": conf["metadata"]["format"]["footer"]["right"],
                "biblio-style": conf["metadata"]["latex"]["biblio-style"],
            },
            allow_unicode=True,
            sort_keys=False,
        )
    )
    file.write(conf["metadata"]["latex"]["header-includes"])

files = [os.path.join("src", file) for file in conf["pandoc"]["src"]]

# Convert all markdown files in the src directory to a single PDF
os.system(
    f"pandoc {' '.join(files)} -o out/{conf['pandoc']['out-name']} -t pdf {' '.join(conf['pandoc']['args'])}"
)


# Remove temporary directory
shutil.rmtree("tmp", ignore_errors=True)
