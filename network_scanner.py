#!/usr/bin/env python3
import os
import datetime
import subprocess
import sys
import logging
import socket
import platform

# --- CONFIGURAÇÃO DE LOGS ---
LOG_FILE = 'scanner_ops.log'

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [%(levelname)s] - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger()

class NetworkScanner:
    def __init__(self, output_dir="relatorios_rede"):
        # Garante caminho absoluto compatível com qualquer SO
        self.output_dir = os.path.join(os.getcwd(), output_dir)
        if not os.path.exists(self.output_dir):
            try:
                os.makedirs(self.output_dir)
            except OSError as e:
                logger.error(f"Erro ao criar pasta: {e}")

    def _get_local_ip_range(self):
        """
        Descobre o IP local de forma UNIVERSAL (Windows/Linux/Mac).
        Usa um socket para detectar a interface de saída correta.
        """
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Não conecta realmente, apenas define a rota para descobrir o IP
            s.connect(("8.8.8.8", 80))
            local_ip = s.getsockname()[0]
            s.close()
            
            # Assume uma máscara /24 (padrão doméstico/PME)
            # Transforma "192.168.1.15" -> "192.168.1.0/24"
            ip_parts = local_ip.split('.')
            base_ip = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}.0/24"
            
            logger.info(f"IP Local detectado: {local_ip}")
            logger.info(f"Range de Scan calculado: {base_ip}")
            return base_ip
        except Exception as e:
            logger.error(f"Não foi possível detectar IP local: {e}")
            return None

    def check_nmap_installed(self):
        """Verifica se o Nmap está instalado e acessível no sistema."""
        system_platform = platform.system()
        # No Windows usa 'where', no Linux usa 'which'
        check_cmd = ["where", "nmap"] if system_platform == "Windows" else ["which", "nmap"]
        
        try:
            subprocess.check_output(check_cmd, stderr=subprocess.DEVNULL)
            return True
        except subprocess.CalledProcessError:
            return False

    def run_scan(self, target=None):
        logger.info(f"--- INICIANDO SCANNER ({platform.system()}) ---")
        
        # Verifica se o Nmap existe antes de tentar rodar
        if not self.check_nmap_installed():
            logger.critical("ERRO: Nmap não encontrado no sistema!")
            logger.info("Windows: Instale em https://nmap.org/download.html")
            logger.info("Linux: Execute 'sudo apt install nmap'")
            return False

        if not target:
            target = self._get_local_ip_range()
            if not target:
                logger.error("Abortado: Alvo não definido.")
                return

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
        output_file = os.path.join(self.output_dir, f"scan_{timestamp}.txt")

        logger.info(f"Executando Nmap em {target}...")
        
        # Comando universal
        # shell=True é necessário para funcionar bem em ambos os ambientes com argumentos
        cmd = f"nmap -sV -T4 --open {target} -oN \"{output_file}\""
        
        try:
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                logger.info(f"SUCESSO! Relatório salvo em: {output_file}")
                return True
            else:
                logger.error(f"Erro Nmap: {stderr.decode(errors='ignore')}")
                return False
        except Exception as e:
            logger.critical(f"Erro execução: {e}")
            return False

if __name__ == "__main__":
    scanner = NetworkScanner()
    scanner.run_scan()
