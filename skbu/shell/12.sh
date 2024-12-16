# 12.	Write a shell script which will find largest among three integers.

echo "Enter first number:"
read a;
echo "Enter second number:"
read b;
echo "Enter Third number:"
read c;

if [ $a -gt $b -a $a -gt $c ]
then
echo $a "is largest.";
elif [ $b -gt $c ]
then
echo $b "is largest.";
else
echo $c "is largest.";
fi