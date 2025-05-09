import zxcvbn
from datetime import datetime

class PasswordChecker:
    def __init__(self, password):
        self.password = password
        self.result = None

    def analyze(self):
        self.result = zxcvbn.zxcvbn(self.password)
        return {
            'score': self.result['score'],
            'guess_time': self._format_time(self.result['crack_times']['offline_slow_hashing']),
            'feedback': self.result['feedback']['warning'] or 'Sem problemas detectados',
            'suggestions': self.result['feedback']['suggestions']
        }
    
    def format_time(self, time_str):
        """Formata '3hours' para '3horas'"""
        translations = {'second': 'segundo', 'minute': 'minuto', 'hour': 'hora',
                        'day': 'dia', 'month': 'mês', 'year': 'ano'}
        for eng, pt in translations.items():
            time_str = time_str.replace(eng, pt)
        
        return time_str
    