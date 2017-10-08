
Dragnet API
=======

RESTful API built with Flask, to be deployed with Docker, based entirely off of the [<i>Dragnet Content Extraction Algorithm</i>](https://github.com/seomoz/dragnet)

[![Build Status](https://api.travis-ci.org/seomoz/dragnet.png)](https://api.travis-ci.org/seomoz/dragnet.png)

Dragnet isn't interested in the shiny chrome or boilerplate dressing
of a web page. It's interested in... 'just the facts.'  The machine
learning models in Dragnet extract the main article content and
optionally user generated comments from a web page.  They provide
state of the art performance on variety of test benchmarks.

For more information on Dragnet's approach check out:

* The paper [<i>Content Extraction Using Diverse Feature Sets</i>](dragnet_www2013.pdf?raw=true), published
at WWW in 2013, gives an overview of the machine learning approach.
* [A comparison](https://moz.com/devblog/benchmarking-python-content-extraction-algorithms-dragnet-readability-goose-and-eatiht/) of Dragnet and alternate content extraction packages.
* [This blog post](https://moz.com/devblog/dragnet-content-extraction-from-diverse-feature-sets/) explains the intuition behind the algorithms.

# GETTING STARTED

Depending on your use case, Dragnet provides two separate models to extract
just the main article content or the content and any user generated
comments.  Each model implements the `analyze` method that
takes an HTML string and returns the content string.

```python
import requests
from dragnet import content_extractor, content_comments_extractor

# fetch HTML
url = 'https://moz.com/devblog/dragnet-content-extraction-from-diverse-feature-sets/'
r = requests.get(url)

# get main article without comments
content = content_extractor.analyze(r.content)

# get article and comments
content_comments = content_comments_extractor.analyze(r.content)
```

## Installing

Dragnet is written in Python (developed with 2.7, not tested on 3)
and built on the numpy/scipy/Cython numerical computing environment.
In addition we use <a href="http://lxml.de/">lxml</a> (libxml2)
for HTML parsing.

### Installing with Docker:

1. Build the docker image 
``` 
$ docker build -t dragnetAPI .
```
2. Run the docker image as a container
```bash
# creates runtime environment and executes entrypoint script in said environment 
$ docker container run -it dragnet-1 /bin/bash -c "source /root/miniconda2/bin/activate /root/py && python my_script.py"
```

```bash
$ cd dragnet
$ sudo make install
# these should now pass
$ make test
```
