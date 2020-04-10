echo "sending data to server"
scp -i "paillergpkey.pem" cipher.txt pub.txt priv1.txt h.txt test.txt pub1.txt tot.txt ubuntu@ec2-54-210-237-215.compute-1.amazonaws.com:~ &>/dev/null
echo "done"
