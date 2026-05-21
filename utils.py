import os
from datetime import datetime

def create_output_folder(base_dir: str) -> str:
    """
    Cria uma pasta com a data atual dentro de base_dir.
    Ex: data/2026-05-20/
    """
    today = datetime.today().strftime("%Y-%m-%d")
    folder_path = os.path.join(base_dir, today)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path