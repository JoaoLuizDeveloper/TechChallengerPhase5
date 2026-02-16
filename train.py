from ultralytics import YOLO, settings
import os
import torch

def main():
    # DIRETÓRIO MESTRE (Ajustado exatamente para o que você pediu)
    BASE_DIR = r'D:\Git\PosGraduacao\Fase 05\Repos\Proprio\TechChallengerPhase5'
    
    # 1. Força o YOLO a salvar tudo dentro da Fase 05
    settings.update({
        'datasets_dir': BASE_DIR,
        'runs_dir': os.path.join(BASE_DIR, 'runs'),
        'weights_dir': os.path.join(BASE_DIR, 'weights')
    })
    
    # 2. Garante que o Python está trabalhando "dentro" dessa pasta
    os.chdir(BASE_DIR)
    
    device = 0 if torch.cuda.is_available() else 'cpu'
    print(f"--- INICIANDO TREINO NA FASE 05 ---")
    print(f"Dispositivo: {device}")
    print(f"Pasta de Trabalho: {os.getcwd()}")

    # 3. Carrega o modelo base
    model = YOLO('yolov8n.pt')

    # 4. Inicia o treinamento
    model.train(
        data=os.path.join(BASE_DIR, 'data.yaml'),
        epochs=100,
        imgsz=640,
        device=device,
        workers=0,
        project='runs',      # Pasta que será criada na Fase 05
        name='treino_final', # Nome da subpasta dos resultados
        exist_ok=True        # Se você rodar de novo, ele não cria 'treino_final2'
    )

if __name__ == '__main__':
    main()