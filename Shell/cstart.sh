#!/bin/bash


#variaveis
app=
ip=
user=
contain=
#funcoes

getINPUT()
{
    if [ $1 ]; then
        echo "Argumento do container existe"
        getCONTAIN
    else
        echo "Argumento do container nao existe"
        #exit
    fi

    if [ $2 ]; then
        echo "Argumento do programa existe"
        getCONTAIN
    else
        echo "Argumento do programa nao existe"
    fi
    
}

getIP()
{

}

getCONTAIN()
{
    Verify=$(lxc-info -n $contain)
    if [ "$Verify" ==  "$contain doesn't exist" ]; then    
        echo "Container não existe!"
        #exit
    else
        Verify=$(lxc-info -n tor | grep State | awk '{print $2}')
        if [ "$Verify" ==  "STOPPED" ]; then    
            echo "Iniciando o container: $contain..."
            lxc-start -n $contain -d
    
}


<<coment

echo "IP AGORA: $ip"
cont=$1
app=$2
user=$3
ip="-"
echo "IP AGORA: $ip"


wip(){
if [ "$ip" == "-" ]; then 
	echo "IP AGORA: $ip"
	echo "sem ip..."
        sleep 1
        ip=$(lxc-ls --fancy | grep -w $cont | awk '{print $3}')
	echo "IP AGORA: $ip"
	wip
	echo "IP AGORA: $ip"

else
echo "IP AGORA: $ip"

	if [ "$ip" == "-" ]; then
echo "IP AGORA: $ip"
		wip
echo "IP AGORA: $ip"

	fi
fi
}
echo "IP AGORA: $ip"

echo "Iniciando o container $cont"
lxc-start -n $cont -d

echo "Obtendo IP do conteiner $cont"
echo "IP AGORA: $ip"

echo "IP AGORA: $ip"
wip

echo "IP AGORA: $ip"
echo "O IP e $ip"
echo "IP AGORA: $ip"

echo "Fazendo acesso SSH para o usuario $user no ip $ip e executando o app $app"
ssh -i ~/.ssh/id_lxc -X -l $user $ip $app 
echo "IP AGORA: $ip"

echo "Finalizando o container $1"
#lxc-stop -n $1
#echo "$1 $2 $3"
coment
echo "a"
