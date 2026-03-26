# ULTIMATE Cloud Desktop Platform

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PyQt5](https://img.shields.io/badge/PyQt5-5.15+-green.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-red.svg)
![AWS](https://img.shields.io/badge/AWS-EC2-orange.svg)
![Docker](https://img.shields.io/badge/Docker-20.10+-blue.svg)

## 🚀 Enterprise-Level Cloud Management Platform

Una piattaforma desktop completa per la gestione di servizi cloud enterprise, combinando un'interfaccia grafica moderna con un backend API robusto.

### ✨ Caratteristiche Principali

- **🖥️ Interfaccia Desktop**: GUI PyQt5 elegante e intuitiva
- **⚡ Backend FastAPI**: API REST ad alte prestazioni
- **☁️ AWS Integration**: Gestione completa di EC2 instances
- **🐳 Docker Management**: Controllo container Docker
- **📊 Real-time Monitoring**: Monitoraggio CPU/RAM in tempo reale
- **🔒 Enterprise Security**: Architettura sicura e scalabile

### 🛠️ Architettura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   PyQt5 GUI     │    │   FastAPI        │    │     AWS EC2     │
│                 │◄──►│   Backend       │◄──►│   Docker        │
│ - Dashboard     │    │ - REST API      │    │ - Containers    │
│ - Controls      │    │ - Monitoring    │    │ - Monitoring    │
│ - Real-time     │    │ - Management    │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 📋 Prerequisiti

- **Python 3.8+**
- **PyQt5** per l'interfaccia grafica
- **FastAPI** per il backend
- **boto3** per AWS
- **docker** per Docker management
- **psutil** per monitoraggio sistema
- **requests** per chiamate API

### 🔧 Installazione

1. **Clona il repository:**
   ```bash
   git clone https://github.com/danimassag-sys/cloud_services_app_python_gui.git
   cd cloud_services_app_python_gui
   ```

2. **Installa le dipendenze:**
   ```bash
   pip install fastapi boto3 docker psutil requests pyqt5
   ```

3. **Configura AWS:**
   ```bash
   aws configure
   # Inserisci le tue credenziali AWS
   ```

4. **Avvia il backend:**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

5. **Avvia l'applicazione GUI:**
   ```bash
   python cloud_services_app_python_gui.py
   ```

### 🎯 Utilizzo

#### Backend API

Il backend fornisce i seguenti endpoint REST:

- `GET /servers/ec2` - Lista tutte le istanze EC2
- `POST /servers/ec2/start/{instance_id}` - Avvia un'istanza EC2
- `POST /servers/ec2/stop/{instance_id}` - Ferma un'istanza EC2
- `GET /docker` - Lista tutti i container Docker
- `POST /docker/start/{name}` - Avvia un container Docker
- `POST /docker/stop/{name}` - Ferma un container Docker
- `GET /monitor` - Statistiche di monitoraggio sistema

#### Interfaccia Grafica

L'applicazione desktop offre:

- **Dashboard in tempo reale** con metriche CPU/RAM
- **Gestione EC2** - Avvia/ferma istanze con un click
- **Controllo Docker** - Gestisci container locali
- **Monitoraggio integrato** - Visualizza lo stato del sistema
- **Interfaccia intuitiva** - Design moderno e responsive

### 🔐 Sicurezza

- Autenticazione AWS IAM
- Comunicazione HTTPS
- Gestione sicura delle credenziali
- Logging completo delle operazioni

### 📊 Monitoraggio

- **CPU Usage**: Percentuale utilizzo CPU
- **RAM Usage**: Percentuale utilizzo memoria
- **EC2 Status**: Stato delle istanze AWS
- **Docker Status**: Stato dei container
- **Real-time Updates**: Aggiornamenti automatici ogni secondo

### 🐳 Docker Deployment

Per eseguire in un container Docker:

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 🤝 Contributi

Contributi benvenuti! Per contribuire:

1. Fork il progetto
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Commit delle modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

### 📝 Licenza

Questo progetto è distribuito sotto licenza MIT. Vedi il file `LICENSE` per maggiori dettagli.

### 📞 Supporto

Per supporto o domande:
- Apri una issue su GitHub
- Contatta il maintainer

---

**⚠️ Nota**: Questa è una piattaforma enterprise-level. Assicurati di avere le autorizzazioni appropriate per gestire risorse AWS e Docker prima dell'utilizzo.</content>
<parameter name="filePath">c:\Users\danim\Desktop\cloud_services_app_python_gui\README.md