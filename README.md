# std_googleAssistant
This repository .... [describe what this repo. is for..]


#### [Google Assistant Instructions](https://github.com/UAEU-IRI/std_googleAssistant/wiki/Google-Assistant)

#### [Inmoov Assembly Instructions (right hand and forearm)](http://inmoov.fr/hand-and-forarm/)

#### Useful Links:

- RPi.GPIO documentaion

https://pypi.org/project/RPi.GPIO/

https://sourceforge.net/p/raspberry-gpio-python/wiki/Examples/

# launch command:
```
python hotword.py --project-id social-arm-69980 --device-model-id social-arm-69980-my-social-arm-9xnl96
```


# Behaviours table

| Behaviour        | Character           | Description  |
| ------------- |:-------------:| -----:|
| victory sign      | 'v' | close all fingers, but fully extend index and middle fingers    |
| show number 1      | '1' | close all fingers, but fully extend index finger    |
| show number 2      | '2' | same as victory sign    |
| show number 3      | '3' | fully extend index, middle, and ring fingers. close remaining fingers    |
| show number 4      | '4' | fully extend all fingers, but close the thumb   |
| show number 5      | '5' | fully extend all fingers   |
