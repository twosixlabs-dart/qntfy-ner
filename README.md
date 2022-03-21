# Qntfy NER analytic    
Simple python-based analytic for tagging named entities in documents.
Complies with CDR schema.  
[![build and publish](https://github.com/twosixlabs-dart/qntfy-ner/actions/workflows/build-and-publish.yml/badge.svg)](https://github.com/twosixlabs-dart/qntfy-ner/actions/workflows/build-and-publish.yml)

## Swagger-rendered HTML documentation

Can be found [here](https://worldmodelers.pages.qntfy.com/spacy-analytic/).

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
### Override maximum document length

Set `MAX_DOCUMENT_LENGTH` environment variable to process text fields with over
the default of `1000000` (1 million) characters.

### Benchmarks

[Read more](./benchmarks/benchmarks.md).


## Delivery information

### Source Code

#### Service or integration code such as REST APIs or web applications

Contained in this repository.

#### Source code for model training

Available at the [spacy website][spacy-training].

### Models

#### Inventory of any open source / public models that were used

Available at the [spacy website][spacy-models].

#### Information for how to obtain these models

Consult [this script](./dependencies.sh) or above site.

### Documentation

#### Reference information on the model or algorithm that is used for each analytic

Available at the [spacy website][spacy-models].

#### Documentation on how to train and deploy new models

Available at the [spacy website][spacy-training].

#### Information on data cleaning, preparation, or formatting that is required for each model

Available at the [spacy website][spacy-models].

### Data

This model was not trained on data provided by TwoSix.

[spacy-training]: https://spacy.io/usage/training
[spacy-models]: https://spacy.io/models/en
