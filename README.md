# Sample Poster

This is an example of what a LaTeX poster (using the [tikzposter](https://www.ctan.org/pkg/tikzposter) package) could look like.

This example includes two types of figures:
1. **SVG** These are edited in [Inkscape](https://inkscape.org). In [/bin](bin) you will find one python script for each SVG file. They do some simple manipulation of the files by naming select tags using their IDs, and output a series of SVG files that are useful for creating narratives in presentations. Another [script](bin/generate-tex-includes) scans the latex source (and any file inclusions or imports) for SVG dependencies, and automatically convers these to PDF. It uses Inkscape for the actual conversion.
2. **TikZ** These are written in LaTeX using the [TikZ](https://en.wikibooks.org/wiki/LaTeX/PGF/TikZ) package.

## Dependencies

- Python 3.6+
- The [svgnarrative](https://pypi.org/project/svgnarrative/) python package (installable through pip)
- Perl 5
- Inkscape
- LaTeX
- Make

## Building

```shell
make
```

