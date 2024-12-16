# 5.	Write a shell script that subtracts one integer from another, based on user input, and displays the result.

echo "Enter the first number:";
read a;
echo "Enter the second one:";
read b;
add=`expr $a - $b`;
echo $a "-" $b "=" $add;