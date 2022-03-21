# Qntfy NER analytic

Simple python-based analytic for tagging named entities in documents.
Complies with CDR schema.

## Introduction

This project uses Python, Flask and gunicorn in order to respond to incoming
RESTful (HTTP) requests. Generally, the service takes in CDR-schema JSON and
returns CDR-compliant annotations.

By default it binds to `0.0.0.0` and uses port `45000`. This port can
be overriden by setting the environment variable `ANALYTIC_PORT` to a
port-like integer in the docker run command.

Currently all logging is done via standard out.

The health of the service can be interrogated by issuing an `HTTP GET`
request to:

```
hostname:port/api/v1/health
```

which should return a JSON object containing the string `healthy` if
everything is OK, or an error if not.

## About the analytic

This project uses the [spacy](https://spacy.io/models/en) NER tagger.
More info about the model can be found in the previous link.

Briefly, the analytic uses a model to tag segments of text with particular
tags. These tags come from the Ontonotes 5 data set, and are widely used
in NER tasks.

The output of the model is an `offset` (containing a `start`, inclusive,
and an `end`, exclusive) that can be used to extract the exact text from
the document. Because this can balloon document size, this extraction
is not included in the analytic, but could be included in a post-processing
step, which TwoSix is currently doing.

The offsets also contain a `tag`, which is a description of the segment of text.
Examples can be seen below.

### Tag set

[This file](tags.json) contains a `JSON` file with the tags
and their human readable explanations.

They are also listed below:

``` shell
'CARDINAL', 'DATE', 'EVENT', 'FAC', 'GPE', 'LANGUAGE', 'LAW', 'LOC', 'MONEY',
'NORP', 'ORDINAL', 'ORG', 'PERCENT', 'PERSON', 'PRODUCT', 'QUANTITY',
'TIME', 'WORK_OF_ART'
```
