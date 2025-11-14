{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # common/utils.py\
import re\
import yaml\
from pathlib import Path\
\
def load_keywords(path='config/keywords.yml'):\
    p = Path(path)\
    data = yaml.safe_load(p.read_text())\
    return [k.lower() for k in data.get('keywords', [])]\
\
def normalize_entry(raw):\
    """\
    Cambia el dict 'raw' al est\'e1ndar requerido.\
    Debe devolver: organismo, convocatoria, proyecto, entidad, importe, fecha, raw_url, resumen, keywords_detectadas\
    """\
    return \{\
        'organismo': raw.get('organismo'),\
        'convocatoria': raw.get('convocatoria'),\
        'proyecto': raw.get('proyecto'),\
        'entidad': raw.get('entidad'),\
        'importe': raw.get('importe'),\
        'fecha': raw.get('fecha'),\
        'raw_url': raw.get('raw_url'),\
        'resumen': raw.get('resumen', ''),\
        'keywords_detectadas': raw.get('keywords_detectadas', []),\
    \}\
\
def find_keywords(text, keywords):\
    text_low = (text or "").lower()\
    found = []\
    for kw in keywords:\
        if kw in text_low:\
            found.append(kw)\
    return sorted(set(found))\
}