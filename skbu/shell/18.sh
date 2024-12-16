# 18. Write a shell script to calculate the factorial of a given number(using for loop).

echo "Enter a number:";
read n;
fact=1;
for i in $(seq 1 1 $n) # $(seq start step end) by default start with 1 and incres +1
do
fact=`expr $fact \* $i`;
done
echo $fact