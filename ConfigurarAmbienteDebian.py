import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {command}")
        print(e)
        exit(1)

def install_telegram():
    print("-----------------------------------------------------------------------------")
    print("Instalando Telegram")
    print("-----------------------------------------------------------------------------")
    run_command("wget -O Telegram_4.8.10.tar.xz https://updates.tdesktop.com/tlinux/tsetup.4.8.10.tar.xz")
    run_command("tar -xJf Telegram_4.8.10.tar.xz")
    run_command("sudo apt update && sudo apt upgrade")
    run_command("cd Telegram && sudo mv Telegram /usr/bin")
    run_command(" rm -f Telegram_4.8.10.tar.xz && rm -r Telegram" )


def install_vscode():
    print("-----------------------------------------------------------------------------")
    print("Baixando Vscode ")
    print("-----------------------------------------------------------------------------")






    run_command("wget -O code_1.80.2.deb https://az764295.vo.msecnd.net/stable/2ccd690cbff1569e4a83d7c43d45101f817401dc/code_1.80.2-1690491597_amd64.deb && sudo dpkg -i ./code_1.80.2.deb && rm code_1.80.2.deb")
   
def config_bash():
    print("-----------------------------------------------------------------------------")
    print("Configurando Terminal")
    print("-----------------------------------------------------------------------------")


    config = r"""# ~/.bashrc: executado pelo bash(1) para shells não-login.
        # Veja /usr/share/doc/bash/examples/startup-files (no pacote bash-doc) para exemplos.

        # Se não estiver sendo executado interativamente, não faça nada.
        case $- in
            *i*) ;;
            *) return;;
        esac

        # Não coloque linhas duplicadas ou linhas que comecem com espaço no histórico.
        # Consulte o bash(1) para mais opções.
        HISTCONTROL=ignoreboth

        # Anexar ao arquivo de histórico, não sobrescrevê-lo.
        shopt -s histappend

        # Defina o tamanho do histórico (quantidade de comandos armazenados).
        HISTSIZE=1000
        HISTFILESIZE=2000

        # Verificar o tamanho da janela após cada comando e, se necessário,
        # atualizar os valores de LINES e COLUMNS.
        shopt -s checkwinsize

        # Se estiver definido, o padrão "**" usado em expansão de pathname corresponderá a todos os arquivos,
        # diretórios e subdiretórios.
        #shopt -s globstar

        # Facilitar a leitura de arquivos de entrada não-textuais, consulte lesspipe(1).
        #[ -x /usr/bin/lesspipe ] && eval "$(SHELL=/bin/sh lesspipe)"

        # Definir a variável debian_chroot se o arquivo /etc/debian_chroot existir e for legível.
        if [ -z "${debian_chroot:-}" ] && [ -r /etc/debian_chroot ]; then
            debian_chroot=$(cat /etc/debian_chroot)
        fi

        # Definir um prompt elegante (sem cor, a menos que seja suportado).
        case "$TERM" in
            xterm-color|*-256color) color_prompt=yes;;
        esac

        # Descomente para ter um prompt colorido, se o terminal tiver essa capacidade; desligado por padrão para não distrair o usuário.
        # O foco em uma janela do terminal deve estar na saída dos comandos, não no prompt.
        force_color_prompt=yes

        if [ -n "$force_color_prompt" ]; then
            if [ -x /usr/bin/tput ] && tput setaf 1 >&/dev/null; then
                # Temos suporte a cores; assumimos que é compatível com Ecma-48 (ISO/IEC-6429).
                # (A falta desse suporte é extremamente rara, e tal caso tenderia a suportar setf em vez de setaf.)
                color_prompt=yes
            else
                color_prompt=
            fi
        fi

        # O seguinte bloco é cercado por dois delimitadores.
        # Esses delimitadores não devem ser modificados. Obrigado.
        # INÍCIO DAS VARIÁVEIS DE CONFIGURAÇÃO DO KALI
        PROMPT_ALTERNATIVE=twoline
        NEWLINE_BEFORE_PROMPT=yes
        # FIM DAS VARIÁVEIS DE CONFIGURAÇÃO DO KALI

        if [ "$color_prompt" = yes ]; then
            # Substituir o indicador padrão do virtualenv no prompt.
            VIRTUAL_ENV_DISABLE_PROMPT=1

            prompt_color='\[\033[;32m\]'
            info_color='\[\033[1;34m\]'
            prompt_symbol='🎩'
            if [ "$EUID" -eq 0 ]; then # Alterar as cores do prompt para o usuário root
                prompt_color='\[\033[;94m\]'
                info_color='\[\033[1;31m\]'
                prompt_symbol='🍷🗿'
            fi
            case "$PROMPT_ALTERNATIVE" in
                twoline)
                    PS1=$prompt_color'┌──${debian_chroot:+($debian_chroot)──}${VIRTUAL_ENV:+(\[\033[0;1m\]$(basename $VIRTUAL_ENV)'$prompt_color')}('$info_color'\u'$prompt_symbol'\h'$prompt_color')-[\[\033[0;1m\]\w'$prompt_color']\n'$prompt_color'└──'$info_color'\$\[\033[0m\] ';;
                oneline)
                    PS1='${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV)) }${debian_chroot:+($debian_chroot)}'$info_color'\u@\h\[\033[00m\]:'$prompt_color'\[\033[01m\]\w\[\033[00m\]\$ ';;
                backtrack)
                    PS1='${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV)) }${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ ';;
            esac
            unset prompt_color
            unset info_color
            unset prompt_symbol
        else
                # Substituir o indicador padrão do virtualenv no prompt.
            VIRTUAL_ENV_DISABLE_PROMPT=1

            prompt_color='\[\033[;32m\]'
            info_color='\[\033[1;34m\]'
            prompt_symbol='🎩'
            if [ "$EUID" -eq 0 ]; then # Alterar as cores do prompt para o usuário root
                prompt_color='\[\033[;1;94m\]'

                info_color='\[\033[1;31m\]'
                prompt_symbol='🍷🗿'
            fi
            case "$PROMPT_ALTERNATIVE" in
                twoline)
                    PS1=$prompt_color'┌──${debian_chroot:+($debian_chroot)──}${VIRTUAL_ENV:+(\[\033[0;1m\]$(basename $VIRTUAL_ENV)'$prompt_color')}('$info_color'\u'$prompt_symbol'\h'$prompt_color')-[\[\033[0;1m\]\w'$prompt_color']\n'$prompt_color'└──'$info_color'\$\[\033[0m\] ';;
                oneline)
                    PS1='${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV)) }${debian_chroot:+($debian_chroot)}'$info_color'\u@\h\[\033[00m\]:'$prompt_color'\[\033[01m\]\w\[\033[00m\]\$ ';;
                backtrack)
                    PS1='${VIRTUAL_ENV:+($(basename $VIRTUAL_ENV)) }${debian_chroot:+($debian_chroot)}\[\033[01;31m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ ';;
            esac
            unset prompt_color
            unset info_color
            unset prompt_symbol
        fi
        unset color_prompt force_color_prompt

        # Se este for um terminal xterm, defina o título para user@host:dir.
        case "$TERM" in
        xterm*|rxvt*|Eterm|aterm|kterm|gnome*|alacritty)
            PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
            ;;
        *)
            ;;
        esac

        [ "$NEWLINE_BEFORE_PROMPT" = yes ] && PROMPT_COMMAND="PROMPT_COMMAND=echo"

        # Habilitar suporte a cores no ls, less e man, e também adicionar aliases úteis.
        if [ -x /usr/bin/dircolors ]; then
            test -r ~/.dircolors && eval "$(dircolors -b ~/.dircolors)" || eval "$(dircolors -b)"
            export LS_COLORS="$LS_COLORS:ow=30;44:" # Corrige a cor do ls para pastas com permissões 777

            alias ls='ls --color=auto'
            #alias dir='dir --color=auto'
            #alias vdir='vdir --color=auto'

            alias grep='grep --color=auto'
            alias fgrep='fgrep --color=auto'
            alias egrep='egrep --color=auto'
            alias diff='diff --color=auto'
            alias ip='ip --color=auto'

            export LESS_TERMCAP_mb=$'\E[1;31m'     # começa piscando
            export LESS_TERMCAP_md=$'\E[1;36m'     # começa negrito
            export LESS_TERMCAP_me=$'\E[0m'        # restaura negrito/piscando
            export LESS_TERMCAP_so=$'\E[01;33m'    # começa vídeo invertido
            export LESS_TERMCAP_se=$'\E[0m'        # restaura vídeo invertido
            export LESS_TERMCAP_us=$'\E[1;32m'     # começa sublinhado
            export LESS_TERMCAP_ue=$'\E[0m'        # restaura sublinhado
        fi

        # GCC com mensagens e erros coloridos.
        #export GCC_COLORS='error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01'

        # Alguns aliases para o ls.
        alias ll='ls -l'
        alias la='ls -A'
        alias l='ls -CF'

        # Definições de aliases.
        # Você pode querer colocar todas as suas adições em um arquivo separado, como ~/.bash_aliases, em vez de adicioná-las aqui diretamente.
        # Veja /usr/share/doc/bash-doc/examples no pacote bash-doc.
        if [ -f ~/.bash_aliases ]; then
            . ~/.bash_aliases
        fi

        # Habilitar recursos de conclusão programável (não é necessário habilitar novamente se já estiver habilitado em /etc/bash.bashrc e /etc/profile sources /etc/bash.bashrc).
        if ! shopt -oq posix; then
        if [ -f /usr/share/bash-completion/bash_completion ]; then
            . /usr/share/bash-completion/bash_completion
        elif [ -f /etc/bash_completion ]; then
            . /etc/bash_completion
        fi
        fi
        """


    
    # Obtendo o nome de usuário atual
    import os
    username = os.getlogin()

    # Definindo os caminhos do arquivo .bashrc
    user_bashrc_path = f'/home/{username}/.bashrc'
    root_bashrc_path = '/root/.bashrc'

    # Escrevendo o conteúdo no arquivo .bashrc do usuário
    with open(user_bashrc_path, 'w') as bashrc_file:
        bashrc_file.write(config)

    # Copiando o arquivo do usuário para o diretório root e ajustando as permissões
    run_command(f"sudo cp {user_bashrc_path} {root_bashrc_path} && sudo chown root:root {root_bashrc_path}")


