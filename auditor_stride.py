from ultralytics import YOLO            # Garante o acesso à classe principal para carregar o modelo .pt
import pandas as pd                     # Essencial para estruturar os dados do dataset e gerar o relatório final
import os                               # Garante a gestão de arquivos em diferentes partes do script

# ==========================================
# 1. DEFINA OS CAMINHOS AQUI (AJUSTE CONFORME SUA PASTA)
# ==========================================
# Se o arquivo estiver em outra pasta, use o caminho completo (ex: r'C:\Users\...\best.pt')
caminho_modelo = r'D:\Git\PosGraduacao\Fase 05\Repos\Proprio\TechChallengerPhase5\runs\detect\runs\treino_final\weights\best.pt'

# Liste o caminho completo das imagens
imagens_alvo = [
    r'D:\Git\PosGraduacao\Fase 05\Repos\Proprio\TechChallengerPhase5\datasets\val\images\img1.png',
    r'D:\Git\PosGraduacao\Fase 05\Repos\Proprio\TechChallengerPhase5\datasets\val\images\img2.png'
]

# ==========================================
# 2. LÓGICA DO PROJETO
# ==========================================

# Carrega o modelo
if not os.path.exists(caminho_modelo):
    print(f"❌ ERRO: O arquivo de modelo não foi encontrado em: {caminho_modelo}")
else:
    model = YOLO(caminho_modelo)

    # Dicionário de Mapeamento STRIDE (Mantendo o que já tínhamos)
    stride_repo = {
        'usuario': {'ameaca': 'Spoofing', 'risco': 'Falsificação de identidade', 'defesa': 'MFA e Acesso Condicional'},
        'servidor_ec2': {'ameaca': 'Tampering / DoS', 'risco': 'Modificação de arquivos ou queda', 'defesa': 'Security Groups e Patching'},
        'banco_dados_rds': {'ameaca': 'Information Disclosure', 'risco': 'Vazamento de dados', 'defesa': 'Criptografia em repouso e SSL'},
        'load_balancer': {'ameaca': 'Denial of Service', 'risco': 'Sobrecarga de tráfego', 'defesa': 'WAF integrado e Auto Scaling'},
        'rede_vpc': {'ameaca': 'Information Disclosure', 'risco': 'Sniffing de rede', 'defesa': 'VPC Flow Logs e Isolamento de Subnets'},
        'aws_waf': {'ameaca': 'Denial of Service', 'risco': 'Ataques de aplicação (L7)', 'defesa': 'Regras gerenciadas e IP Sets'},
        'aws_shield': {'ameaca': 'Denial of Service', 'risco': 'Ataques volumétricos (DDoS)', 'defesa': 'Proteção Standard/Advanced habilitada'},
        'web_server': {'ameaca': 'Tampering', 'risco': 'Desfiguração (Defacement)', 'defesa': 'Monitoramento de integridade e Backup'},
        'internet': {'ameaca': 'External Threat', 'risco': 'Origem de ataques', 'defesa': 'Firewall de borda e IPS'},
        'azure_api_management': {'ameaca': 'Elevation of Privilege', 'risco': 'Abuso de endpoints', 'defesa': 'Validação de Token e Throttling'},
        'azure_logic_apps': {'ameaca': 'Tampering', 'risco': 'Execução de fluxos maliciosos', 'defesa': 'Gerenciamento de Identidade (MSI)'},
        'azure_sql_database': {'ameaca': 'Information Disclosure', 'risco': 'Exposição de dados SQL', 'defesa': 'Data Masking e Firewall do Azure SQL'},
        'aws_cloud_trail': {'ameaca': 'Repudiation', 'risco': 'Apagamento de trilhas de auditoria', 'defesa': 'Proteção de deletar logs e MFA Delete'},
        'aws_key_managment_KMS': {'ameaca': 'Information Disclosure', 'risco': 'Uso indevido de chaves', 'defesa': 'Políticas de chave restritivas e Rotação'},
        'aws_backup': {'ameaca': 'Information Disclosure', 'risco': 'Perda/Roubo de backups', 'defesa': 'Criptografia e Cofre protegido'},
        'aws_cloud_watch': {'ameaca': 'Repudiation', 'risco': 'Falta de monitoramento crítico', 'defesa': 'Alarmes de métricas e Dashboard de SOC'},
        'microsoft_entra_ID': {'ameaca': 'Spoofing', 'risco': 'Comprometimento de credenciais', 'defesa': 'PIM e Revisão de Acesso'},
        'api_gateway': {'ameaca': 'Elevation of Privilege', 'risco': 'Acesso sem autorização', 'defesa': 'Authorizers Lambda / Cognito'},
        'servidor_app': {'ameaca': 'Tampering', 'risco': 'Execução de código arbitrário', 'defesa': 'Varredura de vulnerabilidades (Inspector)'}
    }

    print("--- INICIANDO AUDITORIA ---")
    results = model.predict(source=imagens_alvo, save=True, conf=0.1)

    dados_relatorio = []
    for i, r in enumerate(results):
        img_path = imagens_alvo[i]
        nome_arquivo = os.path.basename(img_path)
        
        for c in r.boxes.cls:
            nome_classe = model.names[int(c)]
            info = stride_repo.get(nome_classe, {'ameaca': 'Analise Manual', 'risco': 'N/A', 'defesa': 'Verificar docs'})
            
            dados_relatorio.append({
                'Imagem': nome_arquivo,
                'Componente': nome_classe,
                'Ameaça STRIDE': info['ameaca'],
                'Recomendação': info['defesa']
            })

    # Exibe e Salva
    df = pd.DataFrame(dados_relatorio).drop_duplicates()
    print(df.to_string(index=False))
    df.to_csv('relatorio_final_stride.csv', index=False)