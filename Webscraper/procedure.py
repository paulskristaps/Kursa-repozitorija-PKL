import os
import ruamel.yaml

#Procedūra, kas čeko vai pastāv konfigurācijas fails un uzģenerē jaunu ja nēeksistē

#Defaultie parametri konfig failam
def create_config(file_path):
    default_config = {
        'version': 1,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            }
        },
        'handlers': {
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'default',
                'filename': 'Webscraper/logfile.log',
                'level': 'DEBUG'
            }
        },
        'loggers': {
            'my_logger': {
                'level': 'DEBUG',
                'handlers': ['file']
            }
        }
    }

    #YAML faila konfigurācija
    yaml = ruamel.yaml.YAML()
    yaml.indent(offset=2)
    yaml.width = 4096

    #Izveido jaunu failu un saraksta konfigurāciju
    with open(file_path, 'w') as file:
        yaml.dump(default_config, file)

#Faila atrašanās vieta
config_file_path = "Webscraper/logging_config.yaml"

#Čeko vai fails jau pastāv
if not os.path.isfile(config_file_path):
    #Ja nē tad uztaisa
    create_config(config_file_path)

