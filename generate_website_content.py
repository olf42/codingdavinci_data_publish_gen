#!/usr/bin/env python3
"""
Coding Da Vinci Data Presentation Generator

This script is a helper to generate the codingdavinci website data presentation
from yaml files. maintainability is better than with the suggested method of
putting it all into one large HTML file.

Copyright: 2018, Universitätsbibliothek Leipzig <info@ub.uni-leipzig.de>
Author: F. Rämisch <raemisch@ub.uni-leipzig.de>
License: http://opensource.org/licenses/gpl-3.0.php GNU GPLv3

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 2,
as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
"""

import os.path
import sys
import yaml

from os import mkdir, listdir
from jinja2 import Template

BASEPATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE = os.path.join(BASEPATH, "template.html")
BUILDDIR = os.path.join(BASEPATH, "build")
DATADIR = os.path.join(BASEPATH, "data")

def gen_builddir(builddir):
    """
    Creates the build dir if not existent.

    :param builddir: path where built files are save to
    :return: the build path
    """
    if not os.path.isdir(builddir):
        mkdir(builddir)
    return builddir

def get_template(templatepath):
    """
    Takes a template filename and returns a jinja2-Template object
    :param template: full path to template
    :return: jinja2 template
    """
    with open(templatepath) as tfile:
        return Template(tfile.read())

def get_data(datadir):
    """
    Reads all files from the data directory and returns the content as a list of dicts.
    Each file contains the content as a yaml file.

    :param datadir: the directory where the data is located
    :return: list of dicts with the data
    """
    data = []
    for data_file in os.listdir(datadir):
        with open(os.path.join(datadir, data_file)) as dfile:
            data.append(yaml.load(dfile.read()))
    return data

def make_website_content(builddir=BUILDDIR, templatepath=TEMPLATE, datadir=DATADIR):
    """
    Main function wrapping the whole build process.

    :param builddir: output directory where the files are saved to
    :param template:
    :return:
    """
    output = []
    out_dict = {}

    gen_builddir(builddir)
    template = get_template(templatepath)
    data = get_data(datadir)

    # Collect Data to be rendered
    # This is required, to be able to bundle data entries of one provider
    for entry in data:
        if entry['build']:
            provider_slug = entry['provider_slug']
            if provider_slug not in out_dict.keys():
                out_dict[provider_slug] = entry
                out_dict[provider_slug]['data_points'] = [entry,]
            else:
                out_dict[provider_slug]['data_points'].append(entry)

    # Build the template
    for entry in out_dict.values():
        output.append(template.render(entry))

    with open(os.path.join(builddir, "daten.html"), "w") as buildfile:
        buildfile.write("\n".join(output))


def main(argv):
    """
    Wrapper around the make website content. Parses command line arguments to ease
    the build process from the shell.

    :param argv: sys.argv arguments (optionally) containing builddir and template file
    :return:
    """
    builddir = BUILDDIR
    template = TEMPLATE
    datadir = DATADIR
    if len(argv) > 1:
        builddir = argv[1]
    if len(argv) > 2:
        template = argv[2]
    if len(argv) > 3:
        datadir = argv[3]

    make_website_content(builddir, template, datadir)


if __name__ == "__main__":
    main(sys.argv)
