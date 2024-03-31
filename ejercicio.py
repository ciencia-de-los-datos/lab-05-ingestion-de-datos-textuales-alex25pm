import os
import pandas as pd

# Función para leer los archivos de texto y obtener los datos
def read_files(directory):
    data = []
    for sentiment in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, sentiment)):
            for filename in os.listdir(os.path.join(directory, sentiment)):
                if filename.endswith(".txt"):  # Verificamos si el archivo tiene la extensión ".txt"
                    with open(os.path.join(directory, sentiment, filename), 'r', encoding='utf-8', errors='ignore') as file:
                        text = file.read()
                        data.append({'phrase': text, 'sentiment': sentiment})
    return data

# Directorios de entrenamiento y prueba
train_directory = 'train'
test_directory = 'test'

# Leer archivos de entrenamiento y prueba
train_data = read_files(train_directory)
test_data = read_files(test_directory)

# Convertir los datos en DataFrames de pandas
train_df = pd.DataFrame(train_data)
test_df = pd.DataFrame(test_data)

print(train_df), print(test_df)

# Guardar los DataFrames como archivos CSV
train_df.to_csv('train_dataset.csv', index=False)
test_df.to_csv('test_dataset.csv', index=False)