# 14.	Write a shell script which will find smallest among three integers.

echo "Enter first number:"
read a;
echo "Enter second number:"
read b;
echo "Enter Third number:"
read c;

if [ $a -lt $b -a $a -lt $c ]
then
echo $a "is smallest.";
elif [ $b -lt $c ]
then
echo $b "is smallest.";
else
echo $c "is smallest.";
fi