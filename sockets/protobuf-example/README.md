
# Criando um virtualenv

Para criar um virtualenv, execute o comando `python3 -m venv venv`. Isso irá criar um virtualenv chamado venv.

# Ativando o virtualenv criado

Para ativar o virtualenv criado, execute o comando a seguir (na mesma pasta em que você executou o passo anterior):

`source venv/bin/activate`

Após esse comando, o seu terminal deverá mudar, contendo um indicativo (venv) no inicio da linha.

# Instalando protobuf

Virtualenvs são importantes para que libs instaladas fiquem localmente no projeto atual. Logo, podemos instalar a 
biblioteca do protobuf sem problemas usando o `pip`

Para tal, execute o comando `pip install protobuf` **com o virtualenv ativado**.

# Compilando arquivo proto

Para compilar o arquivo .proto no diretório atual, entre na pasta "protobuf-exemple" e invoque o protoc para compilar o 
arquivo .proto:

`./protobuf/bin/protoc -I . --python_out . addressbook.proto`

O protoc pode estar em qualquer caminho do seu sistema, portanto, o comando acima irá variar de acordo com onde você tiver
salvado o protoc. Ou seja, uma forma geral do comando é:

`./caminho/para/protoc/bin/protoc -I . --python_out . addressbook.proto`