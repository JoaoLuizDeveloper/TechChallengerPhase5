from ultralytics import YOLO, settings  # Carrega a arquitetura do YOLOv8 e gerencia configurações globais
import os                               # Permite navegar em pastas e manipular caminhos de arquivos no Windows
import torch                            # Base para o Deep Learning; essencial para ativar o uso da GPU (CUDA)
from pathlib import Path

def main():
    # DIRETÓRIO MESTRE    
    BASE_DIR = Path(__file__).resolve().parent

    # 1. Configurações do YOLO
    settings.update({
        'datasets_dir': BASE_DIR,
        'runs_dir': os.path.join(BASE_DIR, 'runs'),
        'weights_dir': os.path.join(BASE_DIR, 'weights')
    })
    
    os.chdir(BASE_DIR)
    
    # 2. Detecção de GPU com feedback detalhado
    if torch.cuda.is_available():
        device = 0
        gpu_name = torch.cuda.get_device_name(0)
        print(f"--- GPU DETECTADA: {gpu_name} ---")
    else:
        device = 'cpu'
        print("--- AVISO: GPU NÃO DETECTADA. RODANDO NA CPU (LENTO) ---")

    print(f"Pasta de Trabalho: {os.getcwd()}")

    # 3. Carrega o modelo
    model = YOLO('yolov8n.pt')

    # 4. Inicia o treinamento otimizado para GPU
    model.train(
        data=os.path.join(BASE_DIR, 'data.yaml'),
        epochs=300,
        imgsz=800,        # Mantive 800 para capturar detalhes dos ícones de infraestrutura
        device=device,
        batch=4,         # Ajuste conforme a memória (VRAM) da sua GPU (16, 32 ou -1 para auto)
        workers=0,        # No Windows, manter 0 evita erros de memória compartilhada
        amp=True,         # Ativa Mixed Precision (treina mais rápido e usa menos VRAM)
        project='runs',
        name='treino_final',
        exist_ok=True,
        verbose=True      # Mostra o status de cada época no terminal
    )

if __name__ == '__main__':
    main()