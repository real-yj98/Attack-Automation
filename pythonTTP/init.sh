#! /bin/bash

service rpcbind stop
gnome-terminal -- msfconsole -q -r msgrpc.rc
