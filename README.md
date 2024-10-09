# Универсальный шаблон для написания документов и конспектов <!-- omit in toc -->

## Table of Content <!-- omit in toc -->

- [Установка](#установка)
  - [Python](#python)
  - [Pandoc](#pandoc)
  - [TeXLive](#texlive)
    - [Unix](#unix)
    - [Mac OS](#mac-os)
    - [Windows](#windows)
    - [Необходимые библиотеки](#необходимые-библиотеки)
- [Настройка](#настройка)
- [Использование](#использование)
- [Пример](#пример)
- [Шаблоны](#шаблоны)
- [Фильтры Pandoc](#фильтры-pandoc)
- [image optimizer](#image-optimizer)

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

не забудьте вместо ```path_to_project``` вставить путь до проекта.

## Настройка

Все настройки системы сборки находятся в конфигурационном файле [build-conf.toml](/build-conf.toml).
Для начала будет достаточно поменять название документа и автора в полях *title* и *author*.
Обо всех флагах в настройказ можно почитать в [документации pandoc](https://pandoc.org/MANUAL.html) и [документации eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template/tree/master?tab=readme-ov-file#custom-template-variables).

Настройка титульной страницы производится [внутри шаблона](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/ded753f9a8533638d43d701d4dcefb816eeff9af/templates/eisvogel-custom.tex#L934C1-L1014C1).
Автор, дата и название документа могут вставляться автоматически из [metadata](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/ded753f9a8533638d43d701d4dcefb816eeff9af/build-conf.toml#L21C1-L27C12).

## Использование

1. В папке **/src** располагаются файлы в формате *markdown*. 
2. *Python* скрипт [build.py](/scripts/build.py) формирует временный файл **metadata.yaml** из настроек в конфигурационном файле [build-conf.toml](/build-conf.toml).
3. Выполняется **bash** команда, создающая выходной файл.

Для соединения в единый PDF файл используется утилита [pandoc](https://pandoc.org/index.html),которая переводит *markdown* файлы в единый *.tex* файл, добавляет к нему шаблон и настройки и формирует единый PDF.

Для конвертирования исходников в один PDF файл достаточно в конфигурационном файле [build-conf.toml](/build-conf.toml) сделать следующие изменения:

- Написать список [исходных файлов](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/b6f20ad9705f2a0121f4a6074b35cc94c12a4a3e/build-conf.toml#L18), которые будут входить в PDF.
- Написать имя [выходящего файла](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/b6f20ad9705f2a0121f4a6074b35cc94c12a4a3e/build-conf.toml#L18). Формат выходящего файла важен.

Запуск *Python* скрипта создает выходной PDF:

```bash
python3 ./scripts/build.py
```

Папка **example** и файлы [README.md](/README.md), [title-page-01.jpg](/title-page-01.jpg) и [title-page-02.jpg](/title-page-02.jpg) независимы и могут быть удалены для личного использования этого проекта.

## Пример

В корневой папке вы можете встретить **example** - пример сборки файлов в один PDF.

| ![](/example1.jpg) | ![](/example2.jpg) |
| ------------------ | ------------------ |
| ![](/example3.jpg) | ![](/example4.jpg) |

## Шаблоны

В проекте приведены два шаблона, основанные на шаблоне [eisvogel](https://github.com/Wandmalfarbe/pandoc-latex-template/tree/master?tab=readme-ov-file#custom-template-variables).

[*eisvogel-custom.tex:*](/templates/eisvogel-custom.tex)
- [Можно использовать любой ```documentclass``` из списка ```scrartcl, scrbook, scrreprt```.](https://github.com/retrobannerS/pandoc_markdown_build_system/blob/b6f20ad9705f2a0121f4a6074b35cc94c12a4a3e/templates/eisvogel-custom.tex#L73C1-L73C99)
- Адаптирован для русского языка.
- Добавлена переменная цвета подписей к картинкам/таблицам.
- Добавлена переменная использования **metadata** на титульной странице.

[*eisvogel-custom_mephi_titlepage.tex*](/templates/eisvogel-custom_mephi_titlepage.tex)
отличается от [*eisvogel-custom.tex:*](/templates/eisvogel-custom.tex)
- Добавлена титульная страница - пародия на ГОСТ:

| Без логотипа                                  | С логотипом                                  |
| --------------------------------------------- | -------------------------------------------- |
| ![титульник без логотипа](/title-page-01.jpg) | ![титульник с логотипом](/title-page-02.jpg) |

## Фильтры Pandoc

<u>[Документация.](https://pandoc.org/filters.html)</u>

*Pandoc* умеет работать с разными фильтрами, но сам рекомендует использовать *Lua-Filters*, так как в этом случае получается нативная работа.

Пайплайн работы *Pandoc*: file $\longrightarrow$ AST(абстрактное синтаксическое дерево) $\longrightarrow$ обработка фильтром $\longrightarrow$ преобразование в tex $\longrightarrow$ применение шаблона $\longrightarrow$ преобразование в целевой формат. То есть фильтр проходится по дереву и в соответствии с запрограммированными правилами изменяет в нем элементы.

В шаблон уже встроены некоторые фильтры, которые можно включать и выключать в конфигурационном файле [build-conf.toml](/build-conf.toml).

## image optimizer