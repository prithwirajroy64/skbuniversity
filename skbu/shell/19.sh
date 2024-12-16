# 19. Write a shell script to calculate the factorial of a given number(using while loop).

echo "Enter a number:";
read n;
fact=1;
while [ $n -gt 1 ]
do
fact=`expr $fact \* $n`;
n=`expr $n - 1`;
done
echo $fact