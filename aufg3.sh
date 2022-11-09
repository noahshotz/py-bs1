#!bin/sh

INDEX=$#
echo $INDEX
while [ $INDEX -ge 0 ]
do
    echo "Position" $INDEX ":" ${!INDEX}
    INDEX=$(expr $INDEX - 1)
done