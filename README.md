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
| ------------- |:-------------:| :-----|
| victory or peace sign      | 'v' | close all fingers, but fully extend index and middle fingers    |
| show number 1      | '1' | close all fingers, but fully extend index finger    |
| show number 2      | '2' | same as victory sign    |
| show number 3      | '3' | fully extend index, middle, and ring fingers. close remaining fingers    |
| show number 4      | '4' | fully extend all fingers, but close the thumb   |
| show number 5      | '5' | fully extend all fingers   |
| Hand Wake up | 'w' | fully extends all fingers, or the wrist rotates 5 degrees clock wise and -5 degrees counter clockwise and back to zero degree (shake wrist)|
| Response Finish | 'r' | Relax fingers, fingers close a little |
| Count numbers from 1 to 5 | 'c' | Extend one finger after another till all fingers is extended|
| thumb up | 't' | close all fingers but fully extend thumb |
| Hi | 'h' | extend  and extend all fingers or move wrist |
| bye | 'b' | move wrist |
| close hand | 'l' | close all fingers   |
| open hand | 'o' | fully extend all fingers   |
| Play Rock Paper Scissor | 'p' | the hand choose randomly between rock paper scissor and user press buttons to decide his move |
| Play Memory Sequence | 's' | the hand do random numbers for example 345 and user try to remember and press buttons to decide the numbers sequence he remembered |
| Have a good day | 'u' | bye function   |


# Behaviours table from ARD to RPI

| Character        | Description | 
| ------------- | :-----| 
| 'l'     | play loss song | 
| 'w'     | play win song | 
| 't'     | play same song | 
| 'a'     | play loss song for memory game | 
| 'b'     | play win song for memory game| 
| 'c'     | count the number of fingers that arm have| 
| 'm'     | after we ask about hand sign of shaikh Mohammad  | 
| 'i'     | hand sign of shaikh Mohammad "Win" |
| 'v'     | hand sign of shaikh Mohammad "Victory" | 
| 'e'     | hand sign of shaikh Mohammad "Love" |
