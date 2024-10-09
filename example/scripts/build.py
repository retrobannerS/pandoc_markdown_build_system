import os
import shutil
import tomllib
from conf_parser import write_yaml
from image_optimizer import optimize_images

# Change the current working directory to the root of the project
os.chdir(os.path.join(os.path.dirname(__file__), ".."))

# Recursively remove out directory and then create it again
shutil.rmtree("out", ignore_errors=True)
os.makedirs("out", exist_ok=True)

# Recursively remove temporary directory and then create it again
shutil.rmtree("tmp", ignore_errors=True)
os.makedirs("tmp", exist_ok=True)

# Convert configuration to metadata
with open("build-conf.toml", "rb") as file:
    conf = tomllib.load(file)

write_yaml(conf, "tmp/metadata.yaml")

# Optimize images
if conf["image-optimization"]["enabled"]:
    optimize_images(
        "assets/images",
        "tmp/images",
        conf["image-optimization"]["quality"],
        conf["image-optimization"]["max-size"],
    )

# Convert all markdown files in the src directory to a single file(e.g. PDF)
files = [os.path.join("src", file) for file in conf["pandoc"]["src"]]

os.system(
    f"pandoc {' '.join(files)} -o out/{conf['pandoc']['out-name']} {' '.join(conf['pandoc']['args'])}"
)

# Remove temporary directory
shutil.rmtree("tmp", ignore_errors=True)
