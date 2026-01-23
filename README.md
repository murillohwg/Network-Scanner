🛡️ Network Scanner Pro (Multiplataforma)

Uma ferramenta de auditoria de rede robusta e multiplataforma desenvolvida em Python. Combina a potência do Nmap com a automação de scripts para detectar dispositivos e vulnerabilidades em redes locais (Windows/Linux).

🚀 Funcionalidades Principais

Auto-Discovery Universal: Detecta automaticamente o IP local e a faixa de rede (Subnet) tanto no Windows quanto no Linux (Kali/Ubuntu), utilizando Sockets nativos para identificar a interface de saída correta.

Wrapper Nmap Otimizado: Executa varreduras rápidas (-T4) focadas na deteção de serviços e versões, geridas via subprocessos do sistema.

Auditoria Completa (Logs): Todas as varreduras e erros são registrados em scanner_ops.log, garantindo rastreabilidade histórica.

Tratamento de Erros: Verifica automaticamente se o Nmap está instalado no PATH do sistema antes de executar, fornecendo instruções claras caso esteja em falta.

🛠️ Como Usar

Pré-requisitos

Python 3.x instalado.

Nmap instalado e acessível no terminal:

Windows: Baixe em nmap.org

Linux: sudo apt install nmap

Instalação

git clone [https://github.com/SEU-USUARIO/Network-Scanner-Pro.git](https://github.com/SEU-USUARIO/Network-Scanner-Pro.git)
cd Network-Scanner-Pro


Execução

Basta rodar o script. Ele detectará a sua rede automaticamente.

python3 network_scanner.py


Nota: No Linux, recomenda-se o uso de sudo para uma deteção de Sistema Operativo (OS Fingerprinting) mais precisa.

📝 Logs e Relatórios

Logs: Consulte scanner_ops.log para histórico de execução e debugging.

Relatórios: Os resultados técnicos do Nmap são salvos na pasta relatorios_rede/ com carimbo de data/hora (ex: scan_2023-10-27_10-00.txt).

2023-10-27 10:00:01 - [INFO] - --- INICIANDO SCANNER (Linux) ---
2023-10-27 10:00:01 - [INFO] - IP Local detectado: 192.168.1.15
2023-10-27 10:00:05 - [INFO] - SUCESSO! Relatório salvo em: .../scan_2023...txt


⚠️ Aviso Legal (Disclaimer)

Esta ferramenta foi desenvolvida para fins educacionais e de administração de sistemas profissionais. O utilizador é responsável por garantir que possui permissão para auditar a rede alvo.

Desenvolvido como parte do portfólio de Segurança da Informação e SecOps.
