# 17. Write a shell script that performs basic arithmetic operations using case statement. 

echo "Enter a number:"
read a;
echo "Enter second one:"
read b;
echo 1. for  addition;
echo 2. for  subtraction;
echo 3. for  multiplication;
echo 4. for  division;
echo "enter your choice:"
read c;
case $c in
1) echo $a "+" $b "=" `expr $a + $b`;;
2) echo $a "-" $b "=" `expr $a - $b`;;
3) echo $a "×" $b "=" `expr $a \* $b`;;
4) echo $a "÷" $b "=" `expr $a / $b`;;
esac