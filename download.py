#!/usr/bin/env python

import gdown
import os
import os.path


files = {
    "idwiki.txt.zst": "https://drive.google.com/uc?id=13YH7zDpYTZhJBNIl78lZOLMDEn1Qdp5B",
    "mswiki.txt.zst": "https://drive.google.com/uc?id=1nNpXwxD-xNz3MN0HvCmuypbQJn2zmPLp",
    "tlwiki.txt.zst": "https://drive.google.com/uc?id=1fUYi_-MnD_xUedoZfbwxml8dDM7tYHFm",
}

download = lambda to, url: gdown.download(url, to, quiet=False)


def main():
    output_dir = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'data')

    try:
        os.mkdir(output_dir)
    except:
        pass

    for k, v in files.items():
        download(os.path.join(output_dir, k), v)


if __name__ == '__main__':
    main()
