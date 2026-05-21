import requests
import pandas as pd
from pyspark.sql import SparkSession

from config import API_URL, BASE_OUTPUT_DIR, CSV_FILENAME
from utils import create_output_folder

def fetch_api_data(url: str) -> list:
    """
    Consulta a API e retorna os dados em formato lista de dicionários.
    """
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return [data]  # API retorna dict, convertendo para lista de dicts

def save_csv(data: list, output_folder: str, filename: str):
    """
    Salva os dados em CSV usando pandas.
    """
    df = pd.DataFrame(data)
    output_path = f"{output_folder}/{filename}"
    df.to_csv(output_path, index=False)
    print(f"CSV salvo em: {output_path}")
    return output_path

def process_with_spark(csv_path: str):
    """
    Cria SparkSession local, lê CSV e exibe algumas linhas.
    """
    spark = SparkSession.builder \
        .appName("IBGE Population Lab") \
        .master("local[*]") \
        .getOrCreate()

    df = spark.read.csv(csv_path, header=True, inferSchema=True)
    df.show(5)
    spark.stop()

def main():
    output_folder = create_output_folder(BASE_OUTPUT_DIR)
    data = fetch_api_data(API_URL)
    csv_path = save_csv(data, output_folder, CSV_FILENAME)
    process_with_spark(csv_path)

if __name__ == "__main__":
    main()