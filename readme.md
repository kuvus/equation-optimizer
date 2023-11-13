# Optymalizator tinyGP
Narzędzie służące do optymalizacji wyjścia z tinyGP
## Uwagi
Program został przygotowany do optymalizacji wyjścia z tinyGP, oraz przystosowania go do działania w programie EXCEL w Języku Polskim, tj:
- Separatorem dziesiętnym na wyjściu programu jest przecinek
- Program nie obsługuje liczb stałych, liczba wejściowa musi zawierać separator dziesiętny (np. 1.0, 2.0, 3.0)
- Nazwy funkcji trygonometrycznych muszą być pisane małymi literami (sin, cos)
## Użycie
Program wymaga do działania Pythona w wersji 3.8 lub nowszej oraz zainstalowania poniższych zależności.   
### Instalacja zależności
```bash
pip install antlr4-python3-runtime
```
### Uruchomienie
```bash
python3 main.py <plik_wejsciowy> [plik_wyjsciowy]
```

Zoptymalizowane równanie zostanie wyświetlone na wyjściu standardowym, oraz jeśli została podana ścieżka, zostanie zapisany w pliku wyjściowym.