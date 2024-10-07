import os
import shutil
import tomllib
from parser import write_yaml

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

write_yaml(conf, "tmp/metadata.yaml")

files = [os.path.join("src", file) for file in conf["pandoc"]["src"]]

# Convert all markdown files in the src directory to a single PDF
os.system(
    f"pandoc {' '.join(files)} -o out/{conf['pandoc']['out-name']} -t pdf {' '.join(conf['pandoc']['args'])}"
)


# Remove temporary directory
shutil.rmtree("tmp", ignore_errors=True)
