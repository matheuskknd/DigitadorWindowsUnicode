# DigitadorWindowsUnicode

Este repositório contém um script standalone que simplesmente digita como se fosse no teclado o que for colocado na variável `texto` após 5 segundos. Funciona pra qualquer texto com caracteres Unicode codificados em UTF-8.

## <a name="python_environment"></a>Python environment

Para garantir que todas as dependências estejam instaladas corretamente, execute os seguintes comandos dentro da raiz do repositório antes de usar o script:

Bash

```bash
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --upgrade "pip<26" "setuptools<80"
python -m pip install -r requirements.txt
```

CMD

```bash
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade "pip<26" "setuptools<80"
python -m pip install -r requirements.txt
```

Power Shell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade "pip<26" "setuptools<80"
python -m pip install -r requirements.txt
```

Cheque a instalação. O seguinte comando deve mostrar todas as dependências:

```bash
python -m pip freeze
```
