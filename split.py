from pydub import AudioSegment
import os

def split_audio(file_path, start_time_str, end_time_str, target_folder=""):
    # Carrega o arquivo de áudio
    audio = AudioSegment.from_file(file_path)

    # Converte string de tempo no formato mm:ss para milissegundos
    start_time = sum(int(x) * 60 ** i for i, x in enumerate(reversed(start_time_str.split(":")))) * 1000
    end_time = sum(int(x) * 60 ** i for i, x in enumerate(reversed(end_time_str.split(":")))) * 1000

    # Extrai a parte especificada do áudio
    extracted_audio = audio[start_time:end_time]

    # Cria a pasta de destino se não existir
    if target_folder and not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Substitui dois-pontos por sublinhados no nome do arquivo de saída
    safe_start_time_str = start_time_str.replace(":", "-")
    safe_end_time_str = end_time_str.replace(":", "-")
    target_file_name = f"{os.path.splitext(os.path.basename(file_path))[0]}_{safe_start_time_str}_to_{safe_end_time_str}.mp3"
    target_file_path = os.path.join(target_folder, target_file_name) if target_folder else target_file_name

    # Exporta o trecho extraído
    extracted_audio.export(target_file_path, format="mp3")
    print(f"Áudio cortado salvo em: {target_file_path}")

# Configurações iniciais
arquivo_base = "nome_do_seu_audio_aqui.mp3"  # Caminho para o arquivo de áudio ou coloque na mesma pasta
inicio_tempo = "00:00"  # Tempo inicial no formato mm:ss
fim_tempo = "10:00"  # Tempo final no formato mm:ss

# Substitua 'pasta_destino' com o caminho desejado ou deixe em branco para usar o diretório atual do script
pasta_destino = r"G:\Concurso CORE ES\Programas para estudos\Mp3 Split"  # ou pasta_destino = ""

# Se 'pasta_destino' não estiver vazio, verifica se o caminho existe. Se não existir, tenta criar.
if pasta_destino and not os.path.exists(pasta_destino):
    try:
        os.makedirs(pasta_destino)
    except OSError as e:
        print(f"Erro ao criar a pasta de destino: {e}")

# Executa a função de divisão do áudio
split_audio(arquivo_base, inicio_tempo, fim_tempo, pasta_destino)

# ::OBSERVAÇÕES::
# É necessário ter o "ffmpeg" instalado, na pasta -> C:\ffmpeg.
# Tutorial de como instalar: https://www.youtube.com/watch?v=Q267RF1I3GE