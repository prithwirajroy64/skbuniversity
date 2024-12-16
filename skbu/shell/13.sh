# 13.	Write a shell script which will find smallest among two integers.

echo "Enter a number:"
read a;
echo "Enter second one:"
read b;

if [ $a -lt $b ]
then
echo $a "is smallest.";
else
echo $b "is smallest.";
fi