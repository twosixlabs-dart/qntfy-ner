#!/usr/bin/env python3

import sys
import os
import logging
import json

import falcon
import spacy

from seeder import TagAnnotator

from typing import List


nlp = spacy.load("en_core_web_lg", disable=["parser"])
max_length = os.getenv("MAX_DOCUMENT_LENGTH")
if max_length:
    nlp.max_length = int(max_length)

tag = os.getenv("APP_VERSION")
if not tag:
    tag = "unknown"


def txt_to_cdr_tags(txt: str) -> List:
    # plug in logic for doing text to annotations
    doc = nlp(txt)

    entities = []
    for ent in doc.ents:
        logging.debug(ent.text, ent.start_char, ent.end_char, ent.label_)
        entity_dict = {}
        entity_dict["offset_start"] = ent.start_char
        entity_dict["offset_end"] = ent.end_char
        entity_dict["tag"] = ent.label_
        entities.append(entity_dict)
    return entities


def create():
    tag_anno = TagAnnotator(
        txt_to_cdr_tags,
        label="Qntfy NER",
        version=tag,
    )

    return tag_anno.create()
