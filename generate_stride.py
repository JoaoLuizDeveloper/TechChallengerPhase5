import cv2
from ultralytics import YOLO
import json

class SecurityAnalyzer:
    def __init__(self, model_path='yolov8n.pt'):
        # Carrega o modelo treinado (usando um modelo base para teste inicial)
        self.model = YOLO(model_path)
        
        # Base de conhecimento STRIDE baseada nos requisitos [cite: 9, 14]
        self.threat_knowledge = {
            'usuario': {'threat': 'Spoofing', 'fix': 'Implementar MFA'},
            'firewall_waf': {'threat': 'Bypass de Regras', 'fix': 'Revisão periódica de políticas'},
            'api_gateway': {'threat': 'Denial of Service (DoS)', 'fix': 'Configurar Throttling/Rate Limit'},
            'database_rds': {'threat': 'Information Disclosure', 'fix': 'Criptografia de dados em repouso'},
            'ec2_instance': {'threat': 'Tampering', 'fix': 'Hardening de SO e Patch Management'}
        }

    def analyze_image(self, img_path):
        print(f"--- Analisando: {img_path} ---")
        results = self.model(img_path)
        
        detected_elements = []
        for result in results:
            for box in result.boxes:
                # Obtém o nome da classe detectada
                class_id = int(box.cls[0])
                label = self.model.names[class_id]
                detected_elements.append(label)
        
        return list(set(detected_elements)) # Remove duplicatas

    def generate_report(self, components):
        report = []
        for comp in components:
            # Busca as ameaças na nossa base de conhecimento [cite: 14]
            info = self.threat_knowledge.get(comp, {'threat': 'Análise pendente', 'fix': 'Consultar Documentação'})
            report.append({
                "componente": comp,
                "ameaca_stride": info['threat'],
                "contramedida": info['fix']
            })
        return report

# --- Execução do Projeto ---
analyzer = SecurityAnalyzer()

# Testando com suas imagens 
for img in ['img1.png', 'img2.png']:
    found = analyzer.analyze_image(img)
    final_report = analyzer.generate_report(found)
    
    print(f"Relatório para {img}:")
    print(json.dumps(final_report, indent=4, ensure_ascii=False))
    print("-" * 30)