{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # common/bq_loader.py\
from google.cloud import bigquery\
import os\
import json\
\
DATASET = os.getenv('BQ_DATASET', 'proteinas_alternativas')\
TABLE = os.getenv('BQ_TABLE', 'adjudicaciones')\
\
def get_client():\
    # Asume GOOGLE_APPLICATION_CREDENTIALS ya apuntando al json en el runner/local\
    return bigquery.Client()\
\
def ensure_table_exists():\
    client = get_client()\
    dataset_ref = client.dataset(DATASET)\
    try:\
        client.get_dataset(dataset_ref)\
    except Exception:\
        client.create_dataset(DATASET)\
    table_ref = dataset_ref.table(TABLE)\
    schema = [\
        bigquery.SchemaField("organismo", "STRING"),\
        bigquery.SchemaField("convocatoria", "STRING"),\
        bigquery.SchemaField("proyecto", "STRING"),\
        bigquery.SchemaField("entidad", "STRING"),\
        bigquery.SchemaField("importe", "NUMERIC"),\
        bigquery.SchemaField("fecha", "DATE"),\
        bigquery.SchemaField("raw_url", "STRING"),\
        bigquery.SchemaField("resumen", "STRING"),\
        bigquery.SchemaField("keywords_detectadas", "STRING", mode="REPEATED"),\
        bigquery.SchemaField("inserted_at", "TIMESTAMP"),\
    ]\
    try:\
        client.get_table(table_ref)\
    except Exception:\
        table = bigquery.Table(table_ref, schema=schema)\
        client.create_table(table)\
        print("Tabla creada:", table_ref.path)\
\
def load_rows(rows):\
    client = get_client()\
    dataset_ref = client.dataset(DATASET)\
    table_ref = dataset_ref.table(TABLE)\
    errors = client.insert_rows_json(table_ref, rows)\
    if errors:\
        raise RuntimeError(errors)\
    return True\
}