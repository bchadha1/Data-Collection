import os
import symtable
import numpy as np
import pandas as pd
import matplotlib as mtp
import pymongo
import mongoengine
import pyspark
import cv2
import sys, os, random
import nltk
import re
import time
import textblob
import vaderSentiment
from textblob import *

# Textblob is for sentiment classification accuracy
# Vader is for classification

analysis = TextBlob("TextBlob sure looks like it has some interesting features!")
print(dir(analysis))
