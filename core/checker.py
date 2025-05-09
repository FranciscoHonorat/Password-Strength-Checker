import zxcvbn
from datetime import datetime

class PasswordChecker:
    def __init__(self, password):
        self.password = password
        self.result = None
    
    def analyze(self):
        try:
            self.result = zxcvbn.zxcvbn(self.password)
            
            # Verificação segura da estrutura de dados
            crack_times = self.result.get('crack_times_display', {})
            
            return {
                'score': self.result.get('score', 0),
                'guess_time': self.format_time(crack_times.get('offline_slow_hashing', 'seconds')),
                'feedback': self.result.get('feedback', {}).get('warning', "Sem problemas detectados"),
                'suggestions': self.result.get('feedback', {}).get('suggestions', [])
            }
        except Exception as e:
            print(f"Erro na análise: {str(e)}")
            return {
                'score': 0,
                'guess_time': 'indeterminado',
                'feedback': "Erro na análise",
                'suggestions': []
            }
    
    def format_time(self, time_str):
        """Formata '3 hours' para '3 horas'"""
        translations = {
            'second': 'segundo', 'seconds': 'segundos',
            'minute': 'minuto', 'minutes': 'minutos',
            'hour': 'hora', 'hours': 'horas',
            'day': 'dia', 'days': 'dias',
            'month': 'mês', 'months': 'meses',
            'year': 'ano', 'years': 'anos'
        }
        for eng, pt in translations.items():
            time_str = time_str.replace(eng, pt)
        return time_str