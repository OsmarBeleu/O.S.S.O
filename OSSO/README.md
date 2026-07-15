# Profissionalismo
Exatamente! Olhe como sou profissional!

# Testes
Eu estarei usando este documento para apresentar coisas novas, testes, compartilhar comandos ou sei-lá-o-que que eu ache *possível* (talvez só acrescente algo porque sim) compartilhar por aqui.

# Passo-a-passo para compilar
Você precisa dos pacotes `gcc g++ gdb make cmake libwxgtk3.2-dev libwxgtk-media3.2-dev libboost-dev` como pré-requisito para conseguir compilar o projeto.
Além disso, também é necessário o pacote de extensão [Extension Pack for C/C++](https://open-vsx.org/vscode/item?itemName=KylinIdeTeam.kylin-cpp-pack) no "VS Code".

Instalados esses, abra o projeto na pasta `OSSO`, caso pedido escolha o compilador `gcc` e abra `CMakeLists.txt`. Então... eu sinceramente não sei direito como isso deve ser feito, mas isto funciona:

- Clique na aba superior (escrito OSSO; para pesquisa e execução de comandos)
- Execute `>Tasks: Configure Task`
- Apague qualquer edição que for feita ao arquivo `tasks.json` (será aberto imediatamente)
- Pule num pé só
- Volte ao `CMakeLists.txt`
- Dê `Ctrl + S` com o terminal do "VS Code" aberto

Caso várias coisas apareçam no terminal... Parabéns! Funcionou. Agora o CLang estará funcionando e você pode conferir isso abrindo `main.cpp`, que terá nenhum erro de sintaxe.
Caso nada aconteça... Bem, tente reabrir o "VS Code" (feche com o `CMakeLists.txt` aberto. Se não abrir nele é garantido não funcionar) e repetir o último passo.
Caso nada aconteça... Tente o passo-a-passo novamente, mas pule no outro pé.

# Parabéns!
Se tudo deu completamente errado no tópico anterior e você não quer chorar, chore!
Se tudo deu completamente errado no tópico anterior e você está chorando, ótimo! Não prossiga lendo!

Você tem o wxWidgets lindamente configurado! Vitória!
Agora será necessário baixar o wxFormBuilder, uma aplicação visual para editar o maravilhoso `.fbp` e com ele criar a interface.
> Nota: não, em hipótese alguma, exporte algo do wxFormBuilder. Apenas salve o projeto com `Ctrl + S` (sem fazer muito barulho), copie o código necessário da aba `XRC` e cole no arquivo `.xrc`.
> Ah, e também você consegue prever a janela com `F5`

Toodle-pip!