@echo off
:poczatek
cls
echo Tomasz Kalus
echo Projekt z Jezykow Skryptowych
echo --------------------------------------
echo  ####  #####   ##   #####  #    #  # 
echo #        #    #  #    #    #   #   # 
echo  ####    #   #    #   #    ####    # 
echo      #   #   ######   #    #  #    #    
echo #    #   #   #    #   #    #   #   # 
echo  ####    #   #    #   #    #    #  #                     
echo --------------------------------------
echo.
echo Wybierz opcje z menu ponizej:
echo.
echo 1) Uruchom skrypt dla plikow wejsciowych
echo 2) Kopia zapasowa raportu
echo 3) Informacje o projekcie
echo 4) Wyjscie
echo.
set /p opcja=wybierz:
if %opcja%==1 goto opcja1
if %opcja%==2 goto opcja2
if %opcja%==3 goto opcja3
if %opcja%==4 exit
goto zly_wybor
:opcja1
cls
echo Uruchamiam skrypt dla plikow wejsciowych
echo --------------------------------------
if not exist out mkdir out
for /f %%f in ('dir /b in') do ( 
   python main.py < in\%%f > out\%%f
   echo Przetwarzanie pliku %%f
)

echo.
echo Wygenerowano raport o nazwie:
python generate_report.py
echo.
pause
goto poczatek
:opcja2
cls
echo Wykonuje kopie zapasowa raportu
echo --------------------------------------
if not exist backup_%date% mkdir backup_%date%
forfiles /M raport*.html  /C "cmd /c copy @file backup_%date%"
echo Wykonano backup wszystkich raportow do folderu backup_%date%


pause
goto poczatek
:opcja3
cls
echo Informacje o projekcie:
echo --------------------------------------
echo Skrypt weryfikuje poprawnosc planszy do gry w Statki dla plikow znajdujacych sie w folderze in.
echo Wyniki walidacji sa zapisywane do folderu out oraz do raportu z odpowiednia data.
echo.
echo Tomasz Kalus (c) 2023
echo Informatyka, semestr III
echo Wydzial Matematyki Stosowanej
pause
goto poczatek
:zly_wybor
echo Opcja nieznana! Wybierz ponownie
pause 
goto poczatek