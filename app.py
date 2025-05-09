from core.checker import PasswordChecker
from core.hibp import HIBPChecker
from utils.report import PDFReport
import getpass

def main():
    print("=== Password Strength Checker ===")
    password = getpass.getpass("Digite a senha para análise: ")

    # Análise local
    checker = PasswordChecker(password)
    result = checker.analyze()

    # Verificação de vazamentos
    hibp = HIBPChecker()
    leaks = hibp.check(password)

    # Resultado
    print(f"\nPontuação: {result['score']}/4")
    print(f"Tempo para quebrar: {result['guess_time']}")
    print(f"Vazamentos: {'Não encontrados' if leaks == 0 else f'{leaks} vazamentos'}")

    # Gerar PDF
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