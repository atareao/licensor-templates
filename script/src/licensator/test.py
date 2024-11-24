#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2024 Lorenzo Carbonell <a.k.a. atareao>

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from os import walk
import frontmatter
from yaml import  dump
from yaml import CDumper as Dumper

def main():
    files = []
    licenses = []

    route = "/data/rust/licensor-templates/temporal/choosealicense.com/_licenses/"
    for (dirpath, dirnames, filenames) in walk(route):
        files.extend(filenames)
        break
    for filename in files:
        print(filename)
        fileroute = f"{route}/{filename}"
        with open(fileroute) as fr:
            post = frontmatter.load(fr)
            print(post.metadata)
            print(post.content)
            licenses.append({
                "name": post.metadata["spdx-id"],
                "description": post.metadata["title"],
                "filename": f"{post.metadata["spdx-id"].lower()}.jinja"
            })
        jinjafilename = f"{post.metadata["spdx-id"].lower()}.jinja"
        jinja = (f"/data/rust/licensor-templates/temporal/choosealicense.com/"
                 f"_licenses/{jinjafilename}")
        with open(jinja, "w") as fw:
            fw.write(post.content)
    print(licenses)
    output = dump(licenses, Dumper=Dumper)
    with open("licenses.yml", "w") as fw:
        fw.write(output)


if __name__ == '__main__':
    main()
