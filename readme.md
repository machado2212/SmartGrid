# 💡 SmartGrid Monitoring & Fault Detection

Protótipo IoT para telemetria, detecção automatizada de anomalias e gestão operacional de redes de iluminação pública municipal.

---

## 📌 Visão Geral do Projeto

A interrupção de circuitos ou falhas pontuais em luminárias públicas geram insegurança para a população e lentidão na manutenção quando dependem apenas de chamados telefônicos de moradores. 

Este projeto propõe uma arquitetura escalável de ponta a ponta:
- **Telemetria de campo:** Captação de grandezas elétricas e status operacional de cada ponto de iluminação.
- **Detecção de falhas:** Notificação em tempo real de lâmpadas queimadas, desvios de consumo ou falta de alimentação.
- **Escalabilidade operacional:** Prova de conceito dimensionada para expandir facilmente de um cluster de ensaio para postes de um bairro ou de uma cidade inteira.

---

## 🏗️ Arquitetura do Sistema

```text
 [ Sensores / Pontos de Iluminação ]
                 │
                 ▼
       [ ESP32 (Microcontrolador) ]
                 │ (Publicação via MQTT / Wi-Fi)
                 ▼
      [ HiveMQ Broker (Nuvem) ]
                 │ (Inscrição em tópicos)
                 ▼
       [ Backend em Python / API ]
                 │ (Processamento & Lógica de Alerta)
                 ▼
   [ Dashboard Web (HTML / CSS / JS) ]
```

1. **Hardware (Edge):** O microcontrolador processa as leituras do sensor elétrico e publica pacotes periódicos com telemetria e alertas de acionamento.
2. **Mensageria (Broker):** O HiveMQ distribui mensagens de forma assíncrona entre campo e servidor sob o protocolo leve MQTT.
3. **Servidor (Backend):** Aplicação em Python ingere os dados, analisa anomalias (ex.: corrente nula com relé acionado indicando lâmpada queimada) e provê endpoints via API REST.
4. **Painel Operacional (Frontend):** Interface gráfica responsiva para os operadores monitorarem o mapa/status dos postes em tempo real.

---

## 🛠️️ Tecnologias e Ferramentas

### **Linguagens**
- **C / C++:** Programação embarcada e controle de periféricos no microcontrolador ESP32.
- **Python:** Backend, ingestão do broker, processamento analítico de regras de falha e rotas de API.
- **HTML5 & CSS3:** Interface web para supervisão e visualização de alarmes operacionais.

### **Ferramentas & Infraestrutura**
- **Hardware:** ESP32 SoC (Wi-Fi/Bluetooth nativo) + Módulos de sensoriamento.
- **Broker MQTT:** HiveMQ (Cloud ou Cluster local).
- **Ambientes de Desenvolvimento:** Visual Studio Code & Arduino IDE.
- **Comunicação:** Protocolo MQTT e APIs REST.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python instalado.
- Arduino IDE e configurado.
- Acesso ou credenciais a uma instância do HiveMQ Broker.