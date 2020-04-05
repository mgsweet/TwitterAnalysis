#!/usr/local/bin/expect
set user xxx
set passwd xxx

set timeout 20
spawn scp -r src $user@spartan.hpc.unimelb.edu.au:/home/$user/assignment1/
expect {
	"password:" { send "$passwd\r"}
}
interact
spawn scp -r scripts $user@spartan.hpc.unimelb.edu.au:/home/$user/assignment1/
expect {
	"password:" { send "$passwd\r"}
}
interact
