from fpdf import FPDF

class PDFReport:
    def generate(self, data, filename="report.pdf"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        #titulo
        pdf.cell(200, 10, txt="Relatorio de Segurança de Senha", ln=1, align='C')

        #dados
        pdf.cell(200, 10, txt=f"Senha testada: {'*'*len(data['password'])}", ln=1)
        pdf.cell(200, 10, txt=f"Nivel de Segurança: {data['score']}/4, ln=1"),
        pdf.cell(200, 10, txt=f"tempo estimado para quebrar: {data['guess_time']}", ln=1)
        pdf.cell(200, 10, txt=f"Vazamentos encontrados: {data['leaks']} vezes, ln=1")

        