from core.checker import PasswordChecker
from core.hibp import HIBPChecker
from utils.report import PDFReport
import getpass
import sys

def main():
    print("=== DEBUG MODE ===")
    print("Sistema operacional:", sys.platform)
    print("Versão Python:", sys.version)
    
    try:
        password = getpass.getpass("Digite a senha para análise: ")
        print(f"Senha recebida: {'*'*len(password)} (tamanho: {len(password)})")
        
        checker = PasswordChecker(password)
        print("Iniciando análise...")
        result = checker.analyze()
        print("Análise concluída!")
        
        hibp = HIBPChecker()
        print("Verificando vazamentos...")
        leaks = hibp.check(password)
        print("Verificação de vazamentos concluída!")
        
        print("\nRESULTADOS:")
        print(f"Pontuação: {result['score']}/4")
        print(f"Tempo para quebrar: {result['guess_time']}")
        print(f"Vazamentos: {'Não encontrados' if leaks == 0 else f'{leaks} vazamentos'}")
        
        report = PDFReport()
        report.generate({
            'password': password,
            'score': result['score'],
            'guess_time': result['guess_time'],
            'leaks': leaks if leaks != -1 else "Erro na verificação"
        })
        print("\nRelatório gerado em report.pdf")
    
    except Exception as e:
        print(f"ERRO: {str(e)}", file=sys.stderr)

if __name__ == "__main__":
    main()