# 9.	Write a shell script that swaps the values of two integers without using a third variable, based on user input.

echo "Ready to swapping your numbers.";
echo "Enter the first number:";
read a;
echo "Enter the second one:";
read b;

a=`expr $a + $b`;
b=`expr $a - $b`;
a=`expr $a - $b`;

echo "Swaping successful.";
echo "Now your first number is:" $a "and second number is:" $b;