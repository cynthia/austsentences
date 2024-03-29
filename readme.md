austSentences
=============

austSentences is a large-scale web corpus of Austronesian text. It can be used for any task which
requires a large amount of unsupervised and (relatively) well-formed text, such as language
modeling.

Please note that this is not meant to be an exhaustive corpus covering all Austronesian languages. Currently the corpus contains Bahasa Indonesia, Bahasa Melayu, and Tagalog.

Format
------

The files are [zstd](https://github.com/facebook/zstd) compressed plain text, with one sentence per line encoded in UTF-8.

 - [idwiki.txt.zst](https://drive.google.com/uc?id=13YH7zDpYTZhJBNIl78lZOLMDEn1Qdp5B): 4,172,466 sentences
 - [mswiki.txt.zst](https://drive.google.com/uc?id=1nNpXwxD-xNz3MN0HvCmuypbQJn2zmPLp): 1,710,055 sentences
 - [tlwiki.txt.zst](https://drive.google.com/uc?id=1fUYi_-MnD_xUedoZfbwxml8dDM7tYHFm): 320,230 sentences

Downloading
-----------

You can either download the zstd compressed files directly from the links above, or use the download script.

    python download.py

The requirements can be installed with:

    pip install -r requirements.txt

Extracting
----------

You need a working zstd binary to be able to decompress the corpus. For (Debian) Linux, installation can be done by:

    sudo apt install zstd

For macOS, installation via [Homebrew](https://brew.sh) is possible via:

    brew install zstd

(I have no idea about the availability on non-Debian Linux distributions, BSD, or Windows. PRs welcome!)

Then, use the following command to decompress the corpus.

    zstd -d filename.txt.zst

Details
-------

This corpus is a preprocessed text dump of [Wikipedia](https://wikipedia.org/) articles for each respective language.

The original text is from a snapshot of Wikipedia as of August 1, 2019.
The text has been stripped of Wiki markup, and is encoded in UTF-8.

Short sentences and headlines have been scrubbed out.

Caveats
-------

The corpus may contain paraphrased foreign language text, as there has not been any explicit
processing to remove such text. If this is an issue, you may want to use language detection
to filter out text that is not needed.

Contributing
------------

Currently, as the files are not tracked by Git (due to it's size) the contribution workflow is
unconventional. If you see any errors (e.g. incorrectly tokenized cases at sentence level), the
recommendation is to make a change against the corpus, and submit a diff patch as a Github issue.

The plan is to amalgamate the diffs and provide a patch script to update the corpus to the latest
version - the patches will most likely be small enough to be tracked on Github. When we have
enough patches, these will be applied to the corpus and a new snapshot will be released.

Additionally, as the files are distributed through Google Drive it may be rather inconvenient to
automate access to the files with a script (e.g. cURL or wget) - if you have space for mirroring
the files, please contact the maintainers.

Citations
---------

If you plan to use this work in a publication, please contact the maintainers.

(This hasn't been sorted out yet.)

License
-------

Please refer to the license file [license.txt](license.txt) for details.

Maintainers
-----------

 - [Sangwhan Moon](https://sangwhan.com)
