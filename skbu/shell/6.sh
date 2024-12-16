# 6.	Write a shell script that performs addition, subtraction, multiplication, and division on two integers provided by the user, and displays the results of each operation.

echo "Enter the first number:";
read a;
echo "Enter the second one:";
read b;
add=`expr $a + $b`;
echo $a "+" $b "=" $add;
sub=`expr $a - $b`;
echo $a "-" $b "=" $sub;
mul=`expr $a \* $b`;
echo $a "×" $b "=" $mul;
div=`expr $a / $b`;
echo $a "÷" $b "=" $div;