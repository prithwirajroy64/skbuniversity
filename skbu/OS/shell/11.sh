# 11.	Write a shell script which will find largest among two integers.

echo "Enter a number:"
read a;
echo "Enter second one:"
read b;

if [ $a -gt $b ]
then
echo $a "is largest.";
else
echo $b "is largest.";
fi