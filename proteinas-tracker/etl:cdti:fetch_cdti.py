{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # etl/cdti/fetch_cdti.py\
from common.utils import load_keywords, normalize_entry, find_keywords\
from common.bq_loader import ensure_table_exists, load_rows\
from datetime import date\
\
def fetch_cdti():\
    ejemplo = \{\
        'organismo': 'CDTI',\
        'convocatoria': 'NEOTEC 2025',\
        'proyecto': 'Biofabricaci\'f3n de an\'e1logos vegetales',\
        'entidad': 'Empresa Ejemplo SL',\
        'importe': 90000,\
        'fecha': str(date.today()),\
        'raw_url': 'https://cdti.es/example.pdf',\
        'resumen': 'Investigaci\'f3n en biofabricaci\'f3n y an\'e1logos vegetales'\
    \}\
    return [ejemplo]\
\
def main():\
    keywords = load_keywords()\
    raws = fetch_cdti()\
    rows = []\
    for raw in raws:\
        raw['keywords_detectadas'] = find_keywords(raw.get('proyecto','') + " " + raw.get('resumen',''), keywords)\
        row = normalize_entry(raw)\
        rows.append(row)\
    ensure_table_exists()\
    load_rows(rows)\
    print("CDTI: insertadas", len(rows))\
\
if __name__ == '__main__':\
    main()\
}