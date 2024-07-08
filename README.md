
# Sierra_find_image_impref

this script done for geting ATcommands result in binary to comare it to given values for easy way.
some results of AT commands are decoding by default terminals, and when you work with strings in Python it easy to compare in identical string and not use with regex.
you need to run it in VSCODE in debbug modem and set brick point for result argumnet and copy it as binary.

this will provide you the actual value with raw values as "\r\n" values and correct whitspaces. 

'AT!IMPREF?\r\r\n!IMPREF: \r\n preferred fw version:    02.33.03.00\r\n preferred carrier name:  GENERIC\r\n preferred config name:   GENERIC_002.072_001\r\n preferred subpri index:  000\r\n current fw version:      02.33.03.00\r\n current carrier name:    GENERIC\r\n current config name:     GENERIC_002.072_001\r\n current subpri index:    000\r\n\r\nOK\r\n'


![image](https://github.com/elkanamol/Sierra_find_image_impref/assets/57934787/4d082594-af8f-4aea-b074-3eacf72dad89)



