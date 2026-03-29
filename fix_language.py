"""Run this script to translate all Swedish to English in code."""
import os

TRANSLATIONS = {
    "Analysera": "Analyze", "analysera": "analyze",
    "Säkerhet": "Security", "säkerhet": "security", "säkerhets": "security",
    "Kostnad": "Cost", "kostnad": "cost",
    "Minne": "Memory", "minne": "memory",
    "Juridisk": "Legal", "juridisk": "legal",
    "Beräkna": "Calculate", "beräkna": "calculate",
    "Kontrollera": "Check", "kontrollera": "check",
    "Hämta": "Get", "hämta": "get",
    "Spara": "Save", "spara": "save",
    "Skapa": "Create", "skapa": "create",
    "Generera": "Generate", "generera": "generate",
    "Returnera": "Return", "returnera": "return",
    "Uppdatera": "Update", "uppdatera": "update",
    "Radera": "Delete", "radera": "delete",
    "Verifiera": "Verify", "verifiera": "verify",
    "Validera": "Validate", "validera": "validate",
    "Öppna": "Open", "öppna": "open",
    "Stäng": "Close", "stäng": "close",
    "Kör": "Run", "kör": "run",
    "Starta": "Start", "starta": "start",
    "Stoppa": "Stop", "stoppa": "stop",
    "Hitta": "Find", "hitta": "find",
    "Tillåt": "Allow", "tillåt": "allow",
    "Blockera": "Block", "blockera": "block",
    "Filtrera": "Filter", "filtrera": "filter",
    "Sortera": "Sort", "sortera": "sort",
    "Sammanfatta": "Summarize", "sammanfatta": "summarize",
    "Jämför": "Compare", "jämför": "compare",
    "Utvärdera": "Evaluate", "utvärdera": "evaluate",
    "Rekommendera": "Recommend", "rekommendera": "recommend",
    "Förbättra": "Improve", "förbättra": "improve",
    "Optimera": "Optimize", "optimera": "optimize",
}

count = 0
for root, dirs, files in os.walk("backend"):
    for f in files:
        if f.endswith('.py') and 'test_' not in f:
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
            original = content
            for sv, en in TRANSLATIONS.items():
                content = content.replace(sv, en)
            if content != original:
                with open(path, 'w', encoding='utf-8') as fh:
                    fh.write(content)
                count += 1

print(f"Translated {count} files to English")
print("Run: python fix_language.py")
