# 15.	Write a shell script which will check a number was divisible by 7 and 10.

echo "Check your number divisible by 7 and 10.";
echo "Enter a number:";
read a;

if [ `expr $a % 7` -eq 0 -a `expr $a % 7` -eq 0 ]
then
echo $a "is divisible by 7 & 10";
else
echo $a "is not divisible by 7 & 10";
fi