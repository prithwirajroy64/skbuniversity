# 16. Write a shell script that provides the user with a menu of options to perform the following actions:
# 1.pwd
# 2.ls
# 3.date

echo 1. pwd;
echo 2. ls;
echo 3. date;
echo "enter your choice:"
read a;
case $a in
1) pwd;;
2) ls;;
3) date;;
esac