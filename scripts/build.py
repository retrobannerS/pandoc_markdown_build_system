import os
import shutil
import tomllib
from parser import write_yaml, write_template
from image_optimizer import optimize_images

# Change the current working directory to the root of the project
os.chdir(os.path.join(os.path.dirname(__file__), ".."))

# Recursively remove out directory and then create it again
shutil.rmtree("out", ignore_errors=True)
os.makedirs("out", exist_ok=True)

# Recursively remove temporary directory and then create it again
shutil.rmtree("tmp", ignore_errors=True)
os.makedirs("tmp", exist_ok=True)

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

if conf["project"]["latex"]:  # if latex project
    # Create void file and link out template
    with open("tmp/void.tex", "w") as file:
        pass
    os.system(
        f"pandoc tmp/void.tex -o tmp/raw_template.tex {' '.join(conf['pandoc']['args'])}"
    )

    # Parse our template
    preambles = [
        os.path.join("preambles", file) for file in conf["project"]["preambles"]
    ]
    write_template(preambles)

    # Move to separated folder
    shutil.rmtree("src/template", ignore_errors=True)
    os.makedirs("src/template", exist_ok=True)
    shutil.move("tmp/template.tex", "src/template/template.tex")
    shutil.move("tmp/titlepage.tex", "src/template/titlepage.tex")
    shutil.move("tmp/toc.tex", "src/template/toc.tex")

    # create main.tex if is does not exist
    if os.path.exists("src/main.tex"):
        None
    else:
        with open("src/main.tex", "w") as main:
            main.write("\\input{template/template.tex}\n\n")
            main.write("\\begin{document}\n")
            main.write("\t\\input{template/titlepage.tex}\n")
            main.write("\t\\input{template/toc.tex}\n")
            main.write("\t\n\t\n\t\n")
            main.write("\\end{document}\n")

else:  # if markdown project
    files = [os.path.join("src", file) for file in conf["pandoc"]["src"]]

    # Convert all markdown files in the src directory to a single PDF
    os.system(
        f"pandoc {' '.join(files)} -o out/{conf['pandoc']['out-name']} {' '.join(conf['pandoc']['args'])}"
    )


# Remove temporary directory
shutil.rmtree("tmp", ignore_errors=True)
