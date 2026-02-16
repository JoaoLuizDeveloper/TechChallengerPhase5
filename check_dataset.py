import os

def validar_dataset(base_path):
    print(f"--- Verificando Dataset em: {base_path} ---")
    
    etapas = ['train', 'val']
    
    for etapa in etapas:
        img_path = os.path.join(base_path, 'images', etapa)
        lbl_path = os.path.join(base_path, 'labels', etapa)
        
        # Verifica se as pastas existem
        if not os.path.exists(img_path) or not os.path.exists(lbl_path):
            print(f"\n[ERRO] Pastas de {etapa} não encontradas!")
            print(f"Esperado: {img_path} e {lbl_path}")
            continue

        # Lista arquivos
        imagens = {os.path.splitext(f)[0] for f in os.listdir(img_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))}
        labels = {os.path.splitext(f)[0] for f in os.listdir(lbl_path) if f.endswith('.txt')}

        print(f"\nResultados para [{etapa.upper()}]:")
        print(f"- Imagens encontradas: {len(imagens)}")
        print(f"- Labels (.txt) encontrados: {len(labels)}")

        # Encontra órfãos
        sem_label = imagens - labels
        sem_imagem = labels - imagens

        if sem_label:
            print(f"⚠️ Alerta: {len(sem_label)} imagens SEM arquivo .txt correspondente!")
            print(f"Exemplos: {list(sem_label)[:3]}")
        
        if sem_imagem:
            print(f"⚠️ Alerta: {len(sem_imagem)} arquivos .txt SEM imagem correspondente!")
            print(f"Exemplos: {list(sem_imagem)[:3]}")

        if len(imagens) == len(labels) and not sem_label:
            print(f"✅ Tudo OK na pasta {etapa}!")

# --- AJUSTE O CAMINHO ABAIXO ---
meu_caminho = r"D:\Git\PosGraduacao\Fase 05\Repos\Proprio\TechChallengerPhase5\dataset"
validar_dataset(meu_caminho)