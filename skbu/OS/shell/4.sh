# 4.	Write a shell script that add two integers entered by the user and displays the result.

echo "Enter the first number:";
read a;
echo "Enter the second one:";
read b;
add=`expr $a + $b`;
echo $a "+" $b "=" $add;
