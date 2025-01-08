# 8.	Write a shell script that checks if a given number (entered by the user) is even or odd.

echo "Check your number even or odd.";
echo "Enter a number:";
read a;

if [ `expr $a % 2` -eq 0 ]
then
echo $a "is even";
else
echo $a "is odd";
fi