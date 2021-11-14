# ascii-display
a CLI tool to display images in your terminal

## Installation

just run `sudo sh installer.sh` and you'll be ready!

## Usage

`tid <image> [params]`

arguments: <image> --scale [scale (default=1)] --capprox [int (default=5)] [--nocolor] [--fat] --save [out] <\br>
            capprox: likelyhood of using secondary colors<\br>
            fat: double the width of the output<\br>
            save: write output to [out] file. If nocolor is not active, will store ANSII color escape codes as well<\br>
