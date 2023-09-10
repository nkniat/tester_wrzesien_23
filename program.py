from funkcja_przelicznik import *
import funkcja_ryzyko, funkcja_rodzaj_inwestycji

#  Program przyjmuje ilosc pieniedzy w PLN i konweruje na USD
#  Program ustala akceptowalny poziom ryzyka na podstawie danych:
#  wiek, plec, wyksztalcenie
#  Program podpowiada w co inwestowac

#  funkcja przelicznik(int) konwertuje PLN na USD
kwota_w_USD = przelicznik(kwota)

#  funkcja poziom_ryzyka zwraca liczbę od 0 do 10, która okresla poziom ryzyka,
#  gdzie 0 - brak ryzyka; 10 - ekstremalnie wysokie ryzyko
ryzyko = funkcja_ryzyko.poziom_ryzyka(wiek, plec, wyksztalcenie)

#  funkcja na podstawie poziomu ryzyka i wysokosci kapitalu sugeruje w co inwestowac
funkcja_rodzaj_inwestycji.rodzaj_inwestycji(ryzyko, kwota_w_USD)
