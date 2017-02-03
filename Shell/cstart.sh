#!/bin/bash


#variaveis
contain=$1
app=$2
user=${3:-"root"}

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
        timeBoxIP=0
        ip=$(lxc-ls --fancy | grep -w $cont | awk '{print $3}')
        
        if [ $ip  != "-" -a $timeboxIP -le 5 ]; then
            echo "$ip ..."
            startCONTAIN
        else
            if [ $timeBoxIp -le 5 ]; then
                echo "Timeout..."
                #exit
            else               
                timeBoxIP=`expr $timeBoxIP + 1`
                sleep 1
                getIP
            fi            
        fi
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
        else
            echo "Container $contain ja iniciado!"
        fi
    fi
    
}

sshCONTAIN()
{
    ssh -i ~/.ssh/id_lxc -X -l $user $ip $app
}

startCONTAIN()
{
    getINPUT
}

startCONTAIN

