# 🛡️ CloudGuard-STRIDE: Auditoria Automatizada de Infraestrutura via YOLOv8

Este projeto foi desenvolvido como parte do **Tech Challenge (Fase 5)** da Pós-Graduação. O objetivo é integrar Inteligência Artificial e Segurança Cibernética para automatizar a detecção de ativos de nuvem em diagramas de arquitetura e realizar uma auditoria de riscos baseada na metodologia **STRIDE**.

O sistema utiliza o modelo **YOLOv8** para reconhecimento visual e um motor de regras para mapear ameaças e recomendações de mitigação.

---

## 📂 Estrutura do Projeto

A organização dos arquivos segue o padrão recomendado para reprodutibilidade e integridade do modelo:

* **`dataset/`**: Diretório contendo os dados de treinamento.
    * `images/`: Imagens do projeto divididas em `train` e `val`.
    * `labels/`: Arquivos de anotação `.txt` correspondentes (Padrão YOLO).
* **`data.yaml`**: Configuração de caminhos e definição das classes (ex: Servidor EC2).
* **`check_dataset.py`**: Script de sanitização e verificação de integridade.
* **`train.py`**: Pipeline de treinamento do modelo.
* **`auditor_stride.py`**: Script final de inferência e auditoria de segurança.

---

## 🛠️ Pré-requisitos

O projeto requer a instalação da biblioteca `ultralytics` para operação do YOLOv8:

```bash
pip install ultralytics
```

---

## 🚀 Guia de Execução (Ordem Obrigatória)

### Passo 1: Validação do Dataset
Antes de qualquer treinamento, valide a integridade dos seus dados.
```bash
python check_dataset.py
```
* **Por que fazer isso?** Este script garante que todas as imagens possuem rótulos (labels) correspondentes. Se as métricas nos gráficos aparecerem zeradas, o problema geralmente reside na falta desses arquivos de validação.

### Passo 2: Treinamento do Modelo
Execute o treinamento para que o modelo aprenda a identificar os componentes.
```bash
python train.py
```
* **Resultado:** Este passo gera os pesos otimizados em `runs/detect/train/weights/best.pt`. É este arquivo que será utilizado para as auditorias reais.

### Passo 3: Auditoria de Segurança
Com o modelo treinado, execute a ferramenta de auditoria.
```bash
python auditor_stride.py
```
* **Função:** O script carrega o `best.pt`, detecta componentes em novas imagens e aplica a matriz de ameaças STRIDE para sugerir mitigações imediatas.

---

## 📊 Análise de Métricas

Para validar a qualidade do modelo entregue, analise os gráficos gerados na pasta `runs/`:

* **mAP (Mean Average Precision):** Indica a acurácia do modelo. Busque valores que subam e se estabilizem próximos a 1.0 (100%).
* **Loss (Perda):** As curvas de `box_loss`, `cls_loss` e `dfl_loss` devem apresentar uma tendência de queda constante. Se a perda de validação (`val/loss`) começar a subir enquanto a de treino cai, o modelo está sofrendo de *overfitting*.

---

## 🛡️ Metodologia STRIDE Aplicada

| Componente | Ameaça STRIDE | Recomendação de Segurança |
| :--- | :--- | :--- |
| **Servidor EC2** | Tampering / DoS | Implementar Security Groups restritos e Patching de OS. |
| **S3 Bucket** | Info Disclosure | Habilitar Block Public Access e criptografia em repouso. |
| **Database** | Spoofing / Tampering | Utilizar autenticação IAM e backups multi-regionais. |

---
**Desenvolvido para o Tech Challenge - Pós-Graduação em Engenharia de Machine Learning.**
