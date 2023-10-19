# PAMETNI POZIVNIK
Namen projekta je narediti pametni gasilski pozivnik, za alarmiranje gasilcev ob gasilski intervenciji. Projekt obsega fizični radijski sprejemnik, ki prejme poziv in ga posreduje mobilni aplikaciji. Ta na podlagi nastavitev, ki jih nastavi gasilec, oblikuje obvestilo o pozivu.

## Use case diagram
![Usecase diagram pametnega pozivnika](https://github.com/puhi0210/VAJE/blob/main/Projekt/UseCaseDiagram.png)

### Akterji
Sistem v osnovi uporabljata dva akterja. Prvi je Regijski center za obveščanje. Ta ob intervenciji po radijski zvezi pošlje poziv gasilcem. Drugi akter je gasilec ki poziv prejme v obliki obvestila na mobilni napravi. Poleg tega lahko nastavi v kakšni obliki dobi poziv (utišanje opozoril za določen čas, geofence za prejemanje pozivov le v domačem kraju, ...).

### Aktivnosti
Aktivnosti sistema so sledeče:
- Alarmiranje gasilca: sistem prejme poziv po radijski zvezi, katerega izda Regijski center za obveščanje
- Obveščanje gasilca: gasilec na svoji mobilni napravi prejme obvestilo o pozivu
- Preverjanje nastavitev: aplikacija oblikuje obvestilo na podlagi nastavitev, lokacije, ure, ...
- Nastavljeanje lokacije: v applikaciji nastavimo lokacijo gasilske ga doma in največji radij v okolici doma, v kateri želimo prejeti poziv
- Nastavljanje urnika: v aplikaciji nastavimo, kdaj ne želimo prejeti obvestila (npr.: v času službe)

## Viri
Naslovi spletnih strani, uporabljenih za črpanje virov.
- Dekodiranje POCSAG z RTL-SDR: https://www.rtl-sdr.com/rtl-sdr-tutorial-pocsag-pager-decoding/
- Sending a message from Raspberry PI to Android device using Bluetooth: https://raspberrypi.stackexchange.com/questions/71149/sending-a-message-from-raspberry-pi-to-android-device-using-bluetooth