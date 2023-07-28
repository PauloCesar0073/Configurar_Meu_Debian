import subprocess

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o comando: {command}")
        print(e)
        exit(1)

print("-----------------------------------------------------------------------------")
print("Configurando meu Ambiente Debian")
print("-----------------------------------------------------------------------------")

print("atualizando...")
print("-----------------------------------------------------------------------------")
run_command("sudo apt update && sudo apt upgrade")

print("-----------------------------------------------------------------------------")
print("Baixando Vscode versão 1.80.2")
print("-----------------------------------------------------------------------------")
run_command("wget -O code_1.80.2.deb https://az764295.vo.msecnd.net/stable/2ccd690cbff1569e4a83d7c43d45101f817401dc/code_1.80.2-1690491597_amd64.deb && sudo dpkg -i ./code_1.80.2.deb && rm code_1.80.2.deb")

print("-----------------------------------------------------------------------------")
print("Baixando GitHub-Desktop")
print("-----------------------------------------------------------------------------")
run_command("wget -qO - https://apt.packages.shiftkey.dev/gpg.key | gpg --dearmor | sudo tee /usr/share/keyrings/shiftkey-packages.gpg > /dev/null")
run_command("sudo sh -c 'echo \"deb [arch=amd64 signed-by=/usr/share/keyrings/shiftkey-packages.gpg] https://apt.packages.shiftkey.dev/ubuntu/ any main\" > /etc/apt/sources.list.d/shiftkey-packages.list'")
run_command("sudo apt update && sudo apt install github-desktop")

print("-----------------------------------------------------------------------------")
print("Baixando virtualbox 7.0.10 e configurando.")
print("-----------------------------------------------------------------------------")
run_command("wget -O virtualbox_7.0.10.run https://download.virtualbox.org/virtualbox/7.0.10/VirtualBox-7.0.10-158379-Linux_amd64.run")

run_command("chmod +x virtualbox_7.0.10.run && sudo ./virtualbox_7.0.10.run")
run_command("rm virtualbox_7.0.10.run")

run_command("sudo apt install gcc make perl linux-headers-amd64 linux-headers-$(uname -r)")
run_command("sudo /sbin/vboxconfig")

print("-----------------------------------------------------------------------------")
print("Concluído .....")
print("-----------------------------------------------------------------------------")