def install_githubdesktop():
      
    print("-----------------------------------------------------------------------------")
    print("Baixando GitHub-Desktop")
    print("-----------------------------------------------------------------------------")





    run_command("wget -qO - https://apt.packages.shiftkey.dev/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/shiftkey-packages.gpg > /dev/null")
    run_command("sudo sh -c 'echo \"deb [arch=amd64 signed-by=/usr/share/keyrings/shiftkey-packages.gpg] https://apt.packages.shiftkey.dev/ubuntu/ any main\" > /etc/apt/sources.list.d/shiftkey-packages.list'")
    run_command("sudo apt update && sudo apt install github-desktop")


def install_virtualbox():
    print("-----------------------------------------------------------------------------")
    print("Baixando virtualbox e configurando.")
    print("-----------------------------------------------------------------------------")






    run_command("wget -O virtualbox.deb https://download.virtualbox.org/virtualbox/7.0.10/virtualbox-7.0_7.0.10-158379~Debian~bookworm_amd64.deb")
    run_command("sudo apt install gcc make perl linux-headers-amd64 linux-headers-$(uname -r)")
    run_command("sudo apt install python3-distutils")
    run_command("sudo chmod +x virtualbox.deb")
    run_command("sudo apt install ./virtualbox.deb")
    run_command("sudo /sbin/vboxconfig")
    run_command("rm -f virtualbox.deb")


