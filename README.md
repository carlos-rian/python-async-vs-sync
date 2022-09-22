# TestAsyncPython

## Configurar
Crie um ambiente virtual.

```
virtualenv -p python3.8.2 .venv
source .venv/bin/activate
pip install -r requirements
```

## Executar
```
python main.py
or 
python test_async.py
or
python test_sync.py
```

## Adendo
Caso use a viacep, altere o import do serializador para CepSerial apenas. url: http://viacep.com.br/ws/01001000/json/unicode/