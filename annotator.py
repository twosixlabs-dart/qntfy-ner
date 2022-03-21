#!/usr/bin/env python3

import sys
import os
import logging
import json

import falcon
import spacy

from seeder import TagAnnotator

from typing import List

import analytic


app = analytic.create()