def install_pycharm():

    print("-----------------------------------------------------------------------------")

    print("Instalando o instalador do pycharm Pycharm")
    print("-----------------------------------------------------------------------------")


    run_command("wget https://download-cdn.jetbrains.com/toolbox/jetbrains-toolbox-2.0.1.16621.tar.gz")
    run_command("sudo tar -xzf jetbrains-toolbox-2.0.1.16621.tar.gz -C /usr/bin/ &&  rm -r jetbrains-toolbox-2.0.1.16621.tar.gz && sudo mv /usr/bin/jetbrains-toolbox-2.0.1.16621/jetbrains-toolbox  /usr/bin/ && jetbrains-toolbox")






def main():
    run_command("sudo apt update && sudo apt upgrade && clear")
    print("-----------------------------------------------------------------------------")
    print("Configurando meu Ambiente Debian")
    print("-----------------------------------------------------------------------------")
    
    while True:
        apps = [
            "1. Telegram",
            "2. Instalador Pycharm",
            "3. Vscode",
            "4. Configurar Terminal estilo kali Linux",
            "5. Virtual Box",
            "6. GitHub Desktop",
            "0. Sair"
        ]
        
        print("Qual aplicação instalar:")
        for app in apps:
            print(app)
        
        op = input("\t\t\t\t\t->>> ")
        
        if op == "0":
            break
        elif op == "1":
            install_telegram()
        elif op == "2":
            install_pycharm()
        elif op == "3":
            install_vscode()
        elif op == "4":
            config_bash()
        elif op == "5":
            install_virtualbox()
        elif op == "6":
            install_githubdesktop()
        else:
            continue
        
    print("-----------------------------------------------------------------------------")
    print("Concluído ...")
    print("-----------------------------------------------------------------------------")

if __name__ == "__main__":
    main()
s
