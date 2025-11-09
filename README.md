# EpiWatch

EpiWatch é um projeto de visão computacional que detecta o uso correto de Equipamentos de Proteção Individual (EPIs) em imagens/vídeos (ex.: capacete, amacação, botas, luvas). Quando é detectada a ausência de um EPI, o sistema registra a evidência (imagem/thumbnail) e envia uma alerta (notificação ao gerente/feramenteiro). O projeto também permite classificar o tipo de infração e gerar uma ação corretiva básica (por exemplo: limpeza da oficina) para registro administrativo.

Neste estágio inicial, a API do projeto será implementada usando **Django**, para facilitar a criação de endpoints e integração com banco de dados.

---

## Funcionalidades principais

* Detecção de presença/ausência de EPIs por pessoa na imagem.
* Classes suportadas: `capacete`, `amacacao` (macacão/aventais), `botas`, `luvas`.
* Registro de evidência com timestamp e crop da pessoa sem EPI.
* Envio de alerta para gerente/feramenteiro via API Django.
* Dashboard simples (opcional) para visualizar infrações e imagens.
* Suporte a modelos YOLOv8 (ponto de partida com `yolov8n.pt`).

---

## Estrutura do repositório

```
dir/
├─ data/                # Dados locais (ignorados no git por padrão)
├─ datasets/            # Datasets anotados (VOC/COCO/YAML)
├─ data.yaml            # Configuração do dataset (treino/val)
├─ main.py              # Script principal (inference / integração com Django)
├─ train_yolo.py        # Script de treinamento
├─ venv/                # Ambiente virtual (ignorável)
├─ yolov8n.pt           # Checkpoint do modelo (recomenda-se Git LFS ou armazenamento externo)
├─ epiwatch/            # Projeto Django (apps, settings, urls, views, models)
```

---

## Requisitos

* Python 3.8+
* Django 4.x+
* Pip
* Dependências listadas no `requirements.txt` (ex.: `ultralytics`, `opencv-python`, `djangorestframework`, `pydantic`, `requests`)
* (Opcional) Git LFS para versionar pesos grandes

Links úteis:

* YOLO/Ultralytics: [https://github.com/ultralytics/ultralytics](https://github.com/ultralytics/ultralytics)
* Django REST Framework: [https://www.django-rest-framework.org/](https://www.django-rest-framework.org/)
* Git LFS: [https://git-lfs.github.com/](https://git-lfs.github.com/)

---

## Instalação (rápida)

```bash
# clonar
git clone <URL_DO_REPOSITORIO>
cd <repo>

# criar ambiente
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate    # Windows

# instalar dependências
pip install -r requirements.txt
```

Se for versionar `*.pt`, configure Git LFS:

```bash
git lfs install
git lfs track "*.pt"
git add .gitattributes
```

---

## Treinamento

1. Prepare o dataset em formato COCO ou YOLO.
2. Atualize `data.yaml` com caminhos para treino/val e classes.
3. Execute o treinamento (exemplo com ultralytics):

```bash
python train_yolo.py --data data.yaml --cfg yolov8n.yaml --epochs 50 --batch 16
```

---

## API Django e envio de alerta

No estágio inicial, a API será criada em Django REST Framework:

1. Criar app `infractions` dentro do projeto Django.
2. Definir modelos (`models.py`) para Infrações, Pessoas e Evidências.
3. Criar serializers (`serializers.py`) e views (`views.py`) para expor endpoints REST.
4. Implementar lógica de inferência no `main.py` e chamar endpoints Django para registrar infrações.

Exemplo de endpoint para registrar infração:

```http
POST /api/infractions/
Content-Type: application/json

{
  "timestamp": "2025-11-09T10:00:00Z",
  "infracao": "sem_capacete",
  "imagem_url": "https://storage/exemplo.jpg",
  "confidence": 0.87
}
```

---

## Boas práticas e ética

* Guarde evidências com segurança e controle de acesso.
* Informe os trabalhadores sobre monitoramento por visão computacional.
* Use dados anotados corretamente para reduzir falsos positivos.

---

## Deploy e produção

* Containerize com Docker e use Uvicorn/Gunicorn para rodar Django.
* Armazene imagens em storage (S3, MinIO) e não no repositório.
* Utilize filas (RabbitMQ, Redis) para processar eventos e evitar sobrecarga.

---

## Contribuição

Contribuições são bem-vindas. Abra issues ao reportar bugs ou sugerir melhorias. Para mudanças grandes, prefira abrir um pull request com descrição clara e dados de teste.


## dataset
[link](https://www.kaggle.com/datasets/ketakichalke/ppe-kit-detection-construction-site-workers?utm_source=chatgpt.com)
