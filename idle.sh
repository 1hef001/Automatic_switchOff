#!/bin/bash

# actually assign the variable
idle_time=0
# adapted if clause to actually match (see https://stackoverflow.com/questions/18668556/comparing-numbers-in-bash) 
while [ "$idle_time" -lt "900000" ]; do
    idle_time=$(idle_time=exec sudo -u "$whoami" xprintidle)
    echo "$idle_time"
done
killall -u "$whoami"
sudo shutdown -h now

