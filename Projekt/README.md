# PAMETNI POZIVNIK
Namen projekta je narediti aplikacijo, za alarmiranje gasilcev ob gasilski intervenciji. Projekt obsega fizični radijski sprejemnik, ki prejme poziv in ga posreduje mobilni aplikaciji. 

OPOZORILO!: Python skripta še ni preizkušena z log datoteko programa PWR, kar pomeni da projekt še ne deluje kot zastavljeno.

## Kazalo
- [Use case diagram](#uml)
    - [Akterji](#akterji)
    - [Aktivnosti](#aktivnosti)
- [Izvedba](#izvedba)
- [Viri](#viri)

## Use case diagram <a name="uml"></a>
![Usecase diagram pametnega pozivnika](Projekt\images\UseCaseDiagram.png)

### Akterji <a name="akterji"></a>
Sistem v osnovi uporabljata dva akterja. Prvi je Regijski center za obveščanje. Ta ob intervenciji po radijski zvezi pošlje poziv gasilcem. Drugi akter je gasilec ki poziv prejme v obliki obvestila na mobilni napravi. Tretji akrter je socialno omrežje Telegram, ki iz strani strežnika prejeto sporočilo posreduje gasilcu.

### Aktivnosti <a name="aktivnosti"></a>
Aktivnosti sistema so sledeče:
- Alarmiranje gasilca: sistem prejme poziv po radijski zvezi, katerega izda Regijski center za obveščanje
- Obdelava sporočila: sistem obdela sporočilo, in ga posreduje Telegramu
- Obveščanje gasilca: gasilec na svoji mobilni napravi od Telegrama prejme obvestilo o pozivu

## Izvedba <a name='izvedba'>
Projekt sem izvedel s pomočjo SDR sprejemnika priključenega na osebni računalnik. Za FM demodulacijo signala iz SDR vmesnika sem uporabil SDRSharp/Airspy, ki sem ga s pomočjo programa Voicemeeter pretvoril v virtualni Aux vhod. Tako sem baseband signala pripeljal na PDW Paging Decoding Software. Ko PDW dekodira POCSAG sporočilo ga zapiše v .log datoteko. Python skripta deluje tako, da zaznava spremembe log datoteke, ki jih interpretira kot nove pozive. Te nato preko HTTP request-a pošlje sporočilo Telegram Botu.

SDR vmesnik:
![SDR vmesnik](Projekt\images\sdr.jpg)

SDRSharp:
![SDRSharp](Projekt\images\sdrsharp.png)

PDW Paging Decoder Software:
![SDRSharp](Projekt\images\pdw.png)

Prejem sporočila na telegram:
![SDRSharp](Projekt\images\telegram.png)

## Viri <a name="viri"></a>
Programska oprema: 
- SDRSharp/Airspy: https://airspy.com/download/
- Voicemeeter: https://vb-audio.com/Voicemeeter/
- PDW Paging Decoder Software: https://www.discriminator.nl/pdw/index-en.html

Naslovi spletnih strani, uporabljenih za črpanje virov.
- Dekodiranje POCSAG z RTL-SDR: https://www.rtl-sdr.com/rtl-sdr-tutorial-pocsag-pager-decoding/
- Sending a message from Raspberry PI to Android device using Bluetooth: https://raspberrypi.stackexchange.com/questions/71149/sending-a-message-from-raspberry-pi-to-android-device-using-bluetooth
- Dekodiranje POCSAG z Raspberry Pi: https://github.com/cmar0ck/RasPOC
