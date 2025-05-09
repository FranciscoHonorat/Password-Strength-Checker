from core.checker import PasswordChecker
from core.hibp import HIBPChecker  # Corrigido aqui
from utils.report import PDFReport
import getpass

def main():
    print("=== Passaword Strength Checker===")
    password = getpass.getpass("Digite a senha para análise: ")

    #análise local
    checker = PasswordChecker(password)
    result = checker.analyze()

    hibp = HIBPChecker()
    leaks = hibp.check(password)

    #resultado
    print(f"\nPontuação: {result['scorre']}/4")
    print(f"Tempo para quebrar: {result['guess_time']}")
    print(f"vazamentos {'Não encontramos' if leaks == 0 else f'{'leaks'} vazamentos'}")

    #gerar pdf
    report = PDFReport()
    report.generate({
        'password': password,
        'score': result['score'],
        'guess_time': result['guess_time'],
        'leaks': leaks if leaks != -1 else "Erro na verificação"
    })
    print("\nRelatório gerado em report.pdf")

    if __name__ == "__main__":
        main()