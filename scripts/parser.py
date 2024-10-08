import os
import yaml

def write_yaml(conf, path_yaml):
    # images directory for latex projects
    img_dir = os.path.join(".." if conf["project"]["latex"] else ".", "assets")
    
    with open(path_yaml, "w") as file:
        file.write(
            yaml.dump(
                {
                    # general
                    "title": conf["metadata"]["general"]["title"] if "title" in conf["metadata"]["general"] else None,
                    "subtitle": conf["metadata"]["general"]["subtitle"] if "subtitle" in conf["metadata"]["general"] else None,
                    "abstract": conf["metadata"]["general"]["abstract"] if "abstract" in conf["metadata"]["general"] else None,
                    "author": conf["metadata"]["general"]["author"] if "author" in conf["metadata"]["general"] else None,
                    "date": conf["metadata"]["general"]["date"] if "date" in conf["metadata"]["general"] else None,
                    "lang": conf["metadata"]["general"]["lang"] if "lang" in conf["metadata"]["general"] else None,

                    # layout
                    "block-headings": conf["metadata"]["layout"]["block-headings"] if "block-headings" in conf["metadata"]["layout"] else None,
                    "class-option": conf["metadata"]["layout"]["class-option"] if "class-option" in conf["metadata"]["layout"] else None,
                    "documentclass": conf["metadata"]["layout"]["documentclass"] if "documentclass" in conf["metadata"]["layout"] else None,
                    "geometry": conf["metadata"]["layout"]["geometry"] if "geometry" in conf["metadata"]["layout"] else None,
                    "hyperrefoptions": conf["metadata"]["layout"]["hyperrefoptions"] if "hyperrefoptions" in conf["metadata"]["layout"] else None,
                    "indent": conf["metadata"]["layout"]["indent"] if "indent" in conf["metadata"]["layout"] else None,
                    "linestretch": conf["metadata"]["layout"]["linestretch"] if "linestretch" in conf["metadata"]["layout"] else None,

                    "margin-left": conf["metadata"]["layout"]["margin-left"] if "margin-left" in conf["metadata"]["layout"] else None,
                    "margin-right": conf["metadata"]["layout"]["margin-right"] if "margin-right" in conf["metadata"]["layout"] else None,
                    "margin-top": conf["metadata"]["layout"]["margin-top"] if "margin-top" in conf["metadata"]["layout"] else None,
                    "margin-bottom": conf["metadata"]["layout"]["margin-bottom"] if "margin-bottom" in conf["metadata"]["layout"] else None,

                    "pagestyle": conf["metadata"]["layout"]["pagestyle"] if "pagestyle" in conf["metadata"]["layout"] else None,
                    "papersize": conf["metadata"]["layout"]["papersize"] if "papersize" in conf["metadata"]["layout"] else None,
                    "secnumdepth": conf["metadata"]["layout"]["secnumdepth"] if "secnumdepth" in conf["metadata"]["layout"] else None,
                    "beamerarticle": conf["metadata"]["layout"]["beamerarticle"] if "beamerarticle" in conf["metadata"]["layout"] else None,
                    "handoout": conf["metadata"]["layout"]["handoout"] if "handoout" in conf["metadata"]["layout"] else None,

                    # fonts
                    "fontenc": conf["metadata"]["fonts"]["fontenc"] if "fontenc" in conf["metadata"]["fonts"] else None,
                    "fontfamily": conf["metadata"]["fonts"]["fontfamily"] if "fontfamily" in conf["metadata"]["fonts"] else None,
                    "fontfamilyoptions": conf["metadata"]["fonts"]["fontfamilyoptions"] if "fontfamilyoptions" in conf["metadata"]["fonts"] else None,
                    "fontsize": conf["metadata"]["fonts"]["fontsize"] if "fontsize" in conf["metadata"]["fonts"] else None,

                    "mainfont": conf["metadata"]["fonts"]["mainfont"] if "mainfont" in conf["metadata"]["fonts"] else None,
                    "sansfont": conf["metadata"]["fonts"]["sansfont"] if "sansfont" in conf["metadata"]["fonts"] else None,
                    "monofont": conf["metadata"]["fonts"]["monofont"] if "monofont" in conf["metadata"]["fonts"] else None,
                    "mathfont": conf["metadata"]["fonts"]["mathfont"] if "mathfont" in conf["metadata"]["fonts"] else None,
                    "CJKmainfont": conf["metadata"]["fonts"]["CJKmainfont"] if "CJKmainfont" in conf["metadata"]["fonts"] else None,
                    "CJKsansfont": conf["metadata"]["fonts"]["CJKsansfont"] if "CJKsansfont" in conf["metadata"]["fonts"] else None,
                    "CJKmonofont": conf["metadata"]["fonts"]["CJKmonofont"] if "CJKmonofont" in conf["metadata"]["fonts"] else None,

                    "mainfontoptions": conf["metadata"]["fonts"]["mainfontoptions"] if "mainfontoptions" in conf["metadata"]["fonts"] else None,
                    "sansfontoptions": conf["metadata"]["fonts"]["sansfontoptions"] if "sansfontoptions" in conf["metadata"]["fonts"] else None,
                    "monofontoptions": conf["metadata"]["fonts"]["monofontoptions"] if "monofontoptions" in conf["metadata"]["fonts"] else None,
                    "mathfontoptions": conf["metadata"]["fonts"]["mathfontoptions"] if "mathfontoptions" in conf["metadata"]["fonts"] else None,
                    "CJKoptions": conf["metadata"]["fonts"]["CJKoptions"] if "CJKoptions" in conf["metadata"]["fonts"] else None,
                    "luatexjapresetoptions": conf["metadata"]["fonts"]["luatexjapresetoptions"] if "luatexjapresetoptions" in conf["metadata"]["fonts"] else None,

                    "mainfontfallback": conf["metadata"]["fonts"]["mainfontfallback"] if "mainfontfallback" in conf["metadata"]["fonts"] else None,
                    "sansfontfallback": conf["metadata"]["fonts"]["sansfontfallback"] if "sansfontfallback" in conf["metadata"]["fonts"] else None,
                    "monofontfallback": conf["metadata"]["fonts"]["monofontfallback"] if "monofontfallback" in conf["metadata"]["fonts"] else None,

                    "microtypeoptions": conf["metadata"]["fonts"]["microtypeoptions"] if "microtypeoptions" in conf["metadata"]["fonts"] else None,
                    "babelfonts": conf["metadata"]["fonts"]["babelfonts"] if "babelfonts" in conf["metadata"]["fonts"] else None,

                    # links
                    "colorlinks": conf["metadata"]["links"]["colorlinks"] if "colorlinks" in conf["metadata"]["links"] else None,
                    "boxlinks": conf["metadata"]["links"]["boxlinks"] if "boxlinks" in conf["metadata"]["links"] else None,
                    "linkcolor": conf["metadata"]["links"]["linkcolor"] if "linkcolor" in conf["metadata"]["links"] else None,
                    "filecolor": conf["metadata"]["links"]["filecolor"] if "filecolor" in conf["metadata"]["links"] else None,
                    "citecolor": conf["metadata"]["links"]["citecolor"] if "citecolor" in conf["metadata"]["links"] else None,
                    "urlcolor": conf["metadata"]["links"]["urlcolor"] if "urlcolor" in conf["metadata"]["links"] else None,
                    "toccolor": conf["metadata"]["links"]["toccolor"] if "toccolor" in conf["metadata"]["links"] else None,
                    "links-as-notes": conf["metadata"]["links"]["links-as-notes"] if "links-as-notes" in conf["metadata"]["links"] else None,
                    "urlstyle": conf["metadata"]["links"]["urlstyle"] if "urlstyle" in conf["metadata"]["links"] else None,

                    # frontmatter
                    "lof": conf["metadata"]["frontmatter"]["lof"] if "lof" in conf["metadata"]["frontmatter"] else None,
                    "lot": conf["metadata"]["frontmatter"]["lot"] if "lot" in conf["metadata"]["frontmatter"] else None,
                    "thanks": conf["metadata"]["frontmatter"]["thanks"] if "thanks" in conf["metadata"]["frontmatter"] else None,
                    "toc": conf["metadata"]["frontmatter"]["toc"] if "toc" in conf["metadata"]["frontmatter"] else None,
                    "toc-depth": conf["metadata"]["frontmatter"]["toc-depth"] if "toc-depth" in conf["metadata"]["frontmatter"] else None,

                    #bibliography
                    "biblatexoptions": conf["metadata"]["bibliography"]["biblatexoptions"] if "biblatexoptions" in conf["metadata"]["bibliography"] else None,
                    "biblio-style": conf["metadata"]["bibliography"]["biblio-style"] if "biblio-style" in conf["metadata"]["bibliography"] else None,
                    "biblio-title": conf["metadata"]["bibliography"]["biblio-title"] if "biblio-title" in conf["metadata"]["bibliography"] else None,
                    "bibliography": conf["metadata"]["bibliography"]["bibliography"] if "bibliography" in conf["metadata"]["bibliography"] else None,
                    "natbiboptions": conf["metadata"]["bibliography"]["natbiboptions"] if "natbiboptions" in conf["metadata"]["bibliography"] else None,

                    # titlepage
                    "titlepage": conf["metadata"]["template"]["titlepage"]["titlepage"] if "titlepage" in conf["metadata"]["template"]["titlepage"] else None,
                    "titlepage-color": conf["metadata"]["template"]["titlepage"]["titlepage-color"] if "titlepage-color" in conf["metadata"]["template"]["titlepage"] else None,
                    "titlepage-text-color": conf["metadata"]["template"]["titlepage"]["titlepage-text-color"] if "titlepage-text-color" in conf["metadata"]["template"]["titlepage"] else None,
                    "titlepage-rule-color": conf["metadata"]["template"]["titlepage"]["titlepage-rule-color"] if "titlepage-rule-color" in conf["metadata"]["template"]["titlepage"] else None,
                    "titlepage-rule-height": conf["metadata"]["template"]["titlepage"]["titlepage-rule-height"] if "titlepage-rule-height" in conf["metadata"]["template"]["titlepage"] else None,
                    "titlepage-background": (
                        os.path.join(
                            img_dir,
                            "title-page",
                            conf["metadata"]["template"]["titlepage"]["titlepage-background"],
                        )
                        if "titlepage-background" in conf["metadata"]["template"]["titlepage"]
                        else None
                    ),
                    "titlepage-logo": (
                        os.path.join(
                            img_dir,
                            "title-page", 
                            conf["metadata"]["template"]["titlepage"]["titlepage-logo"],
                        )
                        if "titlepage-logo" in conf["metadata"]["template"]["titlepage"]
                        else None
                    ),
                    "logo-width": conf["metadata"]["template"]["titlepage"]["logo-width"] if "logo-width" in conf["metadata"]["template"]["titlepage"] else None,

                    # page-background
                    "page-background": conf["metadata"]["template"]["page-background"]["page-background"] if "page-background" in conf["metadata"]["template"]["page-background"] else None,
                    "page-background-opacity": conf["metadata"]["template"]["page-background"]["page-background-opacity"] if "page-background-opacity" in conf["metadata"]["template"]["page-background"] else None,

                    # toc
                    "toc-own-page": conf["metadata"]["template"]["toc"]["toc-own-page"] if "toc-own-page" in conf["metadata"]["template"]["toc"] else None,

                    # figure
                    "float-placement-figure": conf["metadata"]["template"]["figure"]["float-placement-figure"] if "float-placement-figure" in conf["metadata"]["template"]["figure"] else None,

                    # table
                    "table-use-row-colors": conf["metadata"]["template"]["table"]["table-use-row-colors"] if "table-use-row-colors" in conf["metadata"]["template"]["table"] else None,

                    # listings
                    "listings-no-page-break": conf["metadata"]["template"]["listings"]["listings-no-page-break"] if "listings-no-page-break" in conf["metadata"]["template"]["listings"] else None,
                    "listings-disable-line-numbers": conf["metadata"]["template"]["listings"]["listings-disable-line-numbers"] if "listings-disable-line-numbers" in conf["metadata"]["template"]["listings"] else None,
                    "code-block-font-size": conf["metadata"]["template"]["listings"]["code-block-font-size"] if "code-block-font-size" in conf["metadata"]["template"]["listings"] else None,

                    # caption
                    "caption-justification": conf["metadata"]["template"]["caption"]["caption-justification"] if "caption-justification" in conf["metadata"]["template"]["caption"] else None,

                    # footnotes
                    "footnotes-pretty": conf["metadata"]["template"]["footnotes"]["footnotes-pretty"] if "footnotes-pretty" in conf["metadata"]["template"]["footnotes"] else None,
                    "footnotes-disable-backlinks": conf["metadata"]["template"]["footnotes"]["footnotes-disable-backlinks"] if "footnotes-disable-backlinks" in conf["metadata"]["template"]["footnotes"] else None,

                    # headerandfooter
                    "disable-header-and-footer": conf["metadata"]["template"]["headerandfooter"]["disable-header-and-footer"] if "disable-header-and-footer" in conf["metadata"]["template"]["headerandfooter"] else None,

                    # header
                    "header-left": conf["metadata"]["template"]["header"]["header-left"] if "header-left" in conf["metadata"]["template"]["header"] else None,
                    "header-center": conf["metadata"]["template"]["header"]["header-center"] if "header-center" in conf["metadata"]["template"]["header"] else None,
                    "header-right": conf["metadata"]["template"]["header"]["header-right"] if "header-right" in conf["metadata"]["template"]["header"] else None,

                    # footer
                    "footer-left": conf["metadata"]["template"]["footer"]["footer-left"] if "footer-left" in conf["metadata"]["template"]["footer"] else None,
                    "footer-center": conf["metadata"]["template"]["footer"]["footer-center"] if "footer-center" in conf["metadata"]["template"]["footer"] else None,
                    "footer-right": conf["metadata"]["template"]["footer"]["footer-right"] if "footer-right" in conf["metadata"]["template"]["footer"] else None,

                    # book
                    "book": conf["metadata"]["template"]["book"]["book"] if "book" in conf["metadata"]["template"]["book"] else None,
                    "first-chapter": conf["metadata"]["template"]["book"]["first-chapter"] if "first-chapter" in conf["metadata"]["template"]["book"] else None,                
                },
                allow_unicode=True,
                sort_keys=False,
            )
        )
        file.write(conf["metadata"]["latex"]["header-includes"])

def write_template(preambles):
    template_flag = True
    titlepage_flag = False
    toc_flag = False

    with open('tmp/raw_template.tex', 'r') as raw, open('tmp/template.tex', 'w') as template, open('tmp/titlepage.tex', 'w') as titlepage, open('tmp/toc.tex', 'w') as toc:
        for line in raw:
            if line.strip() == "\\begin{document}":
                template_flag = False
                continue

            if line.strip() == "%% begin titlepage":
                titlepage_flag = True
                continue

            if line.strip() == "%% end titlepage":
                titlepage_flag = False
                continue

            if line.strip() == "% \\maketitle":
                toc_flag = True
                continue

            if line.strip() == "\\end{document}":
                toc_flag = False
                break

            if template_flag: template.write(line)
            if titlepage_flag: titlepage.write(line)
            if toc_flag: toc.write(line)

    with open('tmp/template.tex', 'a') as template:          
        for preamble in preambles:
            template.write(f"%%\n%% begin {preamble}\n%%\n\n")
            with open(preamble, 'r') as preamble_file:
                for line in preamble_file:
                    template.write(line)
            template.write(f"\n\n%%\n%% end {preamble}\n%%\n\n")


