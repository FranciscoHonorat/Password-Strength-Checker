import hashlib
import requests

class HIBPChecker:
    API_URL = "https://api.pwnedpasswords.com/range/"
    
    def check(self, password):
        sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
        prefix, suffix = sha1_hash[:5], sha1_hash[5:]
        
        try:
            response = requests.get(f"{self.API_URL}{prefix}", timeout=5)
            if response.status_code == 200:
                return self._process_response(response.text, suffix)
            return 0
        except Exception:
            return -1  # Erro na requisição
    
    def _process_response(self, response_text, suffix):
        for line in response_text.splitlines():
            if line.startswith(suffix):
                return int(line.split(':')[1])
        return 0