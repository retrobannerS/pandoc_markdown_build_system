# Система сборки MarkDown файлов, использующая Pandoc <!-- omit in toc -->

## Содержание <!-- omit in toc -->

- [Установка](#установка)
  - [Python](#python)
  - [Pandoc](#pandoc)
  - [TeXLive](#texlive)
    - [Unix](#unix)
    - [Mac OS](#mac-os)
    - [Windows](#windows)
    - [Необходимые библиотеки](#необходимые-библиотеки)
    - [Поддержка русского языка](#поддержка-русского-языка)
- [Настройка](#настройка)
- [Использование](#использование)
- [Пример](#пример)
- [Шаблоны](#шаблоны)
- [Фильтры Pandoc](#фильтры-pandoc)
- [Оптимизация изображений](#оптимизация-изображений)

## Установка

### Python

Установите [Python](https://www.python.org) для вашей операционной системы.

Все требуемые библиотеки для *Python* записаны в [requirements.txt](scripts/requirements.txt). Для установки нужно выполнить в терминале(находясь в папке с проектом) следующую команду:

```bash
pip install -r src/requirements.txt
```

### Pandoc

Установите [Pandoc](https://pandoc.org/getting-started.html) в соответствии с вашей операционной системой.

### TeXLive

Установите минимальную версию *TeXLive*, занимающую минимальное количество места на жестком диске:

#### Unix

Пример установки через пакетный менеджер для *Debian*/*Ubuntu*:

```bash
sudo apt install texlive-base
```

Для Arch Linux:

```bash
sudo pacman -S texlive-core
```

#### Mac OS

Через пакетный менеджер [Homebrew](https://brew.sh):

```bash
brew install --cask basictex
```

Или скачать и установить [BasicTeX.pkg](https://tug.org/mactex/morepackages.html).

#### Windows

Скачайте и зайдите в установщик [install-tl-windows.exe](https://tug.org/texlive/windows.html).
В установщике перейдите в Дополнительно(Advanced), выберите схему, занимающую минимальное место: схема только с инфраструктурой.

#### Необходимые библиотеки

Убедитесь, что *tlmgr* доступен в переменных окружения *PATH*, чтобы его можно было запустить из командной строки или *PowerShell*.

Все требуемые библиотеки для *TeXLive* записаны в [tex-requirements.txt](/tex_requirements.txt).

Для установки на *Unix*/*MacOS* необходимо выполнить следующую команду:

```bash
sudo xargs tlmgr install < path_to_project/tex_requirements.txt
```

Для *Windows* необходимо выполнить в *PowerShell*:

```powershell
Get-Content path_to_project/tex_requirements.txt | ForEach-Object { tlmgr install $_ }
```

не забудьте вместо `path_to_project` вставить путь до проекта.

#### Поддержка русского языка

На данный момент корректная поддержка русского языка доступна только для компилятора `XeLaTeX`.

## Настройка

Все настройки системы сборки находятся в конфигурационном файле [build-conf.toml](/build-conf.toml).
Для начала будет достаточно поменять название документа и автора в полях *title* и *author*.
Обо всех флагах в настройках можно почитать в [документации pandoc](https://pandoc.org/MANUAL.html) и [документации eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template/tree/master?tab=readme-ov-file#custom-template-variables).

Настройка титульной страницы производится [внутри шаблона](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/cf3c7ca2385296278566fb2539825b8f307be8fc/templates/eisvogel-custom.tex#L986C1-L1065C3).
Автор, дата и название документа могут вставляться автоматически из [metadata](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/ded753f9a8533638d43d701d4dcefb816eeff9af/build-conf.toml#L21C1-L27C12).

В файле [build-conf.toml](/build-conf.toml) есть некоторые настройки, которые нужно включать одновременно, то есть среди них есть зависимость:
| Настройка 1                                                                                                                                                     | Настройка 2                                                                                                                                                                                      | Примечание                                                                                                                                                         |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [image-optimization.enabled](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/4e4e5f5a815a5f62bb0d30f2c03904237eb89984/build-conf.toml#L2)     | pandoc argument: ["--lua-filter=filters/replace-image-path.lua"](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/4e4e5f5a815a5f62bb0d30f2c03904237eb89984/build-conf.toml#L15) | Оптимизированные изображения сохраняются в папку tmp, и, чтобы в исходниках писать путь к оригинальному изображению, lua-filter потом заменяет "assets/" на "tmp/" |
| pandoc argument: ["--citeproc"](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/4e4e5f5a815a5f62bb0d30f2c03904237eb89984/build-conf.toml#L17) | `bibliography`                                                                                                                                                                                   | нужен файл с библиографией, чтобы обрабатывать цитирования                                                                                                         |
| [documentclass](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/4e4e5f5a815a5f62bb0d30f2c03904237eb89984/build-conf.toml#L35)                 | [book](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/4e4e5f5a815a5f62bb0d30f2c03904237eb89984/build-conf.toml#L164)                                                          | если `documentclass` не `article`, то нужно включить `book` чтобы правильно распознавать заголовки вида `chapter`                                                  |

## Использование

1. В папке **/src** располагаются файлы в формате *markdown*.
2. *Python* скрипт [build.py](/scripts/build.py) формирует временный файл **metadata.yaml** из настроек в конфигурационном файле [build-conf.toml](/build-conf.toml).
3. Выполняется **bash** команда, создающая выходной файл.

Для соединения в единый PDF файл используется утилита [pandoc](https://pandoc.org/index.html),которая переводит *markdown* файлы в единый *.tex* файл, добавляет к нему шаблон и настройки и формирует единый PDF.

Для конвертирования исходников в один PDF файл достаточно в конфигурационном файле [build-conf.toml](/build-conf.toml) сделать следующие изменения:

- Написать список [исходных файлов](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/b6f20ad9705f2a0121f4a6074b35cc94c12a4a3e/build-conf.toml#L18), которые будут входить в PDF.
- Написать имя [итогового файла](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/b6f20ad9705f2a0121f4a6074b35cc94c12a4a3e/build-conf.toml#L18). Формат выходящего файла важен.

Запуск *Python* скрипта создает выходной PDF:

```bash
python3 ./scripts/build.py
```

Папка **example** и файлы:

- [README.md](/README.md)
- [title-page-01.jpg](/title-page-01.jpg)
- [title-page-02.jpg](/title-page-02.jpg)
- [example1.jpg](/example1.jpg)
- [example2.jpg](/example12.jpg)
- [example3.jpg](/example3.jpg)
- [example4.jpg](/example4.jpg)

независимы и могут быть удалены для личного использования этого проекта.

## Пример

В корневой папке вы можете встретить **example** - пример сборки файлов в один PDF.

| [![](/example1.jpg)](/example1.jpg) | [![](/example2.jpg)](/example2.jpg) |
| ----------------------------------- | ----------------------------------- |
| [![](/example3.jpg)](/example3.jpg) | [![](/example4.jpg)](/example4.jpg) |

## Шаблоны

В проекте приведены два шаблона, основанные на шаблоне [eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template/tree/master?tab=readme-ov-file#custom-template-variables).

[*eisvogel-custom.tex:*](/templates/eisvogel-custom.tex)

- [Можно использовать любой `documentclass` из списка `scrartcl, scrbook, scrreprt`.](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/cf3c7ca2385296278566fb2539825b8f307be8fc/templates/eisvogel-custom.tex#L76)
- Адаптирован для русского языка. [Здесь](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/cf3c7ca2385296278566fb2539825b8f307be8fc/templates/eisvogel-custom.tex#L836C3-L837C27) и [здесь](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/cf3c7ca2385296278566fb2539825b8f307be8fc/templates/eisvogel-custom.tex#L873C3-L884C32).
- [Добавлена переменная цвета подписей к картинкам/таблицам.](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/cf3c7ca2385296278566fb2539825b8f307be8fc/templates/eisvogel-custom.tex#L683C1-L683C89)
- [Добавлена переменная использования **metadata** на титульной странице.](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/cf3c7ca2385296278566fb2539825b8f307be8fc/templates/eisvogel-custom.tex#L1017C9-L1017C31)

[*eisvogel-custom_mephi_titlepage.tex*](/templates/eisvogel-custom_mephi_titlepage.tex)
отличается от [*eisvogel-custom.tex:*](/templates/eisvogel-custom.tex)

- Добавлена [титульная страница](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/cf3c7ca2385296278566fb2539825b8f307be8fc/templates/eisvogel-custom_mephi_titlepage.tex#L1031C5-L1069C8) - пародия на ГОСТ:

| Без логотипа                                  | С логотипом                                  |
| --------------------------------------------- | -------------------------------------------- |
| [![титульник без логотипа](/title-page-01.jpg)](/title-page-01.jpg) | [![титульник с логотипом](/title-page-02.jpg)](/title-page-02.jpg) |

## Фильтры Pandoc

<u>[Документация.](https://pandoc.org/filters.html)</u>

*Pandoc* умеет работать с разными фильтрами, но сам рекомендует использовать *Lua-Filters*, так как в этом случае получается нативная работа.

Пайплайн работы *Pandoc*: file $\longrightarrow$ AST(абстрактное синтаксическое дерево) $\longrightarrow$ обработка фильтром $\longrightarrow$ преобразование в tex $\longrightarrow$ применение шаблона $\longrightarrow$ преобразование в целевой формат. То есть фильтр проходится по дереву и в соответствии с запрограммированными правилами изменяет в нем элементы.

В шаблон уже встроены некоторые фильтры, которые можно включать и выключать в конфигурационном файле [build-conf.toml](/build-conf.toml).

## Оптимизация изображений

Когда в исходниках набирается достаточное количество изображений(особенно тяжеловесных формата `PNG`), то выходной файл формата `PDF` компилируется достаточно долгое время. Для решения этой проблемы есть опция [image-optimization](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/4e4e5f5a815a5f62bb0d30f2c03904237eb89984/build-conf.toml#L1) в конфигурационном файле [build-conf.toml](/build-conf.toml).

Если параметр `enabled` включен, то любое изображение формата `.png`, `.jpg` или `.jpeg` из папки **assets/images** будет приведено к формату `.jpg` в соответствии указанным качеством изображения `quality` (в пределах `1-100`) и максимальным разрешением по одной из сторон `max-size`(в `пикселях`).

Например, изображение формата `.png` с разрешением `3000x2000` при параметре `max-size = 1500` будет сохранено в формате  `.jpg` с разрешением `1500x1000`.
Другой пример, изображение  формата `.png` с разрешением `1000x500` при параметре `max-size = 1500` будет сохранено в формате  `.jpg` с разрешением `1000x500`.
Пропорция разрешения сохраняется, но при слишком больших значениях оно приводится к `max-size` по бОльшей из сторон.

Оптимизированные изображения сохраняются в директорию **tmp/images**. Lua-filter [replace-image-path.lua](/filters/replace-image-path.lua), если он включен, при формировании `PDF` заменит все вхождения `assets/images` и `./assets/images` на `tmp/images`.

Например,

```markdown
![title][assets/images/dogs/1.png]
```

в процессе компиляции заменится на

```markdown
![title][tmp/images/dogs/1.png]
```

автоматически, поэтому в исходных файлах можно пользоваться привычными путями до ваших оригинальных, еще не оптимизированных изображений.
